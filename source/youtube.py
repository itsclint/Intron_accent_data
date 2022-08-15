
from googleapiclient.discovery import build

api_key = "AIzaSyC7La5niFMUSATiXqNc2ySzwN82zGK5U_g"

youtube = build('youtube', 'v3', developerKey=api_key)


def get_channel_videos(channel_id):
    
    videos = []
    next_page_token = None
    
    while 1:
        res = youtube.playlistItems().list(playlistId=channel_id, 
                                           part='snippet', 
                                           maxResults=50,
                                           pageToken=next_page_token).execute()
        videos += res['items']
        next_page_token = res.get('nextPageToken')
        
        if next_page_token is None:
            break
    
    return videos

    





