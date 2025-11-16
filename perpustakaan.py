import sqlite3

# Koneksi ke database
conn = sqlite3.connect("perpustakaan.db")
cur = conn.cursor()

# Buat tabel jika belum ada
def buat_tabel():
    cur.execute("""
    CREATE TABLE IF NOT EXISTS buku (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        judul TEXT NOT NULL,
        penulis TEXT,
        tahun INTEGER
    )
    """)
    conn.commit()

# Tambah data buku
def tambah_buku():
    judul = input("Judul buku: ").strip()
    if judul == "":
        print("Judul tidak boleh kosong!")
        return
    
    penulis = input("Penulis: ").strip()
    tahun_input = input("Tahun terbit (boleh kosong): ").strip()

    if tahun_input:
        if not tahun_input.isdigit():
            print("Tahun harus berupa angka!")
            return
        tahun = int(tahun_input)
    else:
        tahun = None

    cur.execute("INSERT INTO buku (judul, penulis, tahun) VALUES (?, ?, ?)",
                (judul, penulis, tahun))
    conn.commit()
    print("📚 Data buku berhasil ditambahkan!")

# Tampilkan semua buku
def lihat_semua():
    cur.execute("SELECT * FROM buku")
    data = cur.fetchall()
    if not data:
        print("Belum ada data buku.")
        return
    
    print("\n📖 DAFTAR BUKU:")
    print("{:<5} {:<30} {:<20} {:<6}".format("ID", "Judul", "Penulis", "Tahun"))
    print("-" * 65)
    for b in data:
        print("{:<5} {:<30} {:<20} {:<6}".format(b[0], b[1], b[2] or "-", b[3] or "-"))
    print()

# Ubah data buku
def ubah_buku():
    lihat_semua()
    try:
        id_buku = int(input("Masukkan ID buku yang ingin diubah: "))
    except ValueError:
        print("ID harus berupa angka!")
        return

    judul = input("Judul baru: ").strip()
    penulis = input("Penulis baru: ").strip()
    tahun_input = input("Tahun baru (boleh kosong): ").strip()

    if tahun_input:
        if not tahun_input.isdigit():
            print("Tahun harus angka!")
            return
        tahun = int(tahun_input)
    else:
        tahun = None

    cur.execute("UPDATE buku SET judul = ?, penulis = ?, tahun = ? WHERE id = ?",
                (judul, penulis, tahun, id_buku))
    conn.commit()
    print("✏️ Data buku berhasil diubah.")

# Hapus data buku
def hapus_buku():
    lihat_semua()
    try:
        id_buku = int(input("Masukkan ID buku yang ingin dihapus: "))
    except ValueError:
        print("ID harus berupa angka!")
        return

    cur.execute("DELETE FROM buku WHERE id = ?", (id_buku,))
    conn.commit()
    print("🗑️ Data buku berhasil dihapus.")

# Menu CLI
def menu():
    buat_tabel()
    while True:
        print("""
======= MENU PERPUSTAKAAN =======
1. Tambah Buku
2. Lihat Semua Buku
3. Ubah Buku
4. Hapus Buku
5. Keluar
""")
        pilihan = input("Pilih menu (1-5): ").strip()
        if pilihan == "1":
            tambah_buku()
        elif pilihan == "2":
            lihat_semua()
        elif pilihan == "3":
            ubah_buku()
        elif pilihan == "4":
            hapus_buku()
        elif pilihan == "5":
            print("👋 Program selesai. Sampai jumpa!")
            break
        else:
            print("❌ Pilihan tidak valid!")

    conn.close()

# Jalankan program
menu()