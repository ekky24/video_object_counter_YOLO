#!/bin/bash
python "dist/people_moving.py" --source "rtsp" --save-img --device 0 --weights "yolov8l.pt" --classes 0 --area $CCTV_AREA