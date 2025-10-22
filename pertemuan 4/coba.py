import requests
import os 
from bs4 import BeautifulSoup

result= requests.get("https://www.detik.com/")
print(result)
print(result.encoding)
print(result.status_code)
print(result.elapsed)
print(result.url)
print(result.history)
print(result.headers['content-Type'])

def create_directory(folder_name):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

def main_scraper(url,directory):
    create_directory(directory)
    source_code = requests.get(url)
    source_text = source_code.text
    print(source_text)

main_scraper("https://www.detik.com/","Hasil")


def main_scraper(url,directory):
    create_directory(directory)
    source_code=requests.get(url)
    source_text=source_code.text
    soup=BeautifulSoup(source_text,"html.parser")
    print(soup.find_all("div",{'class':'list-content__item column-4 recommendation_firstrow'}))

main_scraper("https://www.detik.com/","hasil")