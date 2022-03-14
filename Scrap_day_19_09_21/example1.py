import bs4

fileExample = open('htmlExample.html')
soup = bs4.BeautifulSoup(fileExample.read(),'html.parser')
element = soup.select('#author')

print(element)
print(element[0])

print(element[0].getText())
print(element[0].attrs)