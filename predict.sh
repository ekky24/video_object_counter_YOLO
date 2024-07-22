#!/bin/bash
python "yolo_app_accumulate.py" --source "rtsp" --save-img --device 0 --weights "yolov8s.pt" --classes 0 --capacity 15