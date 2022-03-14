import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(res.status_code == requests.codes.ok)
print(len(res.text))
print('-----------------------')
print(res.raise_for_status())
print('----------------------')
fileRomeoJuliet = open('RomeoJuliet.txt','wb')

for chunk in res.iter_content(100000):
    fileRomeoJuliet.write(chunk)
