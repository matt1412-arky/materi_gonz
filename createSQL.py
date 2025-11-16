import sqlite3

conn = sqlite3.connect('sekolah.db')
cursor = conn.cursor()

# Membuat tabel siswa
sql_create = '''
CREATE TABLE IF NOT EXISTS siswa (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama TEXT NOT NULL,
    kelas TEXT NOT NULL,
    nilai_matematika INTEGER,
    nilai_fisika INTEGER,
    tanggal_lahir DATE
)
'''
cursor.execute(sql_create)
print("Tabel 'siswa' berhasil dibuat.")

conn.commit()
conn.close()

