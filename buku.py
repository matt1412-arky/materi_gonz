# Class untuk merepresentasikan data buku
class Buku:
    def __init__(self, judul, tahun):
        self.judul = judul
        self.tahun = tahun

    # method untuk menentukan kategori buku berdasarkan tahun
    def kategori_buku(self):
        # if self.tahun <= 2015:
        #     return "Klasik"
        # elif self.tahun >= 2016 and self.tahun <= 2020:
        #     return "Modern"
        # elif self.tahun >= 2021 and self.tahun <= 2022:
        #     return "Terbaru"
        # else: 
        #     return "Sangat Terbaru"

        if self.tahun <= 2005:
            return "Klasik"
        elif self.tahun >= 2006 and self.tahun <= 2015:
            return "Modern"
        elif self.tahun >= 2016 and self.tahun <= 2020:
            return "Terbaru"
        else: 
            return "Sangat Terbaru"

    # method untuk menampilkan data buku dalam format tabel
    def __str__(self):
        return f"{self.judul:<20} {self.tahun:<10} {self.kategori_buku():<20}"


# Class untuk menyimpan daftar koleksi buku
class KoleksiBuku:
    def __init__(self):
        self.daftar = []   # list kosong untuk menampung buku

    # method untuk menambahkan buku baru ke daftar
    def tambah_buku(self, buku):
        self.daftar.append(buku)

    # method untuk menampilkan tabel daftar semua buku
    def tampilkan_buku(self):
        print("=" * 60)
        print(f"{'Judul':<20} {'Tahun':<10} {'Kategori':<20}")
        print("=" * 60)
        for buku in self.daftar:
            print(buku)
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
        buku = Buku(judul, tahun)
        koleksi.tambah_buku(buku)

    # Tampilkan hasil daftar buku
    print("\n=== Daftar Koleksi Buku ===")
    koleksi.tampilkan_buku()
