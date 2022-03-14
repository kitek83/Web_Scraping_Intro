import bs4

fileExample = open('htmlExample.html')
soupExample = bs4.BeautifulSoup(fileExample.read(),'html.parser')
pEle = soupExample.select('p')
print(pEle)
print(len(pEle))
print(pEle[0].getText())
print(pEle[1].getText())
print(pEle[2].getText())
