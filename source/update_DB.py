import datetime
from source import Create_DB, youtube


today = datetime.datetime.now()
querytime = today.strftime('%d_%m_%Y')
res = youtube.get_channel_videos('UUF45Z0qCtC3QEB6yoBKMUJQ')
res_df = Create_DB.extract_ytchannel_metadata(res, "Source/data/nass_04062021.csv") 

table_name = 'nassVIdeos'+ '_' + querytime
Create_DB.data_entry(table_name, res_df)