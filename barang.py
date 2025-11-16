# Membuat class Barang untuk merepresentasikan setiap barang
class Barang:
    # Konstruktor untuk inisialisasi atribut barang
    def __init__(self, nama, jumlah, harga):
        self.nama = nama          # Nama barang
        self.jumlah = jumlah      # Jumlah barang
        self.harga = harga        # Harga satuan barang

    # Method untuk menghitung total harga (jumlah x harga satuan)
    def total_harga(self):
        return self.jumlah * self.harga

    # Method khusus untuk menampilkan data barang dalam bentuk string (tabel rapi)
    def __str__(self):
        return f"{self.nama:<15} {self.jumlah:<5} {format_rupiah(self.harga):<15} {format_rupiah(self.total_harga()):<15}"


# Membuat class Inventaris untuk menyimpan daftar barang
class Inventaris:
    def __init__(self):
        self.barang_list = []     # List kosong untuk menampung barang-barang

    # Method untuk menambahkan barang ke dalam daftar inventaris
    def tambah_barang(self, barang):
        self.barang_list.append(barang)

    # Method untuk menampilkan seluruh inventaris dalam bentuk tabel
    def tampilkan_inventaris(self):
        print("=" * 60)   # Cetak garis pemisah
        # Cetak header tabel
        print(f"{'Nama Barang':<15} {'Jumlah':<5} {'Harga Satuan':<15} {'Total Harga':<15}")
        print("=" * 60)
        # Loop untuk mencetak semua barang dalam daftar
        for barang in self.barang_list:
            print(barang)
        print("=" * 60)
        # Hitung total semua barang
        total_semua = sum([b.total_harga() for b in self.barang_list])
        # Cetak total keseluruhan harga inventaris
        print(f"{'TOTAL':<25}{' ':<15}{format_rupiah(total_semua):<15}")
        print("=" * 60)


# Fungsi untuk memformat angka menjadi format Rupiah
def format_rupiah(angka):
    return f"Rp{angka:,.0f}".replace(",", ".")  # Contoh: 10000 -> Rp10.000


# MAIN PROGRAM
if __name__ == "__main__":
    inventaris = Inventaris()   # Buat objek inventaris

    print("=== Input Data Inventaris (10 Barang) ===")
    # Input data sebanyak 10 barang
    for i in range(1, 11):
        print(f"\nBarang ke-{i}:")
        nama = input("Masukkan nama barang: ")      # Input nama barang
        jumlah = int(input("Masukkan jumlah: "))    # Input jumlah barang
        harga = int(input("Masukkan harga satuan: "))  # Input harga barang
        # Buat objek barang baru
        barang = Barang(nama, jumlah, harga)
        # Tambahkan barang ke daftar inventaris
        inventaris.tambah_barang(barang)

    # Setelah input selesai, tampilkan seluruh inventaris
    print("\n=== Daftar Inventaris ===")
    inventaris.tampilkan_inventaris()
