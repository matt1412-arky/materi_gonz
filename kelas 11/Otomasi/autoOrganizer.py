"""
AUTO-ORGANIZER
Aplikasi untuk mengorganisir file, backup, dan reminder
"""

import os
import shutil
from datetime import datetime
import schedule
import time

class AutoOrganizer:
    def __init__(self):
        self.config = {
            'watch_folder': r"C:\Users\YourName\Downloads",
            'backup_location': r"D:\Backup",
            'organize_time': "21:00",  # Jam 9 malam
            'backup_time': "22:00"      # Jam 10 malam
        }
        
        self.file_types = {
            'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
            'Documents': ['.pdf', '.doc', '.docx', '.txt', '.ppt', '.xlsx'],
            'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
            'Music': ['.mp3', '.wav', '.flac'],
            'Archives': ['.zip', '.rar', '.7z'],
            'Code': ['.py', '.java', '.cpp', '.js', '.html', '.css']
        }
    
    def organize_files(self):
        """Organisir file"""
        folder = self.config['watch_folder']
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        print(f"\n[{timestamp}] 🔄 Mulai mengorganisir file...")
        
        count = 0
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            
            if os.path.isdir(file_path):
                continue
            
            file_ext = os.path.splitext(filename)[1].lower()
            
            for category, extensions in self.file_types.items():
                if file_ext in extensions:
                    category_path = os.path.join(folder, category)
                    
                    if not os.path.exists(category_path):
                        os.makedirs(category_path)
                    
                    destination = os.path.join(category_path, filename)
                    
                    # Handle duplicate
                    if os.path.exists(destination):
                        base, ext = os.path.splitext(filename)
                        counter = 1
                        
                        while os.path.exists(destination):
                            new_name = f"{base}_{counter}{ext}"
                            destination = os.path.join(category_path, new_name)
                            counter += 1
                    
                    shutil.move(file_path, destination)
                    count += 1
                    print(f"📁 {filename} → {category}/")
                    break
        
        print(f"✅ Selesai! {count} file dipindahkan")

    def backup_files(self):
        """Backup folder"""
        source = self.config['watch_folder']
        backup_base = self.config['backup_location']
        
        date_folder = datetime.now().strftime("%Y-%m-%d")
        backup_path = os.path.join(backup_base, date_folder)
        
        print(f"\n💾 Mulai backup ke {backup_path}")
        
        if not os.path.exists(backup_path):
            os.makedirs(backup_path)
        
        for item in os.listdir(source):
            s = os.path.join(source, item)
            d = os.path.join(backup_path, item)
            
            if os.path.isdir(s):
                shutil.copytree(s, d, dirs_exist_ok=True)
            else:
                shutil.copy2(s, d)
        
        print("✅ Backup selesai!")

    def reminder(self):
        """Reminder harian"""
        print("\n🔔 Reminder:")
        print("• Bersihkan file yang tidak diperlukan")
        print("• Backup penting sudah dilakukan")
        print("• Folder sudah terorganisir")

    def run_scheduler(self):
        """Menjalankan scheduler"""
        schedule.every().day.at(self.config['organize_time']).do(self.organize_files)
        schedule.every().day.at(self.config['backup_time']).do(self.backup_files)
        schedule.every().day.at("20:00").do(self.reminder)

        print("🚀 Auto Organizer berjalan...")
        print(f"📂 Folder dipantau: {self.config['watch_folder']}")
        print(f"🕘 Organize: {self.config['organize_time']}")
        print(f"💾 Backup: {self.config['backup_time']}")

        while True:
            schedule.run_pending()
            time.sleep(60)


if __name__ == "__main__":
    app = AutoOrganizer()
    app.run_scheduler()