from selenium import webdriver
from bs4 import BeautifulSoup
import fungsi
import requests
import os
import time

def main_scraper(url):

    driver = webdriver.Chrome()
    driver.set_page_load_timeout(5000)
    driver.get(url)

    time.sleep(3)

    # ambil DOM akhir BUKAN page_source
    html = driver.execute_script("return document.documentElement.outerHTML;")

    soup = BeautifulSoup(html, "html.parser")

    hasil = soup.find_all("div", class_="article__list")

    for item in hasil:
        Judul = item.find("a", class_="article__link")

        if Judul:
            print("Judul : ", Judul.text.strip())
            print("=====================================")

    fungsi.create_directory('hasil')
    file_path = os.path.join('hasil', 'kompasparser.txt')
    fungsi.write_to_file(file_path, html)

    driver.quit()


main_scraper("https://tekno.kompas.com/gadget")
