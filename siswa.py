class Siswa:
    # Variabel kelas (shared untuk semua objek)
    sekolah = "SMA Kolose Gonzaga"  # Nama sekolah, sama untuk semua siswa
    total_siswa = 0                 # Menyimpan total jumlah siswa
    seragam = "Putih Abu"           # Warna seragam sekolah
    
    def __init__(self, nama, kelas, hobi):
        # Variabel instance (unik untuk setiap objek siswa)
        self.nama = nama            # Nama siswa
        self.kelas = kelas          # Kelas siswa
        self.hobi = hobi            # Hobi siswa
        self.nilai = []              # Daftar nilai (kosong saat awal dibuat)
        
        # Setiap kali objek Siswa dibuat, total_siswa bertambah 1
        Siswa.total_siswa += 1
    
    def perkenalan(self):
        # Method untuk menampilkan perkenalan diri siswa"
        print(f"Halo, nama saya {self.nama}, saya kelas {self.kelas} di {Siswa.sekolah}. Hobi saya adalah {self.hobi}.")

# List untuk menyimpan semua objek siswa yang sudah dibuat
data_siswa = []

def tambah_siswa():
    # Fungsi untuk menambah data siswa baru
    nama = input("Masukkan nama siswa: ")
    kelas = input("Masukkan kelas siswa: ")
    hobi = input("Masukkan hobi siswa: ")

    # Membuat objek siswa baru dan menambahkannya ke dalam list data_siswa
    siswa_baru = Siswa(nama, kelas, hobi)
    data_siswa.append(siswa_baru)

    # Menampilkan pesan berhasil dan total siswa
    print(f"✅ Siswa {siswa_baru.nama} berhasil ditambahkan!\n")
    print(f"📊 Total Siswa di {Siswa.sekolah} : {Siswa.total_siswa} orang\n")

def tampilkan_siswa():
    # Fungsi untuk menampilkan semua siswa
    if not data_siswa:  # Cek apakah list kosong
        print("⚠️ Belum ada data siswa.\n")
    else:
        print("\n📄 Daftar Siswa:")
        
        # enumerate() digunakan untuk memberi nomor urut pada setiap siswa
        # enumerate(data_siswa, start=1) menghasilkan pasangan (index, siswa)
        # Contoh: [(1, siswa1), (2, siswa2), ...]
        for i, siswa in enumerate(data_siswa, start=1):
            print(f"{i}. ", end="")  # Menampilkan nomor urut
            siswa.perkenalan()       # Memanggil method perkenalan untuk setiap siswa
        
        print()  # Baris kosong

# Program utama (loop menu)
while True:
    print("=== Pendaftaran Siswa ===")
    print("1. Tambah Siswa")
    print("2. Tampilkan Semua Siswa")
    print("3. Keluar")
    pilihan = input("Pilih menu [1-3]: ")

    if pilihan == "1":
        tambah_siswa()   # Tambah siswa baru
        # tampilkan_siswa()  # Langsung tampilkan daftar siswa setelah ditambah
    elif pilihan == "2":
        tampilkan_siswa()  # Tampilkan semua siswa
    elif pilihan == "3":
        print("👋 Program selesai.")
        break
    else:
        print("❌ Pilihan tidak valid.\n")
