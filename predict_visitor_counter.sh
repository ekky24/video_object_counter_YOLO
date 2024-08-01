#!/bin/bash
python "dist/visitor_counter.py" --source "rtsp" --save-img --device 0 --weights "yolov8s.pt" --classes 0 --area $CCTV_AREA
# python "dist/visitor_counter.py" --source "Crowd.mp4" --save-img --device 0 --weights "yolov8s.pt" --classes 0 --area $CCTV_AREA