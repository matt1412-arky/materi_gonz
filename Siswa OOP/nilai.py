class Nilai:
    def __init__(self, siswa, mapel, nilai):
        self.siswa = siswa
        self.mapel = mapel
        self.nilai = nilai
    
    def info(self):
        print(f"{self.siswa.nama} - {self.mapel.nama}: {self.nilai}")