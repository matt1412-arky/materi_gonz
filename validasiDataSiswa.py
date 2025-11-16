class DataTidakValidError(Exception):
    pass

def validasi_data_siswa(nama, umur, nilai):
    try:
        # Validasi nama
        if not nama or len(nama) < 2:
            raise DataTidakValidError("Nama minimal 2 karakter")
        
        # Validasi umur
        if umur < 15 or umur > 20:
            raise DataTidakValidError("Umur harus 15-20 tahun")
            
        # Validasi nilai
        if nilai < 0 or nilai > 100:
            raise DataTidakValidError("Nilai harus 0-100")
            
        return "✅ Data siswa valid!"
        
    except DataTidakValidError as e:
        return f"❌ {e}"

# Test
print(validasi_data_siswa("Ali", 17, 85))      # Valid
print(validasi_data_siswa("A", 17, 85))       # Nama terlalu pendek
print(validasi_data_siswa("Budi", 25, 85))    # Umur tidak valid
print(validasi_data_siswa("Citra", 16, 150))  # Nilai tidak valid
