from utils import format_rupiah
from barang import Barang

class Inventaris:
    def __init__(self):
        self.barang_list = []

    def tambah_barang(self, barang: Barang):
        self.barang_list.append(barang)

    def tampilkan_inventaris(self):
        print("=" * 60)
        print(f"{'Nama Barang':<15} {'Jumlah':<5} {'Harga Satuan':<15} {'Total Harga':<15}")
        print("=" * 60)
        for barang in self.barang_list:
            print(barang)
        print("=" * 60)
        total_semua = sum([b.total_harga() for b in self.barang_list])
        print(f"{'TOTAL':<25}{' ':<15}{format_rupiah(total_semua):<15}")
        print("=" * 60)
