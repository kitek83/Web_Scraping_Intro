import bs4, requests, os

#os.mkdir('xkcd')
url = 'https://xkcd.com'

while not url.endswith('#'):
    print('Downloading page %s...' % url)
    res = requests.get(url)
    print(res)
    print(res.status_code == requests.codes.ok)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    #finding image in soupr, bs4 object
    findImage = soup.select('#comic img')
    print(findImage)
    if findImage == []:
        print('Image couldn\'t be found!')
    else:
        comicUrl = 'https:' + findImage[0].get('src')
        print(comicUrl)
        #Downloading the img file
        print('Downloading the image: %s' % comicUrl)
        res = requests.get(comicUrl)
        #creating the file in xkcd folder
        imageFile = open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb')
        #downloading the chanks of data to the imageFile
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    # Get the prev button's url
    prevLink = soup.select('a[rel="prev"]')[0]
    print('----------------')
    print(prevLink)
    url = 'https://xkcd.com' + prevLink.get('href')

