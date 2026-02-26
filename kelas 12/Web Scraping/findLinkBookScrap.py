import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com"
# url = "https://learn.gonzaga.sch.id/"
response = requests.get(url)

# Buat objek soup untuk parsing HTML
soup = BeautifulSoup(response.text, "html.parser")

# find() → ambil 1 elemen pertama yang ditemukan
judul_pertama = soup.find("h1")
print(judul_pertama.text)

# find_all() → ambil SEMUA elemen yang cocok (hasilnya list)
semua_link = soup.find_all("a")
print(f"Total link: {len(semua_link)}")

# Cari berdasarkan class CSS
produk = soup.find_all("article", class_="product_pod")
print(f"Jumlah buku: {len(produk)}")

# Cari berdasarkan id
konten = soup.find("div", id="content")

# Ambil atribut (misal href dari link)
for link in semua_link[:5]:
    print(link.get("href"))
