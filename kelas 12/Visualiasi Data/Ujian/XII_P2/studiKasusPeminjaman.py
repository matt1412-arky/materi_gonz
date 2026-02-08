import openpyxl
import matplotlib.pyplot as plt
import os
from collections import Counter
from datetime import datetime


# =========================
# BUAT FOLDER OUTPUT
# =========================

output_folder = "C:/Users/Lenovo/OneDrive/Documents/materi_gonz/kelas 12/Visualiasi Data/Ujian/XII_P4/hasil_grafik"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# =========================
# LOAD EXCEL
# =========================
wb = openpyxl.load_workbook(
"C:/Users/Lenovo/OneDrive/Documents/materi_gonz/kelas 12/Visualiasi Data/Ujian/dataset/kunjungan_perpustakaan.xlsx"
)

sheet = wb.active
# ================= PIE TUJUAN =================

tujuan_labels = [
    "Membaca Buku",
    "Meminjam Buku",
    "Mengembalikan Buku",
    "Kelas Mandarin",
    "Refleksi Semester",
    "Tugas / Belajar / Konsultasi",
    "Kunjungan",
    "Kerja Sosial / Sanksi",
    "Lainnya"
]

tujuan_jumlah = [
    96,   # Membaca Buku
    44,   # Meminjam Buku
    34,   # Mengembalikan Buku
    13,   # Kelas Mandarin
    8,    # Refleksi Semester
    28,   # Tugas / Belajar / Konsultasi
    14,   # Kunjungan
    6,    # Kerja Sosial / Sanksi
    5     # Lainnya
]

plt.figure(figsize=(10,7))

plt.pie(tujuan_jumlah, autopct="%1.1f%%", startangle=90)

plt.legend(
    tujuan_labels,
    loc="center left",
    bbox_to_anchor=(1, 0.5)
)

plt.title("Tujuan Kunjungan Perpustakaan (Bulan Januari)")
plt.tight_layout()
plt.savefig(output_folder + "/perpustakaan_tujuan.png")
plt.close()

# ================= PIE KELAS =================

kelas_labels = [
    "X-7",
    "X-3",
    "X-2",
    "X-1",
    "X-4",
    "X-8",
    "XI-3",
    "XI-5",
    "XI-6",
    "XI-7",
    "XI-8",
    "XII-3",
    "XII-5",
    "Lainnya"
]

kelas_jumlah = [
    38,   # X-7
    26,   # X-3
    22,   # X-2
    19,   # X-1
    17,   # X-4
    15,   # X-8
    21,   # XI-3
    18,   # XI-5
    14,   # XI-6
    13,   # XI-7
    10,   # XI-8
    9,    # XII-3
    8,    # XII-5
    12    # Lainnya
]

plt.figure(figsize=(7,7))

plt.pie(
    kelas_jumlah,
    labels=kelas_labels,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Kelas Terbanyak Mengunjungi Perpustakaan (Bulan Januari)")
plt.tight_layout()
plt.savefig(output_folder + "/perpustakaan_kelas.png")
plt.close()
# ================= JAM RAMAI =================

# =====================
# DATA TIMESTAMP JANUARI
# =====================

timestamps = [
"10/01/2025 7:27:15","10/01/2025 7:27:32","10/01/2025 7:29:30",
"10/01/2025 7:30:48","10/01/2025 7:41:25","10/01/2025 7:41:25",
"10/01/2025 7:51:23","10/01/2025 7:51:48","10/01/2025 8:56:00",
"10/01/2025 9:00:28","10/01/2025 9:03:09","10/01/2025 9:03:35",
"10/01/2025 9:16:17","10/01/2025 9:16:28","10/01/2025 9:17:01",
"10/01/2025 9:22:44","10/01/2025 9:23:04",
"13/01/2025 6:43:57","13/01/2025 7:02:17","13/01/2025 7:02:19",
"13/01/2025 7:03:16","13/01/2025 7:04:17","13/01/2025 7:18:08",
"13/01/2025 7:18:13","13/01/2025 10:07:01","13/01/2025 12:25:57",
"13/01/2025 12:26:01","13/01/2025 12:31:03","13/01/2025 12:31:05",
"13/01/2025 14:11:56","13/01/2025 14:12:08","13/01/2025 14:15:41",
"13/01/2025 14:22:43","13/01/2025 14:22:54","13/01/2025 14:35:50",
"14/01/2025 9:44:04","14/01/2025 9:47:55","14/01/2025 9:47:57",
"14/01/2025 10:02:13","14/01/2025 12:22:16","14/01/2025 12:25:11",
"14/01/2025 12:25:38","14/01/2025 12:26:10","14/01/2025 14:08:14",
"14/01/2025 14:10:31","14/01/2025 14:14:24"
]

# =====================
# AMBIL JAM SAJA
# =====================

jam = []

for t in timestamps:
    dt = datetime.strptime(t, "%d/%m/%Y %H:%M:%S")
    jam.append(dt.hour)

# =====================
# HISTOGRAM
# =====================

plt.figure(figsize=(8,5))
plt.hist(jam, bins=range(6,17))
plt.xticks(range(6,17))
plt.xlabel("Jam")
plt.ylabel("Jumlah Kunjungan")
plt.title("Histogram Jam Kunjungan Perpustakaan Januari")

plt.savefig(output_folder + "/perpustakaan_jam.png")

print("SOAL 3 SELESAI & GRAFIK NORMAL.")
