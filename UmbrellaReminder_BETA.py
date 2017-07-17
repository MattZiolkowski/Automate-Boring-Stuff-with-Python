#! python3
# umbrellaReminder.py - checks the weather status in your city and sends reminder about umbrella if its about to rain.

import requests
import bs4

city = 'wroclaw'
url = str(r'https://www.meteoprog.pl/pl/weather/' + city)
print(url)
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')

elem = soup.find('div', class_="infoPrognosis widthProg")
elem = elem.get_text()
pogoda = elem.strip()
print(pogoda)

# TODO: check weather at certain hour automatically

# TODO: check if its going to rain

# TODO: send weather sms to the phone