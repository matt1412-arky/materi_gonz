# Contoh: Nilai Matematika per Semester
import matplotlib.pyplot as plt

# Data nilai matematika Ali selama 6 semester
nama = ['Ali', 'Budi', 'Citra', 'Dina', 'Eko']
jumlah_absen = [2, 5 , 1, 3, 4]

# Membuat grafik batang
plt.barh(nama, jumlah_absen, color='coral')

# Menambahkan judul dan label
plt.title('Jumlah Ketidakhadiran Siswa', fontsize=14, fontweight='bold')
plt.xlabel('Jumlah Hari Tidak Hadir')
plt.ylabel('Nama Siswa')

# Menampilkan grafik
plt.show()
