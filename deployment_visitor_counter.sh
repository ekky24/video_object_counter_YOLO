#!/bin/bash
NV="v2.4"
docker build -f Dockerfile_visitor_counter -t visitor_counter:$NV .


# # Tahu Sumedang
# docker stop visitor_counter_tsu
# docker rm visitor_counter_tsu
# docker run --cpus="8" --ulimit nproc=8 --memory="2000m" --network="host" --log-opt max-size=10m --log-opt max-file=3 -e CCTV_AREA="tsu" --name visitor_counter_tsu --gpus all -d --restart unless-stopped visitor_counter:$NV

# # McD
# docker stop visitor_counter_mcd
# docker rm visitor_counter_mcd
# docker run --cpus="8" --ulimit nproc=8 --memory="2000m" --network="host" --log-opt max-size=10m --log-opt max-file=3 -e CCTV_AREA="mcd" --name visitor_counter_mcd --gpus all -d --restart unless-stopped visitor_counter:$NV

# # Masjid
# docker stop visitor_counter_masjid
# docker rm visitor_counter_masjid
# docker run --cpus="8" --ulimit nproc=8 --memory="2000m" --network="host" --log-opt max-size=10m --log-opt max-file=3 -e CCTV_AREA="masjid" --name visitor_counter_masjid --gpus all -d --restart unless-stopped visitor_counter:$NV

# # Solaria
# docker stop visitor_counter_sol
# docker rm visitor_counter_sol
# docker run --cpus="8" --ulimit nproc=8 --memory="2000m" --network="host" --log-opt max-size=10m --log-opt max-file=3 -e CCTV_AREA="sol" --name visitor_counter_sol --gpus all -d --restart unless-stopped visitor_counter:$NV

# # SPKLU
# docker stop visitor_counter_spklu
# docker rm visitor_counter_spklu
# docker run --cpus="8" --ulimit nproc=8 --memory="2000m" --network="host" --log-opt max-size=10m --log-opt max-file=3 -e CCTV_AREA="spklu" --name visitor_counter_spklu --gpus all -d --restart unless-stopped visitor_counter:$NV

# # Cig
# docker stop visitor_counter_cig
# docker rm visitor_counter_cig
# docker run --cpus="8" --ulimit nproc=8 --memory="2000m" --network="host" --log-opt max-size=10m --log-opt max-file=3 -e CCTV_AREA="cig" --name visitor_counter_cig --gpus all -d --restart unless-stopped visitor_counter:$NV

# # Starbucks
# docker stop visitor_counter_stb
# docker rm visitor_counter_stb
# docker run --cpus="8" --ulimit nproc=8 --memory="2000m" --network="host" --log-opt max-size=10m --log-opt max-file=3 -e CCTV_AREA="stb" --name visitor_counter_stb --gpus all -d --restart unless-stopped visitor_counter:$NV

# Toilet
docker stop visitor_counter_toilet
docker rm visitor_counter_toilet
docker run --cpus="8" --ulimit nproc=8 --memory="2000m" --network="host" --log-opt max-size=10m --log-opt max-file=3 -e CCTV_AREA="toilet" --name visitor_counter_toilet --gpus all -d --restart unless-stopped visitor_counter:$NV