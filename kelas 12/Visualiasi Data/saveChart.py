import matplotlib.pyplot as plt

# Buat grafik
semester = [1, 2, 3, 4, 5, 6]
nilai = [75, 78, 82, 85, 88, 90] 

plt.plot(semester, nilai, marker='o', linewidth=2)
plt.title('Perkembangan Nilai')
plt.xlabel('Semester')
plt.ylabel('Nilai')
plt.grid(True)

# Simpan grafik sebagai file gambar
plt.savefig('grafik_nilai.png', dpi=300, bbox_inches='tight')

print("✅ Grafik telah disimpan sebagai 'grafik_nilai.png'")

plt.show()