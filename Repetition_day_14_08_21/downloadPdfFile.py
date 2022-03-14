import requests

download = requests.get('https://theanimalfund.net/wp-content/uploads/2020/06/Norway-DOC-1-from-Helena.pdf')
print(download.status_code == requests.codes.ok)
print(download.raise_for_status())

fileNorway = open('Norway.pdf','wb')
for chunk in download.iter_content(100000):
    fileNorway.write(chunk)

