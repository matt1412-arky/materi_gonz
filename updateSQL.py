import sqlite3

conn = sqlite3.connect('sekolah.db')
cursor = conn.cursor()

# Update nilai Ali Rahman
sql_update = """
UPDATE siswa
SET nilai_matematika = ?, nilai_fisika = ?
WHERE nama = ?
"""

# Data baru
data = (90, 85, "Ali Rahmat")

cursor.execute(sql_update, data)
conn.commit()

print(f"✅ {cursor.rowcount} data berhasil diupdate!")

# Lihat hasil update
cursor.execute("SELECT * FROM siswa WHERE nama = 'Ali Rahmat'")
result = cursor.fetchone()
print(f"📊 Nilai baru Ali: Mat={result[3]}, Fis={result[4]}")

conn.close()
