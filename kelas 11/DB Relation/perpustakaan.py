import sqlite3

conn = sqlite3.connect("C:\\Users\\Lenovo\\OneDrive\\Documents\\materi_gonz\\kelas 11\\DB Relation\\DB\\perpustakaan.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS kategori (
    id_kategori INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_kategori TEXT NOT NULL UNIQUE,
    deskripsi TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS penulis (
    id_penulis INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_penulis TEXT NOT NULL UNIQUE,
    negara TEXT        
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS buku (
    id_buku INTEGER PRIMARY KEY AUTOINCREMENT,
    judul TEXT UNIQUE,
    harga FLOAT,
    rating TEXT,
    id_kategori INTEGER,
    id_penulis INTEGER,
    FOREIGN KEY (id_kategori) REFERENCES kategori(id_kategori),
    FOREIGN KEY (id_penulis) REFERENCES penulis(id_penulis)
)
""")  

print("✅ Tabel kategori, penulis, dan buku berhasil dibuat!")

sql_insert_kategori = '''
INSERT OR IGNORE INTO kategori (nama_kategori, deskripsi) VALUES (?,?)
'''

data_kategori = [
    ("Fiksi", "Buku yang berisi cerita imajinatif dan tidak nyata."),
    ("Non-Fiksi", "Buku yang berisi informasi faktual dan nyata."),
    ("Sains", "Buku yang membahas ilmu pengetahuan dan teknologi."),
    ("Sejarah", "Buku yang mengulas peristiwa masa lalu dan perkembangan sejarah.")
]

cursor.executemany(sql_insert_kategori, data_kategori)

print("✅ Data kategori berhasil dimasukkan!")

sql_insert_penulis = '''
INSERT OR IGNORE INTO penulis (nama_penulis, negara) VALUES (?,?)
'''

data_penulis = [
    ("J.K. Rowling", "Inggris"),
    ("Harper Lee", "Amerika Serikat"),
    ("Stephen King", "Amerika Serikat"),
    ("Agatha Christie", "Inggris")
]

cursor.executemany(sql_insert_penulis, data_penulis)

print("✅ Data penulis berhasil dimasukkan!")

sql_insert_buku = '''
INSERT OR IGNORE INTO buku (judul, harga, rating, id_kategori, id_penulis) VALUES (?,?,?,?,?)
'''

data_buku = [
    ("Harry Potter and the Sorcerer's Stone", "100000", "4.8", 1, 1),
    ("To Kill a Mockingbird", "80000", "4.9", 1, 2),
    ("The Shining", "90000", "4.7", 1, 3),
    ("Murder on the Orient Express", "85000", "4.6", 1, 4),
    ("Buku Tanpa Penulis", "50000", "3.5", 2, None), 
    ("Buku Misterius", "60000", "4.0", 3, None), 
]

cursor.executemany(sql_insert_buku, data_buku)

print("✅ Data buku berhasil dimasukkan!")

cursor.execute("""
    SELECT b.judul, b.harga, k.nama_kategori, p.nama_penulis 
    FROM buku b
    INNER JOIN kategori k ON b.id_kategori = k.id_kategori
    INNER JOIN penulis p ON b.id_penulis = p.id_penulis 
    ORDER BY b.harga DESC              
""")

for judul, harga, kat, penulis in cursor.fetchall():
    print(f"{judul:<40} Rp.{harga:,.0f} {kat:<10} {penulis}")

conn.commit()
conn.close()
