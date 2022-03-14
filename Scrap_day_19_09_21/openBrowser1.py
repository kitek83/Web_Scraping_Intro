import bs4, requests, webbrowser
#Program opens first 5 links after search query ar https://pypi.org

query = input("Enter what are you looking for at pypi.org: ")
res = requests.get('https://pypi.org/search/?q=' + query)

#creating beautiful soup object to find all links
soup = bs4.BeautifulSoup(res.text,'html.parser')
element = soup.select('.package-snippet')
print(len(element))
print('--------------------------')

numOpen = min(5, len(element))
count = 0
for i in range(numOpen):
    count += 1
    urlToOpen = 'https://pypi.org' + element[i].get('href')
    print(f'Opening url{count}: ' + urlToOpen)
    webbrowser.open(urlToOpen)
