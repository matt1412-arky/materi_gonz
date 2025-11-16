import json
import os
from datetime import datetime

class CatatanHarian:
    def __init__(self):
        self.file_catatan = 'catatan_harian.json'
        self.catatan = self.load_catatan()
    
    def load_catatan(self):
        """Memuat catatan dari file"""
        try:
            if os.path.exists(self.file_catatan):
                with open(self.file_catatan, 'r') as file:
                    return json.load(file)
            return []
        except Exception as e:
            print(f"❌ Error membaca file: {e}")
            return []
    
    def simpan_catatan(self):
        """Menyimpan catatan ke file"""
        try:
            with open(self.file_catatan, 'w') as file:
                json.dump(self.catatan, file, indent=4)
            return True
        except Exception as e:
            print(f"❌ Error menyimpan file: {e}")
            return False
    
    def tambah_catatan(self, judul, isi):
        """Menambah catatan baru"""
        tanggal = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        catatan_baru = {
            'id': len(self.catatan) + 1,
            'tanggal': tanggal,
            'judul': judul,
            'isi': isi
        }
        
        self.catatan.append(catatan_baru)
        
        if self.simpan_catatan():
            print(f"✅ Catatan '{judul}' berhasil ditambahkan!")
        
    def lihat_semua_catatan(self):
        """Menampilkan semua catatan"""
        if not self.catatan:
            print("📝 Belum ada catatan")
            return
        
        print("\n" + "="*50)
        print("📖 CATATAN HARIAN")
        print("="*50)
        
        for cat in self.catatan:
            print(f"\n🆔 ID: {cat['id']}")
            print(f"📅 Tanggal: {cat['tanggal']}")
            print(f"📌 Judul: {cat['judul']}")
            print(f"📝 Isi: {cat['isi']}")
            print("-"*50)
    
    def cari_catatan(self, keyword):
        """Mencari catatan berdasarkan kata kunci"""
        hasil = []
        
        for cat in self.catatan:
            if keyword.lower() in cat['judul'].lower() or \
               keyword.lower() in cat['isi'].lower():
                hasil.append(cat)
        
        if hasil:
            print(f"\n🔍 Ditemukan {len(hasil)} catatan:")
            for cat in hasil:
                print(f"  - [{cat['id']}] {cat['judul']}")
        else:
            print("❌ Tidak ada catatan yang ditemukan")
    
    def export_txt(self):
        """Export catatan ke file TXT"""
        try:
            with open('catatan_export.txt', 'w') as file:
                file.write("CATATAN HARIAN\n")
                file.write("="*50 + "\n\n")
                
                for cat in self.catatan:
                    file.write(f"Tanggal: {cat['tanggal']}\n")
                    file.write(f"Judul: {cat['judul']}\n")
                    file.write(f"Isi: {cat['isi']}\n")
                    file.write("-"*50 + "\n\n")
            
            print("✅ Catatan berhasil di-export ke catatan_export.txt")
        except Exception as e:
            print(f"❌ Error export: {e}")

# Program utama
def main():
    app = CatatanHarian()
    
    while True:
        print("\n" + "="*50)
        print("📔 APLIKASI CATATAN HARIAN")
        print("="*50)
        print("1. Tambah catatan")
        print("2. Lihat semua catatan")
        print("3. Cari catatan")
        print("4. Export ke TXT")
        print("5. Keluar")
        
        try:
            pilihan = input("\nPilih menu (1-5): ")
            
            if pilihan == '1':
                judul = input("Judul: ")
                isi = input("Isi catatan: ")
                app.tambah_catatan(judul, isi)
                
            elif pilihan == '2':
                app.lihat_semua_catatan()
                
            elif pilihan == '3':
                keyword = input("Cari kata kunci: ")
                app.cari_catatan(keyword)
                
            elif pilihan == '4':
                app.export_txt()
                
            elif pilihan == '5':
                print("👋 Terima kasih!")
                break
                
            else:
                print("❌ Pilihan tidak valid!")
                
        except KeyboardInterrupt:
            print("\n\n👋 Program dihentikan")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

# Jalankan program
if __name__ == "__main__":
    main()