import sqlite3

conn = sqlite3.connect("C:\\Users\\Lenovo\\OneDrive\\Documents\\materi_gonz\\kelas 11\\DB Relation\\DB\\buku_tag.db")
cursor = conn.cursor()

# ── BUAT TABEL ──────────────────────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS buku (
    id_buku   INTEGER PRIMARY KEY AUTOINCREMENT,
    judul     TEXT UNIQUE,
    harga     FLOAT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS tag (
    id_tag   INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_tag TEXT NOT NULL UNIQUE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS buku_tag (
    id_buku INTEGER,
    id_tag  INTEGER,
    PRIMARY KEY (id_buku, id_tag),
    FOREIGN KEY (id_buku) REFERENCES buku(id_buku),
    FOREIGN KEY (id_tag)  REFERENCES tag(id_tag)
)
""")

print("✅ Tabel buku, tag, dan buku_tag berhasil dibuat!")

# ── INSERT BUKU ─────────────────────────────────────────────
sql_insert_buku = "INSERT OR IGNORE INTO buku (judul, harga) VALUES (?, ?)"

data_buku = [
    ("Harry Potter and the Sorcerer's Stone", 100000),
    ("To Kill a Mockingbird",                  80000),
    ("The Shining",                            90000),
    ("Murder on the Orient Express",           85000),
    ("A Brief History of Time",                75000),
]

cursor.executemany(sql_insert_buku, data_buku)
print("✅ Data buku berhasil dimasukkan!")

# ── INSERT TAG ──────────────────────────────────────────────
sql_insert_tag = "INSERT OR IGNORE INTO tag (nama_tag) VALUES (?)"

data_tag = [
    ("Fiksi",),
    ("Misteri",),
    ("Horor",),
    ("Klasik",),
    ("Sains",),
    ("Petualangan",),
]

cursor.executemany(sql_insert_tag, data_tag)
print("✅ Data tag berhasil dimasukkan!")

# ── INSERT BUKU_TAG ─────────────────────────────────────────
# Ambil id_buku dan id_tag dulu biar aman
def get_id_buku(judul):
    cursor.execute("SELECT id_buku FROM buku WHERE judul = ?", (judul,))
    row = cursor.fetchone()
    return row[0] if row else None

def get_id_tag(nama):
    cursor.execute("SELECT id_tag FROM tag WHERE nama_tag = ?", (nama,))
    row = cursor.fetchone()
    return row[0] if row else None

relasi = [
    ("Harry Potter and the Sorcerer's Stone", "Fiksi"),
    ("Harry Potter and the Sorcerer's Stone", "Petualangan"),
    ("To Kill a Mockingbird",                 "Fiksi"),
    ("To Kill a Mockingbird",                 "Klasik"),
    ("The Shining",                           "Horor"),
    ("The Shining",                           "Fiksi"),
    ("Murder on the Orient Express",          "Misteri"),
    ("Murder on the Orient Express",          "Klasik"),
    ("A Brief History of Time",               "Sains"),
]

sql_insert_buku_tag = "INSERT OR IGNORE INTO buku_tag (id_buku, id_tag) VALUES (?, ?)"

data_buku_tag = [
    (get_id_buku(judul), get_id_tag(tag))
    for judul, tag in relasi
]

cursor.executemany(sql_insert_buku_tag, data_buku_tag)
print("✅ Data buku_tag berhasil dimasukkan!")

# ── QUERY GROUP_CONCAT ──────────────────────────────────────
print("\n📚 Daftar Buku beserta Tag-nya:")
print("-" * 65)

cursor.execute("""
    SELECT b.judul, b.harga, GROUP_CONCAT(t.nama_tag, ', ') AS tags
    FROM buku b
    JOIN buku_tag bt ON b.id_buku = bt.id_buku
    JOIN tag t       ON bt.id_tag = t.id_tag
    GROUP BY b.id_buku
    ORDER BY b.harga DESC
""")

for judul, harga, tags in cursor.fetchall():
    print(f"{judul:<42} Rp.{harga:>8,.0f}  [{tags}]")

conn.commit()
conn.close()