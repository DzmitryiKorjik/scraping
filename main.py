from os import write
from pprint import pprint

import requests
from bs4 import BeautifulSoup
from unicodedata import category

url = "https://books.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
#print(soup.prettify())

#aside = soup.find('div', class_="side_categories")
#categories = aside.find('ul').find('li').find('ul')
#with open('liens.html', 'w', encoding='utf-8') as file:  # Ouvrir le fichier UNE SEULE FOIS
#    for category in categories.children:
#        if category.name == 'li':
#            href = category.a['href'].strip('/')
#            text = category.a.text.strip()
#            file.write(f"{text}: {href}\n")  # Écriture formatée dans le fichier
#
#print("Les liens ont été enregistrés dans 'liens.html' avec succès !")


#image = soup.find('section').find_all('img')
#with open('images.html', 'w', encoding='utf-8') as file:
#    for img in image:
#        src = img['src'].strip('/')
#        alt = img['alt'].strip()
#        file.write(f"<img src='{src}' alt='{alt}'/>\n")

#with open('index.html', 'r') as file:
#    html = file.read()
#soup = BeautifulSoup(html, 'html.parser')
#images = soup.find('section').find_all('img')
#for image in images:
#    print(image.get('src'))


articles = soup.find_all('article', class_='product_pod')
with open('titre.html', 'w', encoding='utf-8') as file:
    for article in articles:
        titre = article.find('h3').find('a')
        file.write(f"{titre.text.strip()}\n")





