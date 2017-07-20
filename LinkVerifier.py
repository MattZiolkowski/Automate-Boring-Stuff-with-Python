#! python3

'''
Program follows all links from a given url page, follows these links and downloads their content.
If the link doesn't exists, program displays a notification.

At the moment program handles main errors (e.g. 404, 401).
But program crashes if link doesn't start with 'http|s:' or if the url of the function is invalid.
'''

import requests, bs4

def linkVerif(url):

    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elem = soup.select('a')
    print(elem)

    for i in range(len(elem)):
        link = elem[i].get('href')
        print(link)
        page = requests.get(link)
        try:
            page.raise_for_status()
        except Exception as exc:
            print('There was a problem: ' + str(exc))

linkVerif(r'http://www.rochesterteachers.com/rochester_teachers_association/Useful_Links.html') # Could be replaced by LinkVerif(input())



