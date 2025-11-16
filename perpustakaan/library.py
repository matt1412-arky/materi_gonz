class Book:
    def __init__(self, judul, penulis, tahun):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun

    def __str__(self):
        return f"{self.judul} - {self.penulis} ({self.tahun})"


class Library:
    def __init__(self):
        self.daftar_buku = []

    def tambah_buku(self, judul, penulis, tahun):
        try:
            tahun = int(tahun)  # Validasi input tahun
            buku = Book(judul, penulis, tahun)
            self.daftar_buku.append(buku)
            print("✅ Buku berhasil ditambahkan!")
        except ValueError:
            print("❌ Tahun harus berupa angka!")

    def lihat_buku(self):
        if not self.daftar_buku:
            print("Belum ada buku di perpustakaan.")
        else:
            print("\n=== Daftar Buku ===")
            for i, buku in enumerate(self.daftar_buku, start=1):
                print(f"{i}. {buku}")

    def cari_buku(self, judul):
        for buku in self.daftar_buku:
            if buku.judul.lower() == judul.lower():
                print(f"✅ Buku ditemukan: {buku}")
                return
        print("❌ Buku tidak ditemukan.")
