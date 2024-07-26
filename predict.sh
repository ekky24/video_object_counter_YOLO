#!/bin/bash
python "yolo_app_accumulate.py" --source "rtsp" --save-img --device 0 --weights "yolov8s.pt" --classes 0 --area $CCTV_AREA
# python "yolo_app_accumulate.py" --source "Crowd.mp4" --save-img --device 0 --weights "yolov8s.pt" --classes 0 --area $CCTV_AREA