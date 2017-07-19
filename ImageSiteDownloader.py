#! python3
# ImgurPhotoDownload.py aims to download all the searched pictures displayed on Imgur.com.
# Program does the bulk of the task. Still needs some polishing.
# At the moment it downloads only minature of the images.

import requests, bs4, os

# Insert searched phrase into imgur search engine.

searchInput = input(str('Search and download all Imgur images: '))
url= r'http://imgur.com/search/score?q=' + searchInput

# Parse search result page to get src of each photo to download.

res = requests.get(url)
res.raise_for_status()  # Check if download went OK.
soup = bs4.BeautifulSoup(res.text, 'html.parser') # Creates soup object.

# Search for image html tag.
elemImg = soup.select('a > img')

# Display notification if no images found. 
while True:
    if len(elemImg) == 0:
        print('No results found.')
        break
    else:
        print('Downloading '+ str(len(elemImg)) + ' elements') # Prints a number of images found.
        break

# Choose directory for images to be saved
os.chdir(r'C:\Users\Place\Images\In\This\Folder')

# Download each jpg file on computer.
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
