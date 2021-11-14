import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

url = 'https://selenagomez.fandom.com/wiki/Selena_Gomez'
pa = requests.get(url)
soup = bs(pa.text, "html.parser")
tags = []

for p in soup.find('div', {'class': "mw-parser-output"}).find_all('p')[:-1]:
    tags.append(p.text)
df = pd.DataFrame(tags)
df.to_csv('TomF.txt', sep='\t', encoding='utf-8')
url_pa = 'https://www.selenagomez.com/'
pa = requests.get(url_pa)
soup = bs(pa.text, "html.parser")
info=[]

for t in soup.find('div', {'class': "span12 sinopsis_text"}).find_all('p'):
    info.append(t.text)
df = pd.DataFrame(info)
df.to_csv('SelG.txt', sep='\t', encoding='utf-8')
print("Archivos con resultados, creados.")
