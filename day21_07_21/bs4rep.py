import requests, bs4

res = requests.get('https://nostarch.com/')
print(res)
soupObject = bs4.BeautifulSoup(res.text,'html.parser')
print(res.raise_for_status())
print(type(soupObject))
#print(soupObject)