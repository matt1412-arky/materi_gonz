# Membuat exception sendiri
class NilaiTerlaluRendahError(Exception):
    def __init__(self, nilai):
        self.nilai = nilai
        super().__init__(f"Nilai {nilai} terlalu rendah! Minimal 60")

# Menggunakan custom exception
def cek_kelulusan(nilai):
    if nilai < 60:
        raise NilaiTerlaluRendahError(nilai)
    else:
        return "🎉 LULUS!"

# Test program
try:
    nilai_siswa = int(input("Masukkan nilai: "))
    hasil = cek_kelulusan(nilai_siswa)
    print(hasil)
    
except NilaiTerlaluRendahError as e:
    print(f"❌ {e}")
    print("💡 Belajar lebih giat ya!")
    
except ValueError:
    print("❌ Nilai harus berupa angka!")
