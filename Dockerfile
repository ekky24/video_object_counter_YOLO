FROM python:3.10.14-slim

COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

RUN chmod -R 777 /app

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

ENTRYPOINT ["./predict.sh"]