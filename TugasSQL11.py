import sqlite3

# Koneksi ke database (akan otomatis membuat file peminjaman.db jika belum ada)
conn = sqlite3.connect('peminjaman.db')
cursor = conn.cursor()

# Membuat tabel peminjaman
cursor.execute('''
CREATE TABLE IF NOT EXISTS peminjaman (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama TEXT NOT NULL,
    judul_buku TEXT NOT NULL,
    tanggal_pinjam DATE NOT NULL,
    tanggal_kembali DATE NOT NULL
)
''')
print("✅ Tabel peminjaman berhasil dibuat!\n")

# Menambahkan data awal
data_peminjaman = [
    ("Ali", "Laskar Pelangi", "2025-10-09", "2025-10-15"),
    ("Budi", "Negeri 5 Menara", "2025-10-10", "2025-10-17"),
    ("Citra", "Sang Pemimpi", "2025-10-11", "2025-10-18")
]

cursor.executemany('''
INSERT INTO peminjaman (nama, judul_buku, tanggal_pinjam, tanggal_kembali)
VALUES (?, ?, ?, ?)
''', data_peminjaman)
conn.commit()
print("✅ Data berhasil ditambahkan!")

# Menampilkan data awal
cursor.execute("SELECT * FROM peminjaman")
rows = cursor.fetchall()
for row in rows:
    print(f"{row[0]}. {row[1]} - \"{row[2]}\" ({row[3]} s/d {row[4]})")

# Update data (ubah buku milik Budi)
cursor.execute('''
UPDATE peminjaman
SET judul_buku = "Bumi Manusia"
WHERE nama = "Budi"
''')
conn.commit()

print("\n📘 Setelah update:")
cursor.execute("SELECT nama, judul_buku FROM peminjaman")
# cursor.execute("SELECT * FROM peminjaman")
rows = cursor.fetchall()
# print("📋 DAFTAR PEMINJAMAN")
# print("="*70)
# print(f"{'ID':<5} {'Nama':<20} {'Judul Buku':<30} {'Tanggal Pinjam':<15} {'Tanggal Kembali':<15}")
# print("-"*70)

# for row in rows:
#     print(f"{row[0]:<5} {row[1]:<20} {row[2]:<30} {row[3]:<15} {row[4]:<15}")

for i, row in enumerate(rows, start=1):
    print(f"{i}. {row[0]} - \"{row[1]}\"")

# Delete data (hapus data milik Budi)
cursor.execute('''
DELETE FROM peminjaman
WHERE nama = "Budi"
''')
conn.commit()

print("\n🗑️ Setelah delete:")
cursor.execute("SELECT nama, judul_buku FROM peminjaman")
rows = cursor.fetchall()
for i, row in enumerate(rows, start=1):
    print(f"{i}. {row[0]} - \"{row[1]}\"")

# Tutup koneksi
conn.close()
