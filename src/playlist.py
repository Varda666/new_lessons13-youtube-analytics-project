import isodate
from googleapiclient.discovery import build
import os

import datetime
# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('API_KEY')


# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)

class PlayList():
    def __init__(self, playlist_id: str):
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.playlist_id = playlist_id
        self.playlist = youtube.playlists().list(id=self.playlist_id, part='contentDetails, snippet', maxResults=50).execute()
        self.playlist_title = self.playlist["items"][0]["snippet"]["title"]
        self.url = "https://www.youtube.com/playlist?list=" + self.playlist_id

    def __str__(self):
        return f'{self.playlist}'

    @property
    def total_duration(self):
        """Возвращает объект класса `datetime.timedelta` с суммарной длительность плейлиста (обращение как к свойству"""
        playlist_videos = youtube.playlistItems().list(playlistId=self.playlist_id, part='contentDetails').execute()
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        video_response = youtube.videos().list(part='contentDetails,statistics', id=','.join(video_ids)).execute()
        duration_videos = []
        for video in video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            duration_videos.append(duration)
        total_duration = datetime.timedelta()
        for dur in duration_videos:
            total_duration += dur
        return total_duration



    def show_best_video(self):
        """возвращает ссылку на самое популярное видео из плейлиста (по количеству лайков)"""
        playlist_videos = youtube.playlistItems().list(playlistId='PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw',
                                                       part='contentDetails').execute()
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        video_response = youtube.videos().list(part='contentDetails,statistics', id=','.join(video_ids)).execute()
        max_likecount = 0
        video_id = ''
        for item in video_response["items"]:
            if int(item["statistics"]["likeCount"]) > int(max_likecount):
                max_likecount = item["statistics"]["likeCount"]
                video_id = item["id"]
            else:
                continue

        return f'https://www.youtube.be/{video_id}'




#