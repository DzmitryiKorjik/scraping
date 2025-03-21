# Scraping de Books to Scrape

Un projet de scraping web pour extraire des données du site "Books to Scrape" (https://books.toscrape.com/).

## Description
Ce script Python permet d'extraire différentes informations du site "Books to Scrape", notamment :
- Les catégories de livres
- Les images des livres
- Les titres des livres

## Fonctionnalités
- Extraction des catégories avec leurs liens
- Récupération des images et leurs attributs alt
- Extraction des titres de livres

## Prérequis
- Python 3.x
- BeautifulSoup4
- Requests

## Installation
```bash
  pip install beautifulsoup4
  pip install requests
```

## Utilisation

Exécutez le script principal :

```bash
  python main.py
```

## Structure des fichiers

```
SCRAPING
├── README.md
├── main.py
├── pages
│   ├── images.html
│   ├── index.html
│   ├── liens.html
│   └── titre.html
├── pyproject.toml
└── requirements.txt

```
