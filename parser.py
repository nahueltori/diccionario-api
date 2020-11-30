import json
import requests
from bs4 import BeautifulSoup

RAE_BASE = "https://dle.rae.es/"

palabra = input("Ingrese la palabra a buscar: ")
url = RAE_BASE + palabra
headers = {'Accept': 'application/ld+json'}

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, 'html.parser')
objeto = json.loads(soup.script.string)
DefinedTerm = objeto[2]
palabra = DefinedTerm["name"]
definicion = DefinedTerm["description"]
print("Definición para: " + palabra)
print(definicion)

