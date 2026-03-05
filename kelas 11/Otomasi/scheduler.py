import schedule
import time
import shutil
from datetime import datetime
import os

def backup_task():
    """Tugas backup yang akan dijalankan otomatis"""
    
    source = r"C:\Users\Lenovo\OneDrive\Documents\materi_gonz"
    backup_location = r"C:\Users\Lenovo\OneDrive\Documents\backup"
    
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    backup_name = f"Tugas_Backup_{timestamp}"
    backup_path = os.path.join(backup_location, backup_name)
    
    try:
        shutil.copytree(source, backup_path)
        print(f"✅ [{timestamp}] Backup berhasil: {backup_path}")
    except Exception as e:
        print(f"❌ [{timestamp}] Backup gagal: {e}")

# Jadwalkan tugas
schedule.every().day.at("13:43").do(backup_task)  # Setiap hari jam 20:00
# schedule.every().hour.do(backup_task)           # Setiap jam
# schedule.every(30).minutes.do(backup_task)      # Setiap 30 menit
# schedule.every().monday.at("09:00").do(backup_task)  # Setiap Senin jam 09:00

print("🤖 Scheduler aktif!")
print("📅 Backup otomatis setiap hari jam 13:43")
print("⏸️  Tekan Ctrl+C untuk stop\n")

# Loop utama
while True:
    schedule.run_pending()
    time.sleep(60)  # Cek setiap 1 menit
