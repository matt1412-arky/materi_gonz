# Menulis file baru (mode 'w' = write)
with open('catatan.txt', 'w') as file:
    file.write("Ini adalah baris pertama\n")
    file.write("Ini adalah baris kedua\n")
    
print("✅ File berhasil dibuat!")

# Menambah isi file (mode 'a' = append)
with open('catatan.txt', 'a') as file:
    file.write("Ini adalah baris tambahan\n")
print("✅ Isi file berhasil ditambahkan!")

# Membaca seluruh isi file
with open('catatan.txt', 'r') as file:
    isi = file.read()
    print(isi)

# Membaca per baris
with open('catatan.txt', 'r') as file:
    for baris in file:
        print(baris.strip())  # strip() menghapus \n
