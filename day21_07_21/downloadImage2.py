import requests, os, bs4

url = 'https://xkcd.com'
#os.mkdir('xkcd')

while not url.endswith('#'):
    print('Downloading the web page %s...' % url)
    print()
    res = requests.get(url)
    #making bs4 object
    soup = bs4.BeautifulSoup(res.text,'html.parser')
    #finding the img files
    imgFiles = soup.select('#comic img')
    print(imgFiles)
    if imgFiles == []:
        print('No image was found')
    else:
        comicUrl = 'https:' + imgFiles[0].get('src')
        print('---------------')
        print(comicUrl)
        print('Downloadng the img file: %s' % comicUrl)
        res = requests.get(comicUrl)
        #opening the file in xkcd folder to save img file
        imgFile = open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb')
        for chunk in res.iter_content(100000):
            imgFile.write(chunk)
    #Get the Prev button's url.
    print(2*'======================')
    prev = soup.select('a[rel="prev"]')[0]
    print(prev)
    print()
    url = 'https://xkcd.com' + prev.get('href')
    print('+++++++++++++++++++++++')
    print(url)
    print('++++++++++++++++++++++++++++++')


