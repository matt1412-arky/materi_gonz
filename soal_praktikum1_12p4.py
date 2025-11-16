# Class untuk merepresentasikan data siswa
class Siswa:
    def __init__(self, nama, nilai):
        # Lengkapi bagian ini
        pass

    # method untuk menentukan grade berdasarkan nilai
    def tentukan_grade(self):
        # Lengkapi bagian ini
        pass

    # method untuk menampilkan data siswa dalam format tabel
    def __str__(self):
        return f"{self.nama:<15} {self.nilai:<10} {self.tentukan_grade():<20}"


# Class untuk menyimpan daftar nilai siswa
class DaftarNilai:
    def __init__(self):
        self.daftar = []   # list kosong untuk menampung siswa

    # method untuk menambahkan siswa baru ke daftar
    def tambah_siswa(self, siswa):
        # Lengkapi bagian ini 
        pass

    # method untuk menampilkan tabel nilai semua siswa
    def tampilkan_nilai(self):
        print("=" * 60)
        print(f"{'Nama':<15} {'Nilai':<10} {'Grade':<20}")
        print("=" * 60)
        for siswa in self.daftar:
            # Lengkapi bagian ini
            pass
        print("=" * 60)
        print(f"Rata-rata nilai seluruh siswa: {self.format_rata2():.2f}")
        print("=" * 60)

    # method untuk menghitung rata-rata nilai
    def format_rata2(self):
        if len(self.daftar) == 0:
            return 0
        total = sum([siswa.nilai for siswa in self.daftar if 0 <= siswa.nilai <= 100])
        return total / len(self.daftar)


# MAIN PROGRAM
if __name__ == "__main__":
    daftar_nilai = DaftarNilai()

    print("=== Input Data Nilai Siswa (10 siswa) ===")
    for i in range(1, 11):
        print(f"\nSiswa ke-{i}:")
        nama = input("Masukkan nama siswa: ")
        nilai = int(input("Masukkan nilai: "))
        # Lengkapi bagian ini
        pass

    # Tampilkan hasil daftar nilai
    print("\n=== Daftar Nilai Siswa ===")
    # Lengkapi bagian ini
    pass