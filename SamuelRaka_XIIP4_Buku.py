# Class untuk merepresentasikan data buku
class Buku:
    def __init__(self, judul, tahun):
        # Lengkapi bagian ini
        pass

    # method untuk menentukan kategori buku berdasarkan tahun
    def kategori_buku(self):
        # Lengkapi bagian ini
        pass

    # method untuk menampilkan data buku dalam format tabel
    def __str__(self):
        return f"{self.judul:<20} {self.tahun:<10} {self.kategori_buku():<20}"


# Class untuk menyimpan daftar koleksi buku
class KoleksiBuku:
    def __init__(self):
        self.daftar = []   # list kosong untuk menampung buku

    # method untuk menambahkan buku baru ke daftar
    def tambah_buku(self, buku):
        # Lengkapi bagian ini 
        pass

    # method untuk menampilkan tabel daftar semua buku
    def tampilkan_buku(self):
        print("=" * 60)
        print(f"{'Judul':<20} {'Tahun':<10} {'Kategori':<20}")
        print("=" * 60)
        for buku in self.daftar:
            # Lengkapi bagian ini
            pass
        print("=" * 60)
        print(f"Rata-rata tahun terbit buku: {self.rata_tahun():.2f}")
        print("=" * 60)

    # method untuk menghitung rata-rata tahun terbit
    def rata_tahun(self):
        if len(self.daftar) == 0:
            return 0
        total = sum([buku.tahun for buku in self.daftar if buku.tahun > 0])
        return total / len(self.daftar)


# MAIN PROGRAM
if __name__ == "__main__":
    koleksi = KoleksiBuku()

    print("=== Input Data Buku (5 buku) ===")
    for i in range(1, 6):
        print(f"\nBuku ke-{i}:")
        judul = input("Masukkan judul buku: ")
        tahun = int(input("Masukkan tahun terbit: "))
        # Lengkapi bagian ini
        pass

    # Tampilkan hasil daftar buku
    print("\n=== Daftar Koleksi Buku ===")
    # Lengkapi bagian ini
    pass
