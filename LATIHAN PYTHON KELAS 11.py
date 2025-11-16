# 📝 LATIHAN PYTHON KELAS 11
# TOPIK: Struktur IF, Looping, dan Operator Logika
# Nama File: Nama_Kelas11_StrukturIFLooping.py
# Contoh: BudiXI1_StrukturIFLooping.py

# ======================================================
# SOAL 1:
# Buatlah program untuk menampilkan daftar bilangan genap dari 1 sampai N,
# di mana N diinput oleh pengguna. Gunakan looping FOR.
# ======================================================

N = int(input("Masukkan batas angka (N): "))
print("Bilangan genap dari 1 sampai", N, ":")
for i in range(1, N + 1):
    if i % 2 == 0:
        print(i, end=" ")

print("\n" + "-" * 50)

# ======================================================
# SOAL 2:
# Buatlah program yang meminta input nilai ujian dari pengguna.
# Jika nilai:
# >= 90 dan <= 100 → tampilkan "A"
# >= 75 dan < 90   → tampilkan "B"
# >= 60 dan < 75   → tampilkan "C"
# < 60             → tampilkan "D"
# Gunakan struktur IF dan operator logika.
# ======================================================

nilai = int(input("Masukkan nilai ujian: "))

if nilai >= 90 and nilai <= 100:
    print("Grade: A")
elif nilai >= 75 and nilai < 90:
    print("Grade: B")
elif nilai >= 60 and nilai < 75:
    print("Grade: C")
elif nilai < 60:
    print("Grade: D")
else:
    print("Nilai tidak valid (0-100)")

print("-" * 50)

# ======================================================
# SOAL 3:
# Buatlah program yang menampilkan "FizzBuzz":
# Jika angka habis dibagi 3 → tampilkan "Fizz"
# Jika angka habis dibagi 5 → tampilkan "Buzz"
# Jika angka habis dibagi 3 dan 5 → tampilkan "FizzBuzz"
# Jika tidak, tampilkan angkanya
# Lakukan untuk angka 1 sampai 50.
# ======================================================

print("Hasil FizzBuzz dari 1 sampai 50:")
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

print("-" * 50)
