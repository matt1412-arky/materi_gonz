# Contoh: Nilai Matematika per Semester
import matplotlib.pyplot as plt

# Data nilai matematika Ali selama 6 semester
semester = [1, 2, 3, 4, 5, 6]
nilai = [75, 78, 82, 85, 88, 90]

# Membuat grafik garis
plt.plot(semester, nilai, marker='o', color='blue', linewidth=2)

# Menambahkan judul dan label
plt.title('Perkembangan Nilai Matematika Ali', fontsize=14, fontweight='bold')
plt.xlabel('Semester', fontsize=12)
plt.ylabel('Nilai', fontsize=12)

# Menambahkan grid agar lebih mudah dibaca
plt.grid(True, linestyle='--', alpha=0.5)

# Menampilkan grafik
plt.show()
