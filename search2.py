import webbrowser

import requests,bs4

search = input('Enter the word you are looking for: ')
res = requests.get('https://www.google.com/search?client=firefox-b-d&q=' + search)

soup = bs4.BeautifulSoup(res.text, 'html.parser')
sele = soup.select('.cite')

numOpen = min(5,len(sele))
for i in range(numOpen):
    urlToOpen = 'https://www.google.com' + sele[i]
    print('Opening',urlToOpen)
    webbrowser.open(urlToOpen)