import webbrowser

import requests,bs4

search = input('Enter thr word you are looking for:')
res = requests.get('https://nostarch.com/search/' + search)
soup = bs4.BeautifulSoup(res.text, 'html.parser')
sele = soup.select('a')

numOpens = min(10,len(sele))

for i in range(numOpens):
    urlToOpen = 'https://nostarch.com' + sele[i].get('href')
    print('Opening' + urlToOpen)
    webbrowser.open(urlToOpen)