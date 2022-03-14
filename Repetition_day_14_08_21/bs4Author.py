#reading attributes: author from the bs4 object
import bs4

newFile = open('htmlExample.html')
soupObject = bs4.BeautifulSoup(newFile.read(), 'html.parser')
soupSelect = soupObject.select('#author')
print(soupSelect)
print(len(soupSelect))
print(soupSelect[0])
print()
print(soupSelect[0].getText())
print(soupSelect[0].attrs)

