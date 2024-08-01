#!/bin/bash
NV="v0.6"
docker build -f Dockerfile_visitor_counter -t visitor_counter:$NV .
docker rm visitor_counter
docker run --log-opt max-size=10m --log-opt max-file=3 -e CCTV_AREA="sol" --name visitor_counter -v /mnt/data/machine_learning/output/visitor_counter:/app/output/visitor_counter --gpus all -d --restart unless-stopped visitor_counter:v0.5
# docker run --log-opt max-size=10m --log-opt max-file=3 -e CCTV_AREA="sol" --name visitor_counter -v /mnt/data/machine_learning/output/visitor_counter:/app/output/visitor_counter --gpus all --rm -it visitor_counter:v0.5 /bin/bash
