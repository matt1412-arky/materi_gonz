# import json

# # Data dalam bentuk dictionary
# data_sekolah = {
#     "nama_sekolah": "SMA Merdeka",
#     "siswa": [
#         {"nama": "Ali", "kelas": "XI-A", "nilai": 85},
#         {"nama": "Budi", "kelas": "XI-B", "nilai": 78},
#         {"nama": "Citra", "kelas": "XI-A", "nilai": 92}
#     ],
#     "jumlah_siswa": 3
# }

# # Simpan ke file JSON
# with open('data_sekolah.json', 'w') as file:
#     json.dump(data_sekolah, file, indent=4)
    
# print("✅ File JSON berhasil dibuat!")

import json

# Baca file JSON
with open('data_sekolah.json', 'r') as file:
    data = json.load(file)

# Akses data
print(f"🏫 Sekolah: {data['nama_sekolah']}")
print(f"👥 Jumlah siswa: {data['jumlah_siswa']}\n")

print("📋 Daftar Siswa:")
for siswa in data['siswa']:
    print(f"  - {siswa['nama']} ({siswa['kelas']}): {siswa['nilai']}")
