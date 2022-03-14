import bs4

fileExample = open('htmlExample.html')
exampleSoup = bs4.BeautifulSoup(fileExample.read(),'html.parser')
sele = exampleSoup.select('#author')
print(type(sele))
print(sele)
print(len(sele))
print(sele[0].getText())
print(sele[0].attrs)