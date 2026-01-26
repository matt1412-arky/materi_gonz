import matplotlib.pyplot as plt

# Data tinggi, berat, dan umur siswa

tinggi = [150, 155, 160, 165, 170, 175, 180]

berat = [45, 50, 55, 60, 65, 70, 75]

umur = [15, 15, 16, 16, 17, 17, 18] # Ukuran titik berdasarkan umur

# Membuat scatter plot
plt.scatter(tinggi, berat, s=[u*30 for u in umur], alpha=0.5, c=umur, cmap='viridis')

plt.colorbar(label="Umur") # Menampilkan skala warna

plt.title('Hubungan Tinggi, Berat, dan Umur Siswa', fontsize=14, fontweight='bold')
plt.xlabel('Tinggi Badan (cm)')
plt.ylabel('Berat Badan (kg)')
plt.grid(True)

plt.show()
