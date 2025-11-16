import matplotlib.pyplot as plt

# Data nilai 3 siswa
semester = [1, 2, 3, 4, 5, 6]
nilai_ali = [75, 78, 82, 85, 88, 90]
nilai_budi = [70, 75, 77, 80, 82, 85]
nilai_citra = [85, 87, 88, 90, 92, 95]

# Membuat grafik dengan 3 garis
plt.plot(semester, nilai_ali, marker='o', label='Ali', linewidth=2)
plt.plot(semester, nilai_budi, marker='s', label='Budi', linewidth=2)
plt.plot(semester, nilai_citra, marker='^', label='Citra', linewidth=2)

plt.title('Perbandingan Nilai Matematika', fontsize=14, fontweight='bold')
plt.xlabel('Semester')
plt.ylabel('Nilai')
plt.legend()  # Menampilkan keterangan
plt.grid(True, linestyle='--', alpha=0.3)

plt.show()
