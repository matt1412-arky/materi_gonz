from barang import Barang
from inventaris import Inventaris

if __name__ == "__main__":
    inventaris = Inventaris()

    print("=== Input Data Inventaris (10 Barang) ===")
    for i in range(1, 11):
        print(f"\nBarang ke-{i}:")
        nama = input("Masukkan nama barang: ")
        jumlah = int(input("Masukkan jumlah: "))
        harga = int(input("Masukkan harga satuan: "))
        barang = Barang(nama, jumlah, harga)
        inventaris.tambah_barang(barang)

    print("\n=== Daftar Inventaris ===")
    inventaris.tampilkan_inventaris()
