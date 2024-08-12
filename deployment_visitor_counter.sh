#!/bin/bash
NV="v1.0"
docker build -f Dockerfile_visitor_counter -t visitor_counter:$NV .


# Tahu Sumedang
docker stop visitor_counter_tsu
docker rm visitor_counter_tsu
docker run --log-opt max-size=10m --log-opt max-file=3 -e CCTV_AREA="tsu" --name visitor_counter_tsu -v /mnt/nvme2n1/machine_learning/output/visitor_counter:/app/output/visitor_counter --gpus all -d --restart unless-stopped visitor_counter:$NV

# McD
docker stop visitor_counter_mcd
docker rm visitor_counter_mcd
docker run --log-opt max-size=10m --log-opt max-file=3 -e CCTV_AREA="mcd" --name visitor_counter_mcd -v /mnt/nvme2n1/machine_learning/output/visitor_counter:/app/output/visitor_counter --gpus all -d --restart unless-stopped visitor_counter:$NV

# Masjid
docker stop visitor_counter_masjid
docker rm visitor_counter_masjid
docker run --log-opt max-size=10m --log-opt max-file=3 -e CCTV_AREA="masjid" --name visitor_counter_masjid -v /mnt/nvme2n1/machine_learning/output/visitor_counter:/app/output/visitor_counter --gpus all -d --restart unless-stopped visitor_counter:$NV

# Solaria
docker stop visitor_counter_sol
docker rm visitor_counter_sol
docker run --log-opt max-size=10m --log-opt max-file=3 -e CCTV_AREA="sol" --name visitor_counter_sol -v /mnt/nvme2n1/machine_learning/output/visitor_counter:/app/output/visitor_counter --gpus all -d --restart unless-stopped visitor_counter:$NV

# SPKLU
docker stop visitor_counter_spklu
docker rm visitor_counter_spklu
docker run --log-opt max-size=10m --log-opt max-file=3 -e CCTV_AREA="spklu" --name visitor_counter_spklu -v /mnt/nvme2n1/machine_learning/output/visitor_counter:/app/output/visitor_counter --gpus all -d --restart unless-stopped visitor_counter:$NV

# Cig
docker stop visitor_counter_cig
docker rm visitor_counter_cig
docker run --log-opt max-size=10m --log-opt max-file=3 -e CCTV_AREA="cig" --name visitor_counter_cig -v /mnt/nvme2n1/machine_learning/output/visitor_counter:/app/output/visitor_counter --gpus all -d --restart unless-stopped visitor_counter:$NV

# Starbucks
docker stop visitor_counter_stb
docker rm visitor_counter_stb
docker run --log-opt max-size=10m --log-opt max-file=3 -e CCTV_AREA="stb" --name visitor_counter_stb -v /mnt/nvme2n1/machine_learning/output/visitor_counter:/app/output/visitor_counter --gpus all -d --restart unless-stopped visitor_counter:$NV

# Toilet
docker stop visitor_counter_toilet
docker rm visitor_counter_toilet
docker run --log-opt max-size=10m --log-opt max-file=3 -e CCTV_AREA="toilet" --name visitor_counter_toilet -v /mnt/nvme2n1/machine_learning/output/visitor_counter:/app/output/visitor_counter --gpus all -d --restart unless-stopped visitor_counter:$NV