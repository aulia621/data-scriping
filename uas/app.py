#flask
from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/detik-populer")
def detik_populer():
    url = "https://www.detik.com/jatim/berita/indeks"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    area = soup.find("div", class_="grid-row list-content")
    items = area.find_all("article")

    data = []

    for item in items:
        img = item.find("img")
        link_tag = item.find("a")
        tanggal = item.find("div", class_="media__date")

        data.append({
            "judul": img["title"] if img and img.has_attr("title") else "",
            "url": link_tag["href"] if link_tag else "#",
            "tanggal": tanggal.text.strip() if tanggal else "",
            "gambar": img["src"] if img and img.has_attr("src") else ""
        })

    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)