# file: siswa.py
class Siswa:
    def __init__(self, nama, kelas):
        self.nama = nama
        self.kelas = kelas
    
    def info(self):
        print(f"Nama: {self.nama} - Kelas: {self.kelas}")