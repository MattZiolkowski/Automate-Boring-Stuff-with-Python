#! python3
# lucky.py - Opens several Google search results. Need to creaete a .bat file and path.
# Start program by pressing WIN-R and "lucky <searched website>".
# Program will open in browser 5 top results in seperate tabs.

import requests, sys, webbrowser, bs4
print('Googling...') # display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()
# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, "html.parser")
# Open a browser tab for each result.
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
