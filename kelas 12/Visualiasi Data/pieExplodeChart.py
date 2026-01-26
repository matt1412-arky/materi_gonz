import matplotlib.pyplot as plt

# Data Hobi dan Jumlah Siswa
hobi = ['Olahraga', 'Musik', 'Membaca', 'Gaming', 'Seni']
jumlah_siswa = [12, 8, 5, 10, 5]

# Warna untuk setiap irisan
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']

# Explode: membuat potongon terpisah (fokus pada yang terbesar)
explode = (0.1, 0, 0, 0, 0)

# Membuat pie chart
plt.pie(jumlah_siswa, labels=hobi, colors=colors, autopct='%1.1f%%', explode=explode, shadow=True, startangle=90) 

# Menambahkan judul 
plt.title('Mata Pelajaran Favorit', fontsize=14, fontweight='bold')
plt.axis('equal')  # Agar pie chart berbentuk lingkaran

# Menampilkan grafik
plt.show()