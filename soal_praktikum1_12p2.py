from datetime import datetime

# Class Penduduk
class Penduduk:
    def __init__(self, nama, tempat_lahir, tanggal_lahir):
        # Lengkapi bagian ini
        pass
        # Simpan tanggal lahir sebagai objek datetime
        self.tanggal_lahir = datetime.strptime(tanggal_lahir, "%Y-%m-%d")

    # Method untuk menghitung umur
    def hitung_umur(self):
        hari_ini = datetime.today()
        umur = hari_ini.year - self.tanggal_lahir.year
        # Cek apakah ulang tahun sudah lewat tahun ini
        if (hari_ini.month, hari_ini.day) < (self.tanggal_lahir.month, self.tanggal_lahir.day):
            umur -= 1
        return umur

    # Method untuk mendaftar KTP
    def daftar_ktp(self):
        umur = self.hitung_umur()
        # Lengkapi bagian ini
        pass


# === MAIN PROGRAM ===
if __name__ == "__main__":
    # Input data penduduk
    nama = input("Masukkan nama: ")
    tempat_lahir = input("Masukkan tempat lahir: ")
    tanggal_lahir = input("Masukkan tanggal lahir (format YYYY-MM-DD): ")

    # Membuat objek dari class Penduduk
    # Lengkapi bagian ini
    pass

    # Cek apakah bisa mendaftar KTP
    # Lengkapi bagian ini
    pass
