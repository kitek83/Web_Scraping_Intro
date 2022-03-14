import requests, webbrowser, bs4

search = input('Enter the word you are looking for:')
page = requests.get('https://www.amazon.pl/s?k=' + search)

soup = bs4.BeautifulSoup(page.text, 'html.parser')
soupSelect = soup.select('a-link-normal a-text-normal')
print(soup)
#number = min(10,len(soupSelect))


