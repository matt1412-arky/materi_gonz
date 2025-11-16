from library import Library

def tampilkan_menu():
    print("\n=== Sistem Perpustakaan ===")
    print("1. Tambah Buku")
    print("2. Lihat Semua Buku")
    print("3. Cari Buku")
    print("4. Keluar")

def main():
    perpustakaan = Library()
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ")
        try:
            if pilihan == "1":
                judul = input("Masukkan judul buku: ")
                penulis = input("Masukkan nama penulis: ")
                tahun = input("Masukkan tahun terbit: ")
                perpustakaan.tambah_buku(judul, penulis, tahun)
            elif pilihan == "2":
                perpustakaan.lihat_buku()
            elif pilihan == "3":
                judul = input("Masukkan judul buku yang dicari: ")
                perpustakaan.cari_buku(judul)
            elif pilihan == "4":
                print("Terima kasih, program selesai.")
                break
            else:
                raise ValueError("Pilihan menu tidak valid!")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
