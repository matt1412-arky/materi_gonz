class MataPelajaran:
    def __init__(self, nama, kode):
        self.nama = nama
        self.kode = kode
    
    def info(self):
        print(f"Mapel: {self.nama} (Kode: {self.kode})")