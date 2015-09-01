import random
import re
from bs4 import BeautifulSoup
import requests

b = BeautifulSoup(requests.get('http://www.theonion.com/features/horoscope').text, 'html.parser')
astro = random.choice(b.findAll("li", {"class": "astro-aries"}))
print(re.sub(u"(\u2018|\u2019|\u201c)", "'",astro.find('div', {'class': 'large-thing'}).get_text()))
#print(astro)