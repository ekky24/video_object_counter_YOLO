#!/bin/bash
NV="v2.0"
docker build -f Dockerfile_people_moving -t people_moving:$NV .


# # Tahu Sumedang
# docker stop people_moving_tsu
# docker rm people_moving_tsu
# docker run --memory="2000m" --network="host" --log-opt max-size=10m --log-opt max-file=3 -e CCTV_AREA="tsu" --name people_moving_tsu -v /mnt/nvme2n1/machine_learning/output/people_moving:/app/output/people_moving --gpus all -d --restart unless-stopped people_moving:$NV

# McD
docker stop people_moving_mcd
docker rm people_moving_mcd
docker run --memory="2000m" --network="host" --log-opt max-size=10m --log-opt max-file=3 -e CCTV_AREA="mcd" --name people_moving_mcd -v /mnt/nvme2n1/machine_learning/output/people_moving:/app/output/people_moving --gpus all -d --restart unless-stopped people_moving:$NV

# # Masjid
# docker stop people_moving_masjid
# docker rm people_moving_masjid
# docker run --memory="2000m" --network="host" --log-opt max-size=10m --log-opt max-file=3 -e CCTV_AREA="masjid" --name people_moving_masjid -v /mnt/nvme2n1/machine_learning/output/people_moving:/app/output/people_moving --gpus all -d --restart unless-stopped people_moving:$NV

# # Solaria
# docker stop people_moving_sol
# docker rm people_moving_sol
# docker run --memory="2000m" --network="host" --log-opt max-size=10m --log-opt max-file=3 -e CCTV_AREA="sol" --name people_moving_sol -v /mnt/nvme2n1/machine_learning/output/people_moving:/app/output/people_moving --gpus all -d --restart unless-stopped people_moving:$NV

# # SPKLU
# docker stop people_moving_spklu
# docker rm people_moving_spklu
# docker run --memory="2000m" --network="host" --log-opt max-size=10m --log-opt max-file=3 -e CCTV_AREA="spklu" --name people_moving_spklu -v /mnt/nvme2n1/machine_learning/output/people_moving:/app/output/people_moving --gpus all -d --restart unless-stopped people_moving:$NV

# # Cig
# docker stop people_moving_cig
# docker rm people_moving_cig
# docker run --memory="2000m" --network="host" --log-opt max-size=10m --log-opt max-file=3 -e CCTV_AREA="cig" --name people_moving_cig -v /mnt/nvme2n1/machine_learning/output/people_moving:/app/output/people_moving --gpus all -d --restart unless-stopped people_moving:$NV

# # Starbucks
# docker stop people_moving_stb
# docker rm people_moving_stb
# docker run --memory="2000m" --network="host" --log-opt max-size=10m --log-opt max-file=3 -e CCTV_AREA="stb" --name people_moving_stb -v /mnt/nvme2n1/machine_learning/output/people_moving:/app/output/people_moving --gpus all -d --restart unless-stopped people_moving:$NV

# # Toilet
# docker stop people_moving_toilet
# docker rm people_moving_toilet
# docker run --memory="2000m" --network="host" --log-opt max-size=10m --log-opt max-file=3 -e CCTV_AREA="toilet" --name people_moving_toilet -v /mnt/nvme2n1/machine_learning/output/people_moving:/app/output/people_moving --gpus all -d --restart unless-stopped people_moving:$NV