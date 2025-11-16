from utils import format_rupiah

class Barang:
    def __init__(self, nama, jumlah, harga):
        self.nama = nama
        self.jumlah = jumlah
        self.harga = harga

    def total_harga(self):
        return self.jumlah * self.harga

    def __str__(self):
        return f"{self.nama:<15} {self.jumlah:<5} {format_rupiah(self.harga):<15} {format_rupiah(self.total_harga()):<15}"
