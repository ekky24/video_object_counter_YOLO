#!/bin/bash
NV="v2.3"
docker build -f Dockerfile_people_moving -t people_moving:$NV .


# # McD
# docker stop people_moving_mcd
# docker rm people_moving_mcd
# docker run --memory="2000m" --network="host" --log-opt max-size=10m --log-opt max-file=3 -e CCTV_AREA="mcd" --name people_moving_mcd --gpus all -d --restart unless-stopped people_moving:$NV

# Toilet
docker stop people_moving_toilet
docker rm people_moving_toilet
docker run --cpus="8" --ulimit nproc=8 --memory="2000m" --network="host" --log-opt max-size=10m --log-opt max-file=3 -e CCTV_AREA="toilet" --name people_moving_toilet --gpus all -d --restart unless-stopped people_moving:$NV