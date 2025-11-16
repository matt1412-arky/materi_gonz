# Class untuk merepresentasikan data siswa
class Siswa:
    def __init__(self, nama, nilai):
        self.nama = nama      # atribut nama siswa
        self.nilai = nilai    # atribut nilai siswa

    # method untuk menentukan grade berdasarkan nilai
    def tentukan_grade(self):
        if self.nilai >= 90 and self.nilai <= 100:
            return "A"
        elif self.nilai >= 75 and self.nilai < 90:
            return "B"
        elif self.nilai >= 60 and self.nilai < 75:
            return "C"
        elif self.nilai < 60 and self.nilai >= 0:
            return "D"
        else:
            return "Nilai tidak valid"

    # method untuk menampilkan data siswa dalam format tabel
    def __str__(self):
        return f"{self.nama:<15} {self.nilai:<10} {self.tentukan_grade():<20}"


# Class untuk menyimpan daftar nilai siswa
class DaftarNilai:
    def __init__(self):
        self.daftar = []   # list kosong untuk menampung siswa

    # method untuk menambahkan siswa baru ke daftar
    def tambah_siswa(self, siswa):
        self.daftar.append(siswa)

    # method untuk menampilkan tabel nilai semua siswa
    def tampilkan_nilai(self):
        print("=" * 60)
        print(f"{'Nama':<15} {'Nilai':<10} {'Grade':<20}")
        print("=" * 60)
        for siswa in self.daftar:
            print(siswa)
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
        siswa = Siswa(nama, nilai)
        daftar_nilai.tambah_siswa(siswa)

    # Tampilkan hasil daftar nilai
    print("\n=== Daftar Nilai Siswa ===")
    daftar_nilai.tampilkan_nilai()
