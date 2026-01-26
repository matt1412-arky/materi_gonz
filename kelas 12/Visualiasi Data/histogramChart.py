import matplotlib.pyplot as plt

# Data nilai ujian 30 siswa
nilai_ujian = [65, 70, 72, 75, 78, 80, 80, 82, 82, 85, 85, 85, 85, 88, 88,
88, 90, 90, 90, 92, 92, 95, 95, 95, 95, 98, 98, 100, 100, 100]

# Membuat histogram
plt.hist(nilai_ujian, bins=10, color='lightgreen', edgecolor='black')
plt.title('Distribusi Nilai Ujian Matematika', fontsize=14, fontweight='bold')
plt.xlabel('Nilai Ujian')
plt.ylabel('Jumlah Siswa')
plt.grid(True, axis='y', alpha=0.3)

plt.show()