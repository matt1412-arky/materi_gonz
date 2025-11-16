import sqlite3

conn = sqlite3.connect('sekolah.db')
cursor = conn.cursor()

# Hapus siswa dengan ID tertentu
sql_delete = "DELETE FROM siswa WHERE id = ?"

# ID yang akan dihapus
id_siswa = 5

cursor.execute(sql_delete, (id_siswa,))
conn.commit()

if cursor.rowcount > 0:
    print(f"✅ Siswa dengan ID {id_siswa} berhasil dihapus!")
else:
    print(f"❌ Siswa dengan ID {id_siswa} tidak ditemukan")

conn.close()
