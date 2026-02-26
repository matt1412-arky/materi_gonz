import requests
from bs4 import BeautifulSoup
import csv

def simpan_ke_csv(nama_file="data_buku.csv"):
    url = "https://books.toscrape.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    buku_list = soup.find_all("article", class_="product_pod")

    # Tulis ke file CSV
    with open(nama_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["No", "Judul", "Harga", "Rating"])

        for i, buku in enumerate(buku_list, 1):
            judul = buku.find("h3").find("a")["title"]
            harga = buku.find("p", class_="price_color").text
            rating = buku.find("p", class_="star-rating")["class"][1]
            writer.writerow([i, judul, harga, rating])

    print(f"✅ Data disimpan ke {nama_file}")

simpan_ke_csv()
