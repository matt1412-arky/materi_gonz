import sqlite3

conn = sqlite3.connect('sekolah.db')
cursor = conn.cursor()

# SQL untuk membaca semua data
sql_select = "SELECT * FROM siswa"

# Eksekusi dan ambil semua hasil
cursor.execute(sql_select)
results = cursor.fetchall()

# Tampilkan data
print("📋 DAFTAR SISWA")
print("="*70)
print(f"{'ID':<5} {'Nama':<20} {'Kelas':<8} {'Mat':<5} {'Fis':<5}")
print("-"*70)

for row in results:
    print(f"{row[0]:<5} {row[1]:<20} {row[2]:<8} {row[3]:<5} {row[4]:<5}")

conn.close()

# import sqlite3

# conn = sqlite3.connect('sekolah.db')
# cursor = conn.cursor()

# # Cari siswa dengan nilai fisika >= 85
# sql_select = """
# SELECT nama, kelas, nilai_fisika
# FROM siswa 
# WHERE nilai_fisika >= 85
# """

# cursor.execute(sql_select)
# results = cursor.fetchall()

# print("🌟 SISWA DENGAN NILAI FISIKA >= 85")
# print("-"*40)

# for row in results:
#     print(f"  {row[0]} ({row[1]}): {row[2]}")

# conn.close()

# import sqlite3

# conn = sqlite3.connect('sekolah.db')
# cursor = conn.cursor()

# # Urutkan berdasarkan nilai matematika (tertinggi ke terendah)
# sql_select = """
# SELECT nama, nilai_matematika, nilai_fisika
# FROM siswa
# ORDER BY nilai_matematika DESC
# """

# cursor.execute(sql_select)
# results = cursor.fetchall()

# print("🏆 RANKING NILAI MATEMATIKA")
# print("-"*50)

# rank = 1
# for row in results:
#     print(f"{rank}. {row[0]:<20} Mat: {row[1]:<3} Fis: {row[2]}")
#     rank += 1

# conn.close()
