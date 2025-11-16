import random

angka_rahasia = random.randint(1, 100)  # Angka acak antara 1 sampai 100
tebakan = 0

while tebakan != angka_rahasia:
    tebakan = int(input("Tebak angka antara 1 dan 100: "))
    if tebakan < angka_rahasia:
        print("Terlalu rendah!")
    elif tebakan > angka_rahasia:
        print("Terlalu tinggi!")

print("Selamat! Anda berhasil menebak angka:", angka_rahasia)

