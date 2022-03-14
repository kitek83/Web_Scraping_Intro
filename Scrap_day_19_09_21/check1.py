from youtubesearchpython import VideosSearch
import bs4, requests
from urllib.request import urlopen
import json

videosSearch = VideosSearch('atb', limit=10)
#print(videosSearch.result())
list = []
result = videosSearch.result()
print(result)
list.append(result)
print('---------------------------')
print()
with open('convert.txt','w') as convert_file:
    convert_file.write(json.dumps(result))

convertFile = open('convert.txt','r')
soup = bs4.BeautifulSoup(convertFile.read(),'html.parser')

links = soup.select('#link')
print(links)

