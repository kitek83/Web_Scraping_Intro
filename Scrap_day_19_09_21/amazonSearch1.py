import bs4, webbrowser,requests

query = input('Type searched product in amazon.pl: ')

for num in range(1,43):

    res = requests.get('https://helion.pl/search?szukaj=' + query + f'&nrs={num}')
soup = bs4.BeautifulSoup(res.text, 'html.parser')

selectElement = soup.select('.short-title')
print(len(selectElement))
print('---------------------')
print(selectElement)