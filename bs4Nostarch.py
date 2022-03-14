import requests,bs4

res = requests.get('https://nostarch.com')
nostarchSoup = bs4.BeautifulSoup(res.text,'html.parser')
print(type(nostarchSoup))
print()
print(nostarchSoup)