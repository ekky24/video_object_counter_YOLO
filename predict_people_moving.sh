#!/bin/bash
python "dist/people_moving.py" --source "rtsp" --save-img --device 0 --weights "yolov8s.pt" --classes 0 --area $CCTV_AREA