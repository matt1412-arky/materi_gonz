import os
import shutil
from datetime import datetime

def backup_folder(source, backup_location):
    """
    Backup folder dengan timestamp
    """
    
    # Buat nama backup dengan tanggal
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    folder_name = os.path.basename(source)
    backup_name = f"{folder_name}_backup_{timestamp}"
    backup_path = os.path.join(backup_location, backup_name)
    
    try:
        print(f"📦 Membackup: {source}")
        print(f"📂 Ke: {backup_path}")
        
        # Copy seluruh folder
        shutil.copytree(source, backup_path)
        
        # Hitung ukuran backup
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(backup_path):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                total_size += os.path.getsize(filepath)
        
        size_mb = total_size / (1024 * 1024)
        
        print(f"✅ Backup berhasil!")
        print(f"📊 Ukuran: {size_mb:.2f} MB")
        print(f"📅 Waktu: {timestamp}")
        
        return backup_path
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

# Cara pakai
if __name__ == "__main__":
    source_folder = r"C:\Users\Lenovo\OneDrive\Documents\materi_gonz"
    backup_location = r"C:\Users\Lenovo\OneDrive\Documents\backup"
    
    backup_folder(source_folder, backup_location)
