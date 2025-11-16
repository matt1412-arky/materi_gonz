import csv


class Statistik:
    def __init__(self, data_file="kehadiran.csv"):
        self.data_file = data_file

    def hitung(self):
        hadir, izin, sakit = 0, 0, 0
        with open(self.data_file, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["Status"] == "Hadir":
                    hadir += 1
                elif row["Status"] == "Izin":
                    izin += 1
                elif row["Status"] == "Sakit":
                    sakit += 1
        return hadir, izin, sakit

    def tampilkan(self):
        hadir, izin, sakit = self.hitung()
        print("\n📊 Statistik Kehadiran:")
        print(f"Hadir: {hadir}")
        print(f"Izin : {izin}")
        print(f"Sakit: {sakit}")
