#!/bin/bash
NV="v2.3"
docker build -f Dockerfile_people_moving -t people_moving:$NV .


# # Tahu Sumedang
# docker stop people_moving_tsu
# docker rm people_moving_tsu
# docker run --memory="2000m" --network="host" --log-opt max-size=10m --log-opt max-file=3 -e CCTV_AREA="tsu" --name people_moving_tsu --gpus all -d --restart unless-stopped people_moving:$NV

# McD
docker stop people_moving_mcd
docker rm people_moving_mcd
docker run --memory="2000m" --network="host" --log-opt max-size=10m --log-opt max-file=3 -e CCTV_AREA="mcd" --name people_moving_mcd --gpus all -d --restart unless-stopped people_moving:$NV

# # Masjid
# docker stop people_moving_masjid
# docker rm people_moving_masjid
# docker run --memory="2000m" --network="host" --log-opt max-size=10m --log-opt max-file=3 -e CCTV_AREA="masjid" --name people_moving_masjid --gpus all -d --restart unless-stopped people_moving:$NV

# # Solaria
# docker stop people_moving_sol
# docker rm people_moving_sol
# docker run --memory="2000m" --network="host" --log-opt max-size=10m --log-opt max-file=3 -e CCTV_AREA="sol" --name people_moving_sol --gpus all -d --restart unless-stopped people_moving:$NV

# # SPKLU
# docker stop people_moving_spklu
# docker rm people_moving_spklu
# docker run --memory="2000m" --network="host" --log-opt max-size=10m --log-opt max-file=3 -e CCTV_AREA="spklu" --name people_moving_spklu --gpus all -d --restart unless-stopped people_moving:$NV

# # Cig
# docker stop people_moving_cig
# docker rm people_moving_cig
# docker run --memory="2000m" --network="host" --log-opt max-size=10m --log-opt max-file=3 -e CCTV_AREA="cig" --name people_moving_cig --gpus all -d --restart unless-stopped people_moving:$NV

# # Starbucks
# docker stop people_moving_stb
# docker rm people_moving_stb
# docker run --memory="2000m" --network="host" --log-opt max-size=10m --log-opt max-file=3 -e CCTV_AREA="stb" --name people_moving_stb --gpus all -d --restart unless-stopped people_moving:$NV

# Toilet
docker stop people_moving_toilet
docker rm people_moving_toilet
docker run --memory="2000m" --network="host" --log-opt max-size=10m --log-opt max-file=3 -e CCTV_AREA="toilet" --name people_moving_toilet --gpus all -d --restart unless-stopped people_moving:$NV