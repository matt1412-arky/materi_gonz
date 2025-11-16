import csv
import os
import shutil
from datetime import datetime


class DataManager:
    def __init__(self, data_file="kehadiran.csv", backup_file="backup_kehadiran.csv"):
        self.data_file = data_file
        self.backup_file = backup_file
        self._buat_file_csv()

    def _buat_file_csv(self):
        """Buat file CSV jika belum ada."""
        if not os.path.exists(self.data_file):
            with open(self.data_file, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Tanggal", "Nama", "Status"])

    def backup_data(self):
        """Buat backup otomatis dari file utama."""
        shutil.copy(self.data_file, self.backup_file)

    def catat_kehadiran(self, nama, status):
        """Catat kehadiran siswa."""
        tanggal = datetime.now().strftime("%Y-%m-%d")
        with open(self.data_file, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([tanggal, nama, status])
        self.backup_data()
