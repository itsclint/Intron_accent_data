import pandas as  pd
import numpy as np
import sqlite3
from Source import youtube



def extract_ytchannel_metadata(res, save_csv=None):
    titles = []
    published = []
    videoIds = []

    for i in range(len(res)):
        titles.append(res[i]['snippet']['title'])
        published.append(res[i]['snippet']['publishedAt'])
        videoIds.append(res[i]['snippet']['resourceId']['videoId'])

    data = np.stack([titles, videoIds, published])
    data = data.T
    df = pd.DataFrame(data, columns=['titles', 'videoIds', 'publishedAt'])
    df.head()

    if save_csv is not None:
        df.to_csv(save_csv, index=None)
        
    return df


def data_entry(TableName, df=None):
    if df is not None:
        conn = sqlite3.connect("opennass.db")
        curr = conn.cursor()
        df.to_sql(TableName, conn, if_exists='replace')
        conn.commit()
        curr.close()
        conn.close()

res = youtube.get_channel_videos('UUF45Z0qCtC3QEB6yoBKMUJQ')
res_df = extract_ytchannel_metadata(res, "Source/data/nass_04062021.csv")   
nass_df = pd.read_csv('/Users/mbatakuclinton/OpenNass/Source/data/Nass_data.csv')
Ethnic_df = pd.read_csv('/Users/mbatakuclinton/OpenNass/Source/data/Ethnic_data.csv')


data_entry('nassVideos', df=res_df)
data_entry('HoRdata', nass_df)
data_entry('ethnicTable', Ethnic_df)



    