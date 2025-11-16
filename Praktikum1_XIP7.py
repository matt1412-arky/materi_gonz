# 📝 Pengambilan nilai Praktikum 1 KELAS 11
# TOPIK: Struktur IF, Looping, dan Operator Logika
# Nama File: Nama_XIIP7_Praktikum1.py
# Contoh: Budi_XI1P7_Praktikum1.py

# ======================================================
# SOAL 1 (30 poin):
# Buatlah program untuk menampilkan daftar bilangan ganjil dari 1 sampai N,
# di mana N diinput oleh pengguna. Gunakan looping WHILE.
# ======================================================

N = int(input("Masukkan batas angka (N): "))
print("Bilangan ganjil dari 1 sampai", N, ":")
i = 1
while i <= N:
    if i % 2 != 0:
        print(i, end=" ")
    i += 1

print("\n" + "-" * 50)

# ======================================================
# SOAL 2 (35 poin):
# Buatlah program sederhana untuk menghitung diskon pembelian.
# Ketentuan diskon:
# - Jika total belanja ≥ 500000 → diskon 20%
# - Jika total belanja ≥ 250000 dan < 500000 → diskon 10%
# - Jika total belanja ≥ 100000 dan < 250000 → diskon 5%
# - Jika total belanja < 100000 → tidak ada diskon
# Program harus menampilkan: Total belanja, diskon yang didapat, dan total bayar.
# ======================================================

total_belanja = int(input("Masukkan total belanja: "))

if total_belanja >= 500000:
    diskon = 20
elif total_belanja >= 250000 and total_belanja < 500000:
    diskon = 10
elif total_belanja >= 100000 and total_belanja < 250000:
    diskon = 5
else:
    diskon = 0

total_diskon = total_belanja * diskon / 100
total_bayar = total_belanja - total_diskon

print("Diskon:", str(diskon) + "%")
print("Total bayar:", int(total_bayar))

print("-" * 50)

# ======================================================
# SOAL 3 (35 poin):
# Buatlah program untuk menampilkan deret bilangan Fibonacci sebanyak N suku,
# di mana N diinput oleh pengguna.
#
# 📌 Penjelasan Fibonacci:
# Deret Fibonacci adalah deret angka di mana:
# suku ke-1 = 0
# suku ke-2 = 1
# suku berikutnya = jumlah dua suku sebelumnya
#
# Contoh:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# (1 = 0+1, 2 = 1+1, 3 = 1+2, 5 = 2+3, dst.)
# ======================================================

n = int(input("Masukkan jumlah suku Fibonacci: "))
a, b = 0, 1
print("Hasil deret Fibonacci:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

# 📍 Contoh jika input n = 7
# Output: 0 1 1 2 3 5 8

print("\n" + "-" * 50)

# ======================================================
# ⭐ SOAL BONUS (20 poin – tidak masuk nilai 100 poin):
# Buatlah program login sederhana dengan ketentuan:
# Username: admin, Password: 12345
# - Jika benar → tampilkan "Selamat datang, Admin!"
# - Jika salah → tampilkan "Login gagal, coba lagi."
# - Hanya diberi kesempatan 3 kali, jika masih salah tampilkan "Akun terkunci."
# ======================================================

kesempatan = 3
while kesempatan > 0:
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    if username == "admin" and password == "12345":
        print("Selamat datang, Admin!")
        break
    else:
        kesempatan -= 1
        print("Login gagal, coba lagi. Sisa kesempatan:", kesempatan)

if kesempatan == 0:
    print("Akun terkunci.")

print("-" * 50)
