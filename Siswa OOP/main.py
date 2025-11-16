# file: main.py
from operasi import (
    # siswa
    tambah_siswa, tampilkan_siswa, edit_siswa, hapus_siswa, cari_siswa,
    # guru
    tambah_guru, tampilkan_guru, edit_guru, hapus_guru, cari_guru,
    # mapel
    tambah_mapel, tampilkan_mapel, edit_mapel, hapus_mapel, cari_mapel,
    # nilai
    tambah_nilai, tampilkan_nilai, edit_nilai, hapus_nilai, cari_nilai,
    # data
    simpan_data, load_data
)
import os
from colorama import Fore, init # type: ignore
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# === MENU SISWA ===
def menu_siswa():
    while True:
        clear_screen()
        print(Fore.CYAN + "=" * 40)
        print(Fore.YELLOW + "👤 MENU SISWA".center(40))
        print(Fore.CYAN + "=" * 40)
        print("1. Tambah Siswa")
        print("2. Lihat Semua Siswa")
        print("3. Edit Siswa")
        print("4. Hapus Siswa")
        print("5. Cari Siswa")
        print("6. Kembali ke Menu Utama")
        print(Fore.CYAN + "=" * 40)

        pilihan = input("Pilih menu siswa (1-6): ")
        if pilihan == "1": tambah_siswa()
        elif pilihan == "2": tampilkan_siswa()
        elif pilihan == "3": edit_siswa()
        elif pilihan == "4": hapus_siswa()
        elif pilihan == "5": cari_siswa()
        elif pilihan == "6": break
        else: print("❌ Pilihan tidak valid!")
        input("\n⏎ Tekan Enter untuk kembali...")

# === MENU GURU ===
def menu_guru():
    while True:
        clear_screen()
        print(Fore.CYAN + "=" * 40)
        print(Fore.YELLOW + "👨‍🏫 MENU GURU".center(40))
        print(Fore.CYAN + "=" * 40)
        print("1. Tambah Guru")
        print("2. Lihat Semua Guru")
        print("3. Edit Guru")
        print("4. Hapus Guru")
        print("5. Cari Guru")
        print("6. Kembali ke Menu Utama")
        print(Fore.CYAN + "=" * 40)

        pilihan = input("Pilih menu guru (1-6): ")
        if pilihan == "1": tambah_guru()
        elif pilihan == "2": tampilkan_guru()
        elif pilihan == "3": edit_guru()
        elif pilihan == "4": hapus_guru()
        elif pilihan == "5": cari_guru()
        elif pilihan == "6": break
        else: print("❌ Pilihan tidak valid!")
        input("\n⏎ Tekan Enter untuk kembali...")

# === MENU MATA PELAJARAN ===
def menu_mapel():
    while True:
        clear_screen()
        print(Fore.CYAN + "=" * 40)
        print(Fore.YELLOW + "📚 MENU MATA PELAJARAN".center(40))
        print(Fore.CYAN + "=" * 40)
        print("1. Tambah Mapel")
        print("2. Lihat Semua Mapel")
        print("3. Edit Mapel")
        print("4. Hapus Mapel")
        print("5. Cari Mapel")
        print("6. Kembali ke Menu Utama")
        print(Fore.CYAN + "=" * 40)

        pilihan = input("Pilih menu mapel (1-6): ")
        if pilihan == "1": tambah_mapel()
        elif pilihan == "2": tampilkan_mapel()
        elif pilihan == "3": edit_mapel()
        elif pilihan == "4": hapus_mapel()
        elif pilihan == "5": cari_mapel()
        elif pilihan == "6": break
        else: print("❌ Pilihan tidak valid!")
        input("\n⏎ Tekan Enter untuk kembali...")

# === MENU NILAI ===
def menu_nilai():
    while True:
        clear_screen()
        print(Fore.CYAN + "=" * 40)
        print(Fore.YELLOW + "📝 MENU NILAI".center(40))
        print(Fore.CYAN + "=" * 40)
        print("1. Tambah Nilai")
        print("2. Lihat Semua Nilai")
        print("3. Edit Nilai")
        print("4. Hapus Nilai")
        print("5. Cari Nilai")
        print("6. Kembali ke Menu Utama")
        print(Fore.CYAN + "=" * 40)

        pilihan = input("Pilih menu nilai (1-6): ")
        if pilihan == "1": tambah_nilai()
        elif pilihan == "2": tampilkan_nilai()
        elif pilihan == "3": edit_nilai()
        elif pilihan == "4": hapus_nilai()
        elif pilihan == "5": cari_nilai()
        elif pilihan == "6": break
        else: print("❌ Pilihan tidak valid!")
        input("\n⏎ Tekan Enter untuk kembali...")

# === MENU UTAMA ===
def main_menu():
    while True:
        clear_screen()
        print(Fore.CYAN + "=" * 40)
        print(Fore.YELLOW + "🏫 SISTEM MANAJEMEN SEKOLAH 🏫".center(40))
        print(Fore.CYAN + "=" * 40)
        print("1. 👤 Menu Siswa")
        print("2. 👨‍🏫 Menu Guru")
        print("3. 📚 Menu Mapel")
        print("4. 📝 Menu Nilai")
        print("5. 💾 Simpan Data")
        print("6. 📂 Load Data")
        print("7. 🚪 Keluar")
        print(Fore.CYAN + "=" * 40)

        pilihan = input("Pilih menu utama (1-7): ")
        if pilihan == "1": menu_siswa()
        elif pilihan == "2": menu_guru()
        elif pilihan == "3": menu_mapel()
        elif pilihan == "4": menu_nilai()
        elif pilihan == "5": simpan_data()
        elif pilihan == "6": load_data()
        elif pilihan == "7":
            clear_screen()
            print("👋 Terima kasih telah menggunakan program ini!")
            break
        else:
            print("❌ Pilihan tidak valid!")
            input("\n⏎ Tekan Enter untuk kembali...")

if __name__ == "__main__":
    main_menu()
