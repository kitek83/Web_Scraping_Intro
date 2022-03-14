import bs4, requests,webbrowser
search  = input('Enter searched word: ')
print('Searching...')
res = requests.get('https://pypi.org/search/?q=' + search)
soup = bs4.BeautifulSoup(res.text, 'html.parser')

linkElem = soup.select('.package-snippet')

numOpen = min(5,len(linkElem))

for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElem[i].get('href')
    print('Opening',urlToOpen)
    webbrowser.open(urlToOpen)
