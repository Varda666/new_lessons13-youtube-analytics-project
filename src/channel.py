import json
import os

# необходимо установить через: pip install google-api-python-client
from googleapiclient.discovery import build

import isodate


# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('API_KEY')


# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)

# def printj(dict_to_print: dict):
#     """Выводит словарь в json-подобном удобном формате с отступами"""
#     print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))
#
# channel_id = 'UCwHL6WHUarjGfUM_586me8w'  # HighLoad Channel
# channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
# printj(channel)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str):
        self.id = channel_id
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""


    def print_info(self):
        """Выводит в консоль информацию о канале."""
        channel = youtube.channels().list(id=self.id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

