import requests

# Ambil halaman web
url = "https://books.toscrape.com"
response = requests.get(url)

# Cek status (200 = berhasil, 404 = tidak ditemukan)
print("Status:", response.status_code)
print("Panjang HTML:", len(response.text), "karakter")

# Tampilkan 500 karakter pertama HTML
print(response.text[:500])
