FROM python:3.12
RUN pip install yandex-music
COPY ./yandexMusicGETtrack.py /app/
WORKDIR /app
CMD ["python", "./play_track.py"]
