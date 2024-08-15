import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
previous_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(previous_dir)

import argparse
import pytz
import time
from collections import defaultdict
from pathlib import Path

import cv2
import numpy as np
from shapely.geometry import Polygon
from shapely.geometry.point import Point

from ultralytics import YOLO
from ultralytics.utils.files import increment_path
from ultralytics.utils.plotting import Annotator, colors
import torch
from datetime import datetime
import sqlalchemy as db
import pandas as pd
import subprocess

from data.db_credentials import DB_CONFIG
import dist.config_people_moving as config_people_moving

import shutil

os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

current_region = None

def cleaning(VideoCapture, cv2, save_dir, str_curr_ts):
    VideoCapture.release()
    cv2.destroyAllWindows()

    # clearing tmp
    try:
        os.remove(f"{save_dir}/{str_curr_ts}.mp4")
    except FileNotFoundError:
        print(f"File not found.")
    except PermissionError:
        print(f"Permission denied to delete.")
    except Exception as e:
        print(f"Error occurred while trying to delete: {e}")

def connect_rtsp(source, codec, frame_w, frame_h, save_dir, str_curr_ts):
    # Video Setup
    VideoCapture = cv2.VideoCapture(source)
    VideoCapture.set(cv2.CAP_PROP_FPS, config_people_moving.FRAME_RATE)
    frame_w_0, frame_h_0, fps = (int(VideoCapture.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, 
                                                                cv2.CAP_PROP_FRAME_HEIGHT, 
                                                                cv2.CAP_PROP_FPS
                                       ))

    video_writer = cv2.VideoWriter(f"{save_dir}/{str_curr_ts}.mp4",
                cv2.VideoWriter_fourcc(*codec), 12, (frame_w,frame_h))
    
    return VideoCapture, video_writer

