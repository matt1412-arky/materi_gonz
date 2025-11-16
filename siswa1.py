class Siswa:
    # Variabel class (berlaku untuk semua object Siswa)
    sekolah = "SMA Kolose Gonzaga"
    total_siswa = 0
    seragam = "Putih Abu"
    
    def __init__(self, nama, kelas, hobi):
        # Variabel instance (unik untuk tiap object)
        self.nama = nama
        self.kelas = kelas
        self.hobi = hobi
        self.nilai = []
        Siswa.total_siswa += 1  # setiap object baru, total_siswa bertambah
    
    def perkenalan(self):
        # Method untuk menampilkan info siswa
        print(f"Halo, nama saya {self.nama}, saya kelas {self.kelas} di {Siswa.sekolah}. Hobi saya adalah {self.hobi}.")

# List untuk menyimpan semua data siswa
data_siswa = []

def tambah_siswa():
    # Input data siswa
    nama = input("Masukkan nama siswa: ")
    kelas = input("Masukkan kelas siswa: ")
    hobi = input("Masukkan hobi siswa: ")

    # Membuat object baru dari class Siswa
    siswa_baru = Siswa(nama, kelas, hobi)
    
    # Menyimpan object ke dalam list data_siswa
    data_siswa.append(siswa_baru)
    
    # Menampilkan pesan berhasil
    print(f"✅ Siswa {siswa_baru.nama} berhasil ditambahkan!\n")
    print(f"📊 Total Siswa di {Siswa.sekolah} : {Siswa.total_siswa} orang\n")

def tampilkan_siswa():
    if not data_siswa:
        # Jika list kosong
        print("⚠️ Belum ada data siswa.\n")
    else:
        print("\n📄 Daftar Siswa:")
        
        # range(len(data_siswa)) menghasilkan urutan angka mulai dari 0 sampai jumlah data_siswa - 1
        # Fungsi len(data_siswa) = menghitung jumlah elemen di list data_siswa
        # Contoh: jika ada 3 siswa, len(data_siswa) = 3 → range(3) menghasilkan [0, 1, 2]
        for i in range(len(data_siswa)):
            print(f"{i+1}. ", end="")  # i+1 supaya penomoran mulai dari 1, bukan 0
            data_siswa[i].perkenalan()  # Mengakses object siswa berdasarkan index
        print()

# Program utama
while True:
    print("=== Pendaftaran Siswa ===")
    print("1. Tambah Siswa")
    print("2. Tampilkan Semua Siswa")
    print("3. Keluar")
    pilihan = input("Pilih menu [1-3]: ")

    if pilihan == "1":
        tambah_siswa()
        # tampilkan_siswa()  # langsung tampilkan setelah tambah
    elif pilihan == "2":
        tampilkan_siswa()
    elif pilihan == "3":
        print("👋 Program selesai.")
        break
    else:
        print("❌ Pilihan tidak valid.\n")
