import requests
from bs4 import BeautifulSoup

def scrape_buku():
    """Ambil data buku dari halaman pertama"""
    url = "https://books.toscrape.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Cari semua artikel buku
    buku_list = soup.find_all("article", class_="product_pod")

    print(f"Ditemukan {len(buku_list)} buku\n")
    print(f"{'No':<4} {'Judul':<45} {'Harga'}")
    print("-" * 65)

    for i, buku in enumerate(buku_list, 1):
        # Ambil judul dari atribut 'title' pada tag <a>
        judul = buku.find("h3").find("a")["title"]

        # Ambil harga dari tag <p class="price_color">
        harga = buku.find("p", class_="price_color").text

        print(f"{i:<4} {judul[:44]:<45} {harga}")

# Jalankan program
scrape_buku()
