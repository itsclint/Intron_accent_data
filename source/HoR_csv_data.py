"""
This script scrapes wikipeda for tables with infomation for the 9th assembly 
of the nigerian national assembly's lower house and there respective constituencies
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

#fetch links to the wiki pages with contain the data of interest

#House of Rep data
url = requests.get('https://en.wikipedia.org/wiki/List_of_members_of_the_House_of_Representatives_of_Nigeria,_2019%E2%80%932023').text
# Constituency data
url1 = requests.get('https://en.wikipedia.org/wiki/List_of_ethnic_groups_in_Nigeria').text

#parse the html for bith urls
soup = BeautifulSoup(url,'lxml')
soup1 = BeautifulSoup(url1,'lxml')

# Html elements to extract data
Nass_tab = soup.find('table',{'class':'wikitable sortable'})
Eth_tab = soup1.find('table',{'class':'wikitable sortable'})

df = pd.read_html(str(Nass_tab))
df = pd.DataFrame(df[0])

df1 = pd.read_html(str(Eth_tab))
df1= pd.DataFrame(df1[0])
df1 = df1.drop(df1.iloc[:, 2:], axis = 1)
print(df1.head())

df.to_csv('/Users/mbatakuclinton/OpenNass/Source/data/Nass_data.csv', index=False)
df1.to_csv('/Users/mbatakuclinton/OpenNass/Source/data/Ethnic_data.csv', index=False)



