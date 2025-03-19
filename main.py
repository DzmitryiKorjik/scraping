import f
import requests

respons = requests.get("https://www.google.com/")

with open('index.html', 'w') as f:
    f.write(respons.text)