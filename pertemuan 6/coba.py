import requests
from bs4 import BeautifulSoup
import os

# --- tambahan baru ---
url = 'https://tekno.kompas.com/gadget'
folder = 'hasil'

# pastikan folder ada
os.makedirs(folder, exist_ok=True)

# ambil halaman web
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

# ambil 3 berita pertama
items = soup.find_all('a', class_='article__link', limit=3)

# simpan ke file hasil/article.txt
with open(os.path.join(folder, 'article.txt'), 'w', encoding='utf-8') as f:
    for i, item in enumerate(items, start=1):
        f.write(f"{i}. {item.text.strip()}\n{item['href']}\n\n")

def read_data(path):
    with open(path, 'rt') as file:
        for line in file:
            print(line.strip())

read_data('hasil/article.txt')

