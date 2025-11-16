# import os

# # Cek apakah file ada
# if os.path.exists('data_siswa.csv'):
#     print("✅ File ditemukan")
# else:
#     print("❌ File tidak ada")

# # Cek ukuran file
# ukuran = os.path.getsize('data_siswa.csv')
# print(f"📦 Ukuran file: {ukuran} bytes")

# # Lihat semua file di folder
# print("\n📁 Daftar file:")
# files = os.listdir('.')
# for file in files:
#     if file.endswith('.py'):
#         print(f"  - {file}")

# import os

# # Membuat folder baru
# if not os.path.exists('data'):
#     os.mkdir('data')
#     print("✅ Folder 'data' berhasil dibuat")

# # Membuat folder bertingkat
# os.makedirs('backup/2024/januari', exist_ok=True)
# print("✅ Folder backup berhasil dibuat")

import shutil

# # Copy file
# shutil.copy('data_siswa.csv', 'backup/data_siswa_backup.csv')
# print("✅ File berhasil dicopy")

# Move/Rename file
shutil.move('catatan.txt', 'data/catatan.txt')
print("✅ File berhasil dipindah")
