from bs4 import BeautifulSoup
import os
import fungsi
import requests

def main_scraper(url, directory):
    fungsi.create_directory(directory)
    output_file_path = os.path.join(directory, "artikel.doc")
    if fungsi.does_file_exist(output_file_path):
        os.remove(output_file_path)
        
    print(f"Memproses artikel tunggal: {url}")
    get_details(url, directory)
    print("-----------------------------------------------------")
    print(f" Scraping Selesai. Hasil disimpan di: {output_file_path}")


def get_details(url, directory):
    try:
        source_code = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(f"Gagal mengambil URL: {e}")
        return

    soup = BeautifulSoup(source_code.text, "html.parser")
    
    title_tag = soup.find("h1", {"class": "read__title"})
    article_title = title_tag.text if title_tag else "JUDUL TIDAK DITEMUKAN"
    divEntry = soup.find("div", {"class": "read__content"}) 
    
    if not divEntry:
        print("Gagal menemukan div konten (class: read__content).")
        return

    paragraphs = divEntry.find_all("p")
    output_path = os.path.join(directory, "artikel.doc")
    
    fungsi.write_to_file(output_path, "=====================================================")
    fungsi.write_to_file(output_path, f"JUDUL: ***{article_title}***")
    fungsi.write_to_file(output_path, f"URL : {url}\n")
    fungsi.write_to_file(output_path, "Paragraf Konten : ")

    for p in paragraphs:
        text = p.text.strip()
        if len(text):
            fungsi.write_to_file(output_path, text)
            
    print("-----------------------------------------------------")
    fungsi.write_to_file(output_path, "=====================================================\n")

url_artikel = "https://www.kompas.com/sains/read/2025/10/30/080100223/foto-langka-dari-langit--komet-lemmon-tampak-terlilit-meteor?source=sorotan"
main_scraper(url_artikel, "Berita sekarang")