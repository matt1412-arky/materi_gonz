import csv
import os

def simpan_nilai_siswa(nama, kelas, nilai):
    """Menyimpan data siswa ke CSV dengan error handling"""
    
    try:
        # Cek apakah nilai valid
        if nilai < 0 or nilai > 100:
            raise ValueError("Nilai harus antara 0-100")
        
        # Cek apakah file sudah ada
        file_exists = os.path.exists('nilai_siswa.csv')
        
        # Buka file (append mode)
        with open('nilai_siswa.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            
            # Tulis header jika file baru
            if not file_exists:
                writer.writerow(['Nama', 'Kelas', 'Nilai'])
            
            # Tulis data siswa
            writer.writerow([nama, kelas, nilai])
        
        print(f"✅ Data {nama} berhasil disimpan!")
        return True
        
    except ValueError as e:
        print(f"❌ Error: {e}")
        return False
        
    except PermissionError:
        print("❌ Error: File sedang dibuka di program lain")
        return False
        
    except Exception as e:
        print(f"❌ Error tidak terduga: {e}")
        return False

# Test fungsi
simpan_nilai_siswa("Ali", "XI-A", 85)
simpan_nilai_siswa("Budi", "XI-B", 110)  # Invalid value
simpan_nilai_siswa("Citra", "XI-A", 92)