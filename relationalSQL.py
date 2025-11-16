# import sqlite3

# # Koneksi ke database
# conn = sqlite3.connect('sekolah_relasional.db')
# cursor = conn.cursor()

# # Tabel KELAS (parent/induk)
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS kelas (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     nama_kelas TEXT NOT NULL UNIQUE,
#     wali_kelas TEXT,
#     kapasitas INTEGER DEFAULT 30
# )
# """)

# # Tabel SISWA (child/anak)
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS siswa (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     nama TEXT NOT NULL,
#     kelas_id INTEGER,
#     nilai_rata_rata REAL,
#     tanggal_masuk DATE DEFAULT CURRENT_DATE,
#     FOREIGN KEY (kelas_id) REFERENCES kelas(id)
#         ON DELETE SET NULL
#         ON UPDATE CASCADE
# )
# """)

# conn.commit()
# print("✅ Tabel berhasil dibuat!")

# conn.close()

# import sqlite3

# conn = sqlite3.connect('sekolah_relasional.db')
# cursor = conn.cursor()

# # Data kelas
# data_kelas = [
#     ('XI-A', 'Pak Budi', 30),
#     ('XI-B', 'Bu Ani', 30),
#     ('XI-C', 'Pak Rudi', 28)
# ]

# cursor.executemany("""
# INSERT INTO kelas (nama_kelas, wali_kelas, kapasitas)
# VALUES (?, ?, ?)
# """, data_kelas)

# conn.commit()
# print(f"✅ {cursor.rowcount} kelas berhasil ditambahkan!")

# conn.close()

# import sqlite3

# conn = sqlite3.connect('sekolah_relasional.db')
# cursor = conn.cursor()

# # Data siswa dengan kelas_id yang valid
# data_siswa = [
#     ('Ali Rahman', 1, 85.5),      # kelas_id = 1 (XI-A)
#     ('Budi Santoso', 1, 78.0),    # kelas_id = 1 (XI-A)
#     ('Citra Dewi', 2, 92.5),      # kelas_id = 2 (XI-B)
#     ('Dina Maharani', 2, 88.0),   # kelas_id = 2 (XI-B)
#     ('Eko Prasetyo', 3, 75.5),    # kelas_id = 3 (XI-C)
#     ('Fitri Handayani', 3, 90.0)  # kelas_id = 3 (XI-C)
# ]

# cursor.executemany("""
# INSERT INTO siswa (nama, kelas_id, nilai_rata_rata)
# VALUES (?, ?, ?)
# """, data_siswa)

# conn.commit()
# print(f"✅ {cursor.rowcount} siswa berhasil ditambahkan!")

# conn.close()

# import sqlite3

# conn = sqlite3.connect('sekolah_relasional.db')
# cursor = conn.cursor()

# # Query dengan INNER JOIN
# query = """
# SELECT 
#     siswa.id,
#     siswa.nama,
#     kelas.nama_kelas,
#     kelas.wali_kelas,
#     siswa.nilai_rata_rata
# FROM siswa
# INNER JOIN kelas ON siswa.kelas_id = kelas.id
# ORDER BY kelas.nama_kelas, siswa.nama
# """

# cursor.execute(query)
# results = cursor.fetchall()

# print("📋 DAFTAR SISWA DAN KELASNYA")
# print("="*70)
# print(f"{'ID':<5} {'Nama':<20} {'Kelas':<8} {'Wali Kelas':<15} {'Nilai':<6}")
# print("-"*70)

# for row in results:
#     print(f"{row[0]:<5} {row[1]:<20} {row[2]:<8} {row[3]:<15} {row[4]:<6}")

# conn.close()

# import sqlite3

# conn = sqlite3.connect('sekolah_relasional.db')
# cursor = conn.cursor()

# # Query dengan LEFT JOIN
# query = """
# SELECT 
#     kelas.nama_kelas,
#     kelas.wali_kelas,
#     COUNT(siswa.id) as jumlah_siswa,
#     kelas.kapasitas,
#     (kelas.kapasitas - COUNT(siswa.id)) as sisa_kursi
# FROM kelas
# LEFT JOIN siswa ON kelas.id = siswa.kelas_id
# GROUP BY kelas.id
# ORDER BY kelas.nama_kelas
# """

# cursor.execute(query)
# results = cursor.fetchall()

# print("📊 STATISTIK KELAS")
# print("="*70)
# print(f"{'Kelas':<8} {'Wali Kelas':<15} {'Siswa':<8} {'Kapasitas':<12} {'Sisa':<6}")
# print("-"*70)

# for row in results:
#     print(f"{row[0]:<8} {row[1]:<15} {row[2]:<8} {row[3]:<12} {row[4]:<6}")

# conn.close()

import sqlite3

conn = sqlite3.connect('sekolah_relasional.db')
cursor = conn.cursor()

query = """
SELECT 
    kelas.nama_kelas,
    siswa.nama,
    siswa.nilai_rata_rata
FROM siswa
INNER JOIN kelas ON siswa.kelas_id = kelas.id
WHERE siswa.nilai_rata_rata = (
    SELECT MAX(s2.nilai_rata_rata)
    FROM siswa s2
    WHERE s2.kelas_id = siswa.kelas_id
)
ORDER BY kelas.nama_kelas
"""

cursor.execute(query)
results = cursor.fetchall()

print("🏆 SISWA TERBAIK PER KELAS")
print("="*50)
print(f"{'Kelas':<10} {'Nama':<25} {'Nilai':<8}")
print("-"*50)

for row in results:
    print(f"{row[0]:<10} {row[1]:<25} {row[2]:<8}")

conn.close()

# import sqlite3

# conn = sqlite3.connect('sekolah_relasional.db')
# cursor = conn.cursor()

# query = """
# SELECT 
#     kelas.nama_kelas,
#     kelas.wali_kelas,
#     COUNT(siswa.id) as jumlah_siswa,
#     ROUND(AVG(siswa.nilai_rata_rata), 2) as rata_rata_nilai,
#     MAX(siswa.nilai_rata_rata) as nilai_tertinggi,
#     MIN(siswa.nilai_rata_rata) as nilai_terendah
# FROM kelas
# INNER JOIN siswa ON kelas.id = siswa.kelas_id
# GROUP BY kelas.id
# ORDER BY rata_rata_nilai DESC
# """

# cursor.execute(query)
# results = cursor.fetchall()

# print("📊 PERFORMA KELAS")
# print("="*90)
# print(f"{'Kelas':<8} {'Wali':<12} {'Siswa':<8} {'Rata²':<8} {'Max':<8} {'Min':<8}")
# print("-"*90)

# for row in results:
#     print(f"{row[0]:<8} {row[1]:<12} {row[2]:<8} {row[3]:<8} {row[4]:<8} {row[5]:<8}")

# conn.close()
