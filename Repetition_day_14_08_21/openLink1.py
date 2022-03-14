import bs4, requests, webbrowser

search = input('Enter a word you are looking for:')
page = requests.get('https://pypi.org/search/?q=' + search)  #downloaded the web page with searched phrase as html
#parsing the web page and selecting '.package-snippet'
soup = bs4.BeautifulSoup(page.text, 'html.parser')
selectPacgage = soup.select('.package-snippet')

#setting range of web pages to opened in webbrowser
number = min(10,len(selectPacgage))
#opening first 10 links in web browser
for i in range(number):
    urlToOpen = 'https://pypi.org/' + selectPacgage[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)

