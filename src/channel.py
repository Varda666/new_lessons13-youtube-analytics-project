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
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.channel = youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.title = self.channel["items"][0]["snippet"]["title"]
        self.channel_description = self.channel['items'][0]['snippet']['description']
        self.url = "https://www.youtube.com/channel/" + self.__channel_id
        self.subscriber_count = int(self.channel['items'][0]['statistics']['subscriberCount'])
        self.video_count = self.channel['items'][0]['statistics']['videoCount']
        self.view_count = self.channel['items'][0]['statistics']['viewCount']

    def __str__(self):
        """Возвращает название и ссылку на канал"""
        return f'{self.title} ({self.url})'

    def __add__(self, other):
        """ Складывает два канала между собой по количеству подписчиков """
        return self.subscriber_count + other.subscriber_count

    def __sub__(self, other):
        """ Возвращает разницу в количестве подписчиков двух каналов """
        if self.subscriber_count > other.subscriber_count:
            return self.subscriber_count - other.subscriber_count
        else:
            return other.subscriber_count - self.subscriber_count

    def __lt__(self, other):
        """ Сравнивает количество подписчиков двух каналов """
        return self.subscriber_count < other.subscriber_count

    def __le__(self, other):
        """ Сравнивает количество подписчиков двух каналов """
        return self.subscriber_count <= other.subscriber_count

    def __gt__(self, other):
        """ Сравнивает количество подписчиков двух каналов """
        return self.subscriber_count > other.subscriber_count

    def __ge__(self, other):
        """ Сравнивает количество подписчиков двух каналов """
        return self.subscriber_count >= other.subscriber_count


    def get_info(self):
        """Выводит информацию о канале в dict."""
        channel = youtube.channels().list(id=id, part='snippet,statistics').execute()
        return channel


    def print_info(self):
        """Выводит в консоль информацию о канале."""
        channel = youtube.channels().list(id=self.id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    @staticmethod
    def get_service():
        """Возвращает объект для работы с YouTube API"""
        return youtube

    def to_json(self, file):
        channel = youtube.channels().list(id=id, part='snippet,statistics').execute()
        with open(file, 'w') as f:
            json.dump([self.__channel_id, self.title, self.channel_description, self.url, self.subscriber_count, self.video_count, self.view_count], f)

# self.__channel_id, self.title, self.channel_description, self.url, self.subscriber_count, self.video_count, self.view_count


# print(youtube.channels().list(id='UC-OVMPlMA3-YCIeg4z5z23A', part='snippet, statistic').execute())





