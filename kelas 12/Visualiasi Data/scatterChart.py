import matplotlib.pyplot as plt

# Data jam belajar dan nilai ujian 
jam_belajar = [1, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6]
nilai_ujian = [65, 70, 72, 75, 78, 82, 85, 88, 90, 92]

# Membuat scatter plot
plt.scatter(jam_belajar, nilai_ujian, s = 100, c='red', alpha=0.6, edgecolors='black')

# Menambahkan judul dan label sumbu
plt.title('Hubungan Jam Belajar vs Nilai Ujian', fontsize=14, fontweight='bold')
plt.xlabel('Jam Belajar per Hari')
plt.ylabel('Nilai Ujian')
plt.grid(True, linestyle='--', alpha=0.3)

plt.show()