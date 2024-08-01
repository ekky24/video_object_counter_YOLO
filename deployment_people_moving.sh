#!/bin/bash
NV="v0.3"
docker build -f Dockerfile_people_moving -t people_moving:$NV .
docker rm people_moving
docker run --log-opt max-size=10m --log-opt max-file=3 -e CCTV_AREA="sol" --name people_moving -v /mnt/data/machine_learning/output/people_moving:/app/output/people_moving --gpus all -d --restart unless-stopped people_moving:$NV
# docker run --log-opt max-size=10m --log-opt max-file=3 -e CCTV_AREA="sol" --name people_moving -v /mnt/data/machine_learning/output/people_moving:/app/output/people_moving --gpus all --rm -it people_moving:$NV /bin/bash
