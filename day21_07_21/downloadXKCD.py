import os, requests, bs4

#starting url
url = 'https://xkcd.com'
#store comics in xkcd folder
#os.mkdir('xkcd')
while not url.endswith('#'):
    #Download the page
    print('Downloading page %s...' % url)
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text,'html.parser')
    #Find the url of the comic image
    comicElem = soup.select('#comic img')

    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')
    #Download image.
    print('Downloading image %s...' % (comicUrl))
    res = requests.get(comicUrl)
    print(res.raise_for_status())
    #save image to the ./xkcd
    imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

    #Get the 'prev' buttons url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')

