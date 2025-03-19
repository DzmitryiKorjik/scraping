from os import write

import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())

with open('index.html', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
