# Program Kategori Suhu

# Input suhu dari user
suhu = float(input("Masukkan suhu (°C): "))

# Cek kategori suhu menggunakan if dan operator logika
if suhu < 0:
    print("Beku ❄️")
elif suhu >= 0 and suhu <= 15:
    print("Dingin 🥶")
elif suhu >= 16 and suhu <= 25:
    print("Sejuk 😊")
elif suhu >= 26 and suhu <= 35:
    print("Hangat ☀️")
elif suhu > 35:
    print("Panas 🔥")
