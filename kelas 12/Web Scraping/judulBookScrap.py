import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com"
# url = "https://learn.gonzaga.sch.id/"
response = requests.get(url)

# Buat objek soup untuk parsing HTML
soup = BeautifulSoup(response.text, "html.parser")

# Ambil judul halaman
print("Judul:", soup.title.text)
