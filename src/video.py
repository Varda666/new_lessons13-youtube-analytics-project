#
from googleapiclient.discovery import build
import os
from src.channel import Channel
# import json
# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('API_KEY')


# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)
# print([method for method in dir(youtube) if callable(getattr(youtube, method))])

class UncorrectVideoId(Exception):
    def __init__(self, *args, **kwargs):
        pass



class Video:
    def __init__(self, video_id: str):
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.video_id = video_id
        try:
            self.video = youtube.videos().list(id=self.video_id, part='snippet,statistics').execute()
            if self.video["items"] != []:
                self.video_title = self.video["items"][0]["snippet"]["title"]
                self.video_description = self.video['items'][0]['snippet']['description']
                self.url = "https://www.youtube.com/video/" + self.video_id
                self.view_count = self.video['items'][0]['statistics']['viewCount']
                self.like_count = self.video['items'][0]['statistics']['likeCount']
            elif self.video["items"] == []:
                self.video_title = None
                self.video_description = None
                self.url = None
                self.view_count = None
                self.like_count = None
        except UncorrectVideoId:
            print('')









    def __str__(self):
        super().__str__()
        return f'{self.video_title}'

class PLVideo(Channel):
    def __init__(self, video_id: str, channel_id: str):
        self.video_id = video_id
        self.video = youtube.videos().list(id=self.video_id, part='snippet,statistics').execute()
        self.video_title = self.video["items"][0]["snippet"]["title"]
        self.__channel_id = channel_id

    def __str__(self):
        return f'{self.video_title}'



#
# print(youtube.videos().list(id='4fObz_qw9u4', part='snippet,statistics').execute())
# with open('moscowpythonvideo.json', 'w', encoding="ascii") as f:
#     json.dump(youtube.videos().list(id='4fObz_qw9u4', part='snippet,statistics').execute(), f)
