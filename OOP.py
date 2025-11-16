class Makanan: 
    def __init__(self, nama_makanan):
        self.nama_makanan = nama_makanan

    def tampilkan_info(self):
        print(f"Hai, saya suka makan {self.nama_makanan}")

makanan1 = Makanan("Nasi Goreng")
makanan1.tampilkan_info()

# nama = input("Masukkan nama Anda: ");
# hobi = input("Masukkan hobi Anda: ");
# print(f"Halo {nama}, hobi kamu {hobi} ya!");