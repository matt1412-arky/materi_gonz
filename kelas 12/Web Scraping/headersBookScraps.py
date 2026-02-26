import requests

# Beberapa website blokir bot, kita pura-pura jadi browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0"
}

url = "https://books.toscrape.com"
response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("✅ Berhasil mengambil halaman!")
else:
    print(f"❌ Gagal, kode: {response.status_code}")
