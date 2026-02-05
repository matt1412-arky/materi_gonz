# No .1 
import matplotlib.pyplot as plt

hari = [
    "Senin",
    "Selasa",
    "Rabu",
    "Kamis",
    "Jumat",
    "Sabtu", 
    "Minggu",
]
minuman = [
    120,
    150,
    130,
    160,
    200,
    250,
    230
]
makanan = [
    80,
    90,
    85,
    100,
    140,
    180,
    170
]

plt.plot(hari, minuman, marker='o', label='Minuman', linewidth=2)
plt.plot(hari, makanan, marker='s', label='Makanan', linewidth=2)

plt.title('Perbandingan Makanan dan Minuman pada Kafe', fontsize=14, fontweight='bold')
plt.xlabel('Hari')
plt.ylabel('Jumlah Penjualan')
plt.legend()  # Menampilkan keterangan
plt.grid(True, linestyle='--', alpha=0.3)

plt.show()

# No. 2
import matplotlib.pyplot as plt

jam = [
    "09.00",
    "10.00",
    "11.00",
    "12.00",
    "13.00",
    "14.00",
    "15.00"
]

jumlah_pengunjung = [
    10,
    20,
    35,
    50,
    40,
    30,
    25
]

plt.barh(jam, jumlah_pengunjung, color='coral')

plt.title('Jumlah Pengunjung Perpustakaan', fontsize=14, fontweight='bold')
plt.xlabel('Jumlah Pengunjung')
plt.ylabel('Jam')

plt.show()

# No. 3
import matplotlib.pyplot as plt

mata_pelajaran = ['Matematika', 'Basis Data']
nilai_rata = [80, 82.6]

# Membuat grafik batang
plt.bar(mata_pelajaran, nilai_rata, color='skyblue', edgecolor='navy')

# Menambahkan judul dan label
plt.title('Nilai Rata-rata per Mata Pelajaran', fontsize=14, fontweight='bold')
plt.xlabel('Mata Pelajaran', fontsize=12)
plt.ylabel('Nilai Rata-rata', fontsize=12)
plt.ylim(0, 100)  # Mengatur batas sumbu y dari 0 hingga 100

# Menambahkan nilai di atas setiap batang
for i, nilai in enumerate(nilai_rata):
    plt.text(i, nilai + 1, str(nilai), ha='center', fontweight='bold')

# Menampilkan grafik
plt.show()

