import bs4

exampleFile = open('htmlExample.html')  #file, which was downloaded earlier
exampleBS4 = bs4.BeautifulSoup(exampleFile,'html.parser')
print(type(exampleBS4))
print(exampleBS4)