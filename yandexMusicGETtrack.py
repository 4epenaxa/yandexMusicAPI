import requests
from yandex_music import Client
import os

# Читаем токен из переменной среды
token = os.getenv("YANDEX_MUSIC_TOKEN")

if not token:
    raise ValueError("Токен не установлен. Убедитесь, что переменная среды YANDEX_MUSIC_TOKEN настроена.")
response = requests.get("http://ymmbfa.mipoh.ru/get_current_track_beta", headers={"ya-token": token})
if response.status_code != 200:
    print(f"Ошибка при получении данных: {response.status_code}, {response.text}")
else:
    try:
        data = response.json()
        track_id = data["track"]["track_id"]
        client = Client(token).init()
        track = client.tracks(track_id)[0]
        version = getattr(track, 'version', '')
        if version:
            track_title = f"{track.title} ({version})"
        else:
            track_title = track.title
        artists = ', '.join([artist.name for artist in track.artists])
        # Преобразование обложки доделать
        # cover_uri = track.cover.replace('%%', '300x300')

        print(f"{track_title} - {artists}")
        # print(cover_uri)
    except AttributeError as ae:
        print(f"Ошибка доступа к атрибуту: {ae}")
    except Exception as ex:
        print(f"Общая ошибка: {ex}")
