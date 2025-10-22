from bs4 import BeautifulSoup
import requests

def main_scrapper(url_directory):
    # ambil halaman dari URL target
    response = requests.get(url_directory, headers={"User-Agent": "Mozilla/5.0"})
    if response.status_code != 200:
        print(f"❌ Gagal mengakses {url_directory} (status {response.status_code})")
        return

    # parsing HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # cari semua elemen artikel
    articles = soup.find_all("a", class_="article__link")

    if not articles:
        print("❌ Tidak menemukan artikel. Struktur HTML mungkin berubah.")
        return

    # ambil hanya satu artikel pertama
    first_article = articles[0]
    href = first_article.get("href")
    title = first_article.get_text(strip=True)

    # tampilkan hasil
    print("✅ Artikel Pertama Ditemukan:")
    print(f"Judul: {title}")
    print(f"URL  : {href}")

# jalankan
main_scrapper("https://tekno.kompas.com/gadget")
