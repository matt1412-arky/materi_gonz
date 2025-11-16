# import csv

# # Data siswa
# data_siswa = [
#     ['Nama', 'Kelas', 'Nilai'],
#     ['Ali', 'XI-A', 85],
#     ['Budi', 'XI-B', 78],
#     ['Citra', 'XI-A', 92],
#     ['Dina', 'XI-C', 88]
# ]

# # Menulis ke CSV
# with open('data_siswa.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(data_siswa)
    
# print("✅ File CSV berhasil dibuat!")

# import csv

# # Membaca CSV
# with open('data_siswa.csv', 'r') as file:
#     reader = csv.reader(file)
    
#     print("📋 Data Siswa:")
#     print("-" * 40)
    
#     for row in reader:
#         print(f"{row[0]:15} | {row[1]:8} | {row[2]}")

import csv

with open('data_siswa.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    total_nilai = 0
    jumlah_siswa = 0
    
    for row in reader:
        print(f"Nama: {row['Nama']}, Nilai: {row['Nilai']}")
        total_nilai += int(row['Nilai'])
        jumlah_siswa += 1
    
    rata_rata = total_nilai / jumlah_siswa
    print(f"\n📊 Rata-rata nilai: {rata_rata:.2f}")
