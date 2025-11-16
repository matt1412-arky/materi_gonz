import sqlite3

conn = sqlite3.connect('sekolah.db')
cursor = conn.cursor()

# Membuat tabel siswa
sql_insert = '''
INSERT INTO siswa (nama, kelas, nilai_matematika, nilai_fisika, tanggal_lahir) 
VALUES (?,?,?,?,?)
'''
# data = ("Ali Rahmat", "XI-A", 85, 80, "2008-05-15")
data_siswa = [
    ("Budi Santoso", "XI-B", 90, 88, "2008-08-20"),
    ("Citra Dewi", "XI-A", 78, 82, "2008-12-05"),
    ("Dewi Anggraeni", "XI-C", 92, 95, "2008-03-30"),
    ("Eko Prasetyo", "XI-B", 65, 70, "2008-07-22")
]
# cursor.execute(sql_insert, data)
cursor.executemany(sql_insert, data_siswa)
conn.commit()

# print(f"Data {data[0]} berhasil ditambahkan!")
# print(f"ID: {cursor.lastrowid}")

print(f"{cursor.rowcount} data siswa berhasil ditambahkan!")
conn.close()

