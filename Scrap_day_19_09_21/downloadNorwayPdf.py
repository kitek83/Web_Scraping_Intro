import requests

res = requests.get('https://assets.simpleviewcms.com/simpleview/image/upload/v1/clients/norway/Norway_in_your_pocket_2018_F_3f710b4e-eeca-490b-86b2-7e4dca303633.pdf')
fileNorway = open('Norway1.pdf','wb')

for chunk in res.iter_content(100000):
    fileNorway.write(chunk)

fileNorway.close()
