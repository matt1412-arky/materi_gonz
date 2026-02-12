import os

def batch_rename(folder_path, prefix="", start_number=1):
    """
    Rename banyak file sekaligus dengan format:
    prefix_001.ext, prefix_002.ext, dst.
    """
    
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    files.sort()
    
    print(f"📁 Ditemukan {len(files)} file")
    print(f"🔄 Mulai rename dengan prefix: '{prefix}'\n")
    
    for index, filename in enumerate(files, start=start_number):
        # Ambil ekstensi file
        _, ext = os.path.splitext(filename)
        
        # Buat nama baru
        new_name = f"{prefix}_{index:03d}{ext}"
        
        # Path lengkap
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)
        
        # Rename
        os.rename(old_path, new_path)
        print(f"✅ {filename} → {new_name}")
    
    print(f"\n✨ Selesai! {len(files)} file berhasil direname.")

# Cara pakai
if __name__ == "__main__":
    folder = r"C:\Users\Lenovo\OneDrive\Documents\materi_gonz\kelas 11\tes"
    batch_rename(folder, prefix="Liburan_Bali", start_number=1)
