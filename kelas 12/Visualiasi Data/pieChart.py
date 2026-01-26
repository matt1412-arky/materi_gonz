import matplotlib.pyplot as plt

# Data Hobi dan Jumlah Siswa
hobi = ['Olahraga', 'Musik', 'Membaca', 'Gaming', 'Seni']
jumlah_siswa = [12, 8, 5, 10, 5]

# Warna untuk setiap irisan
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']

# Membuat pie chart
plt.pie(jumlah_siswa, labels=hobi, colors=colors, autopct='%1.1f%%', startangle=90) 

# Menambahkan judul 
plt.title('Distribusi Hobi Siswa Kelas XI-A', fontsize=14, fontweight='bold')
plt.axis('equal')  # Agar pie chart berbentuk lingkaran

# Menampilkan grafik
plt.show()