def run(
        weights="yolov10m.pt",
        source=None,
        device="gpu",
        view_img=False,
        save_img=False,
        exist_ok=False,
        classes=None,
        line_thickness=2,
        region_thickness=2,
        counter_accumulated=False,
        area=None
):
    """
    Run Region counting on a video using YOLOv10 and ByteTrack.

    Supports movable region for real time counting inside specific area.
    Supports multiple regions counting.
    Regions can be Polygons or rectangle in shape

    Args:
        weights (str): Model weights path.
        source (str): Video file path.
        device (str): processing device cpu, 0, 1
        view_img (bool): Show results.
        save_img (bool): Save results.
        exist_ok (bool): Overwrite existing files.
        classes (list): classes to detect and track
        line_thickness (int): Bounding box thickness.
        track_thickness (int): Tracking line thickness
        region_thickness (int): Region thickness.
        counter_accumulated (bool) : accumulation counter
    """

    save_interval = 10
    rtsp_server_url = f"rtsp://localhost:8554/people_moving/{area}"
    ffmpeg_command = [
        'ffmpeg',
        '-y',  # Overwrite output files
        '-f', 'rawvideo',  # Input format
        '-vcodec', 'rawvideo',
        '-pix_fmt', 'bgr24',  # Pixel format
        '-s', '640x360',  # Frame size
        '-r', '12',  # Frame rate
        '-i', '-',  # Input from stdin
        '-c:v', 'libx264',  # Video codec
        '-pix_fmt', 'yuv420p',  # Output pixel format
        '-f', 'rtsp',  # Output format
        rtsp_server_url  # Output URL
    ]
    timezone = pytz.timezone(config_people_moving.TIMEZONE)

    # Check source path
    if source == 'rtsp':
        cctv_host = config_people_moving.LOCATION_CONF[area]['host']
        cctv_username = config_people_moving.LOCATION_CONF[area]['username']
        cctv_pass = config_people_moving.LOCATION_CONF[area]['password']
        cctv_area = config_people_moving.LOCATION_CONF[area]['area']

        source = f"rtsp://{cctv_username}:{cctv_pass}@{cctv_host}"

        counting_region = config_people_moving.LOCATION_CONF[area]['region']
    
    else:
        counting_region = [
            {
                "name": "sol_1",
                "polygon": Polygon([(440, 91), (510, 89), (465, 358), (217, 357)]),  # Polygon points
                "counts": 0,
                "draggin": False,
                "region_color": (37, 255, 255), # BGR value
                "text_color": (0, 0, 0) # Region text color
            }
        ]
        cctv_area = 'sol'
        if not Path(source).exists():
            raise FileNotFoundError(f"Source path '{source}' does not exist.")
    
    # Setup Model
    model = YOLO(f"{weights}")
    if torch.cuda.is_available():
        print("GPU is available.")
        device = torch.device('cuda')
    else:
        print("GPU is not available, using CPU.")
        device = torch.device('cpu')

    model.to(device)

    # Extract class names
    names = model.model.names

    frame_w, frame_h = 1280, 720
    codec = "mp4v"
    curr_ts = datetime.now(timezone)
    str_curr_date = curr_ts.strftime("%Y%m%d")
    str_curr_ts = curr_ts.strftime("%Y%m%d_%H%M%S")

    # save_dir = f'output/people_moving/{cctv_area}/{str_curr_date}'
    save_dir = f'output/people_moving/tmp/{cctv_area}/{str_curr_date}'
    if not os.path.isdir(save_dir):
        os.makedirs(save_dir)
        os.makedirs(save_dir.replace('/tmp', ''))

    VideoCapture, video_writer = connect_rtsp(source, codec, frame_w, frame_h, save_dir, str_curr_ts)
    
    # Iterate and analyze over video frames
    track_history = defaultdict(list)
    count_ids = []
    prev_time = 0
    save_start_time = time.time()
    process = subprocess.Popen(ffmpeg_command, stdin=subprocess.PIPE)

    while True:
        save_curr_time = time.time()

        sucess, frame = VideoCapture.read()
        if not sucess:
            print('INFO: Video read failed')

            # reconnecting and cleaning
            cleaning(VideoCapture, cv2, save_dir, str_curr_ts)
            VideoCapture, video_writer = connect_rtsp(source, codec, frame_w, frame_h, save_dir, str_curr_ts)

            continue
        
        frame = cv2.resize(frame, (frame_w, frame_h))

        curr_time = time.time()
        fps = 1 / (curr_time - prev_time)
        prev_time = curr_time

        cv2.rectangle(frame, (55, 682), (427, 712), (255, 255, 255), -1)
        cv2.putText(frame, datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S"), (56, 709), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1, cv2.LINE_AA)

        # Extract the results
        results = model.track(frame, persist=True, classes=classes)

        if results[0].boxes.id is not None:
            boxes = results[0].boxes.xyxy.cpu()
            track_ids = results[0].boxes.id.int().cpu().tolist()
            clss = results[0].boxes.cls.cpu().tolist()
            annotator = Annotator(frame, line_width=line_thickness, example=str(names))

            for box, track_id, cls in zip(boxes, track_ids, clss):
                bbox_center = (box[0] + box[2]) / 2, (box[1] + box[3]) / 2

                track = track_history[track_id] # Tracking lines plot
                track.append((float(bbox_center[0]), float(bbox_center[1])))
                if len(track) > 30:
                    track.pop(0)

                prev_position = track_history[track_id][-2] if len(track_history[track_id]) > 1 else None
                
                # Check if detection inside region
                for region in counting_region:
                    is_inside_region = region["polygon"].contains(Point((bbox_center[0], bbox_center[1])))
                    # print(counter_accumulated)
                    if is_inside_region:
                        annotator.box_label(box, color=colors(cls,True)) # kotak deteksi yg didalam region
                        if not counter_accumulated:
                            region["counts"] += 1
                        elif counter_accumulated and prev_position is not None and track_id not in count_ids:
                            count_ids.append(track_id)
                            region["counts"] += 1
                            

        # Draw regions (Polygons/Rectangles)
        for region in counting_region:
            region_label = str(region["counts"])
            region_color = region["region_color"]
            region_text_color = region["text_color"]

            polygon_coords = np.array(region["polygon"].exterior.coords, dtype=np.int32)
            centroid_x, centroid_y = int(region["polygon"].centroid.x), int(region["polygon"].centroid.y)

            text_size, _ =cv2.getTextSize(
                region_label, cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.7, thickness=line_thickness
            )
            text_x = centroid_x - text_size[0] // 2
            text_y = centroid_y + text_size[1] // 2
            cv2.rectangle(
                frame,
                (text_x -5, text_y - text_size[1]-5),
                (text_x + text_size[0] + 5, text_y + 5),
                region_color,
                -1
            )
            cv2.putText(
                frame, region_label, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, region_text_color, line_thickness
            )
            cv2.polylines(frame, [polygon_coords], isClosed=True, color=region_color, thickness=region_thickness)
        
        # save output and db
        if save_curr_time - save_start_time >= save_interval:
            source_vid_path = f"{save_dir}/{str_curr_ts}.mp4"
            dest_vid_path = f"{save_dir.replace('/tmp', '')}/{str_curr_ts}.mp4"

            updated_ts = datetime.now(timezone)
            str_curr_ts = updated_ts.strftime("%Y%m%d_%H%M%S")

            save_start_time = save_curr_time
            video_writer.release()

            # check if file video is corrupt
            if os.path.exists(source_vid_path):
                file_size = os.path.getsize(source_vid_path)
                if file_size > config_people_moving.FILE_SIZE_THRESHOLD * 1024:
                    # move file to final dir
                    shutil.move(source_vid_path, dest_vid_path)

            if curr_ts.date() != updated_ts.date():
                curr_ts = updated_ts
                str_curr_date = curr_ts.strftime("%Y%m%d")
                save_dir = f'output/people_moving/tmp/{cctv_area}/{str_curr_date}'
                if not os.path.isdir(save_dir):
                    os.makedirs(save_dir)
                    os.makedirs(save_dir.replace('/tmp', ''))

            video_writer = cv2.VideoWriter(f"{save_dir}/{str_curr_ts}.mp4",
                        cv2.VideoWriter_fourcc(*codec), fps, (frame_w,frame_h))

            # save db
            new_data = {
                'count': [],
                'area': [],
            }
            for i, region in enumerate(counting_region):
                new_data['count'].append(region["counts"])
                new_data['area'].append(region["name"])

            new_data_df = pd.DataFrame(new_data)

            engine = db.create_engine(f"mysql+mysqlconnector://{DB_CONFIG['username']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/cctv",echo=False)
            new_data_df.to_sql('people_moving', con=engine, if_exists="append", index=False)
            engine.dispose()

        print(f"FPS : {fps:.2f}")

        # Send to RTSP Stream 
        frame_resize = cv2.resize(frame, (640, 360))
        process.stdin.write(frame_resize.tobytes())

        if view_img:
            cv2.imshow("Crowd Counter POC", frame)
        
        if save_img:
            video_writer.write(frame)
        
        if not counter_accumulated:
            for region in counting_region: # Reinitialize counter 
                region["counts"] = 0
            
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cleaning(VideoCapture, cv2, save_dir, str_curr_ts)
    video_writer.release()

    process.stdin.close()
    process.wait()   

def parse_opt():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--weights", type=str, default="yolov8n.pt", help="initial weights path")
    parser.add_argument("--device", default="", help="cuda device, i.e. 0 or 0,1,2,3 or cpu")
    parser.add_argument("--source", type=str, required=True, help="video file path")
    parser.add_argument("--view-img", action="store_true", help="show results")
    parser.add_argument("--save-img", action="store_true", help="save results")
    parser.add_argument("--exist-ok", action="store_true", help="existing project/name ok, do not increment")
    parser.add_argument("--classes", nargs="+", type=int, help="filter by class: --classes 0, or --classes 0 2 3")
    parser.add_argument("--line-thickness", type=int, default=2, help="bounding box thickness")
    parser.add_argument("--region-thickness", type=int, default=4, help="Region thickness")
    parser.add_argument("--counter-accumulated", action="store_true", help="accumulated counter")
    parser.add_argument("--area", type=str, default="", help="CCTV location")

    return parser.parse_args()


def main(opt):
    """Main function."""
    run(**vars(opt))


if __name__ == "__main__":
    opt = parse_opt()
    main(opt)
