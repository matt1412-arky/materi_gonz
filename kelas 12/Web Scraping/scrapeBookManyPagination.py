import requests
from bs4 import BeautifulSoup
import time

def scrape_semua_halaman(max_halaman=3):
    """Scraping beberapa halaman sekaligus"""
    semua_buku = []
    base_url = "https://books.toscrape.com/catalogue/page-{}.html"

    for halaman in range(1, max_halaman + 1):
        print(f"📥 Mengambil halaman {halaman}...")
        url = base_url.format(halaman)
        response = requests.get(url)

        if response.status_code != 200:
            print("Halaman tidak ditemukan, berhenti.")
            break

        soup = BeautifulSoup(response.text, "html.parser")
        buku_list = soup.find_all("article", class_="product_pod")

        for buku in buku_list:
            judul = buku.find("h3").find("a")["title"]
            harga = buku.find("p", class_="price_color").text
            semua_buku.append({"judul": judul, "harga": harga})

        # Jeda 1 detik agar tidak membebani server
        time.sleep(1)

    print(f"\n✅ Total buku terkumpul: {len(semua_buku)}")
    return semua_buku

data = scrape_semua_halaman(max_halaman=3)
