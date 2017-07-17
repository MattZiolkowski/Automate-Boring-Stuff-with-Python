#! python3
# ImgurPhotoDownload.py aims to download all the searched pictures displayed on Imgur.com

import requests, bs4, os


# Insert searched phrase into imgur search engine.

searchInput = str(input('Search and dowload Imgur content:'))
url= r'http://imgur.com/search/score?q=' + searchInput

# Parse search result page to get src of each photo to download.

res = requests.get(url)

res.raise_for_status()  # Check if download went OK.

soup = bs4.BeautifulSoup(res.text, "html.parser")

type(soup)

elemImg = soup.select('a > img')

print(elemImg)       # Prints img tags to find src tag
print('Downloading '+ str(len(elemImg)) + ' elements') # Prints amount of jpg. to download


# Create and download each jpg file on computer.
counter = 1
for i in range(len(elemImg)):
    source = str(r'http:'+(elemImg[i].get('src')))
    print('Saving ' + source + ' into ' + os.getcwd())
    JPG = requests.get(source)
    picfile = open(str(searchInput+str(counter)+'.jpg'), 'wb')
    for chunk in JPG.iter_content(100000):
         picfile.write(chunk)
    counter += 1
    picfile.close()
print('Done.')






