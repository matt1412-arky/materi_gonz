# Contoh: Nilai Matematika per Semester
import matplotlib.pyplot as plt

# Data nilai matematika Ali selama 6 semester
mata_pelajaran = ['Matematika', 'Fisika', 'Kimia', 'Biologi', 'Inggris']
nilai_rata = [85, 78, 82, 88, 90]

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
