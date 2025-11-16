from data_manager import DataManager
from statistik import Statistik


class AplikasiKehadiran:
    def __init__(self):
        self.data_manager = DataManager()
        self.statistik = Statistik()

    def menu(self):
        while True:
            print("\n=== MENU KEHADIRAN ===")
            print("1. Catat Kehadiran")
            print("2. Tampilkan Statistik")
            print("3. Keluar")

            pilihan = input("Pilih menu (1-3): ")

            if pilihan == "1":
                self.input_kehadiran()
            elif pilihan == "2":
                self.statistik.tampilkan()
            elif pilihan == "3":
                print("Program selesai. 👋")
                break
            else:
                print("Pilihan tidak valid!")

    def input_kehadiran(self):
        nama = input("Masukkan nama siswa: ")
        status = input("Status (Hadir/Izin/Sakit): ").capitalize()
        if status not in ["Hadir", "Izin", "Sakit"]:
            print("❌ Status tidak valid, coba lagi.")
            return
        self.data_manager.catat_kehadiran(nama, status)
        print(f"✅ Data kehadiran {nama} berhasil dicatat.")


if __name__ == "__main__":
    app = AplikasiKehadiran()
    app.menu()
