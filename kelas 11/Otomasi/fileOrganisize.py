import os
import shutil

def organize_files(folder_path):
    """
    Organisir file berdasarkan ekstensi
    """
    
    # Definisi kategori file
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.ppt', '.pptx', '.xls', '.xlsx'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.flv'],
        'Music': ['.mp3', '.wav', '.flac', '.m4a'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
        'Programs': ['.exe', '.msi', '.apk'],
        'Code': ['.py', '.java', '.cpp', '.js', '.html', '.css']
    }
    
    print(" Mulai mengorganisir file...")
    
    # Loop semua file di folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Skip jika folder
        if os.path.isdir(file_path):
            continue
        
        # Ambil ekstensi file
        file_ext = os.path.splitext(filename)[1].lower()
        
        # Cari kategori yang sesuai
        moved = False
        for category, extensions in file_types.items():
            if file_ext in extensions:
                # Buat folder kategori jika belum ada
                category_path = os.path.join(folder_path, category)
                if not os.path.exists(category_path):
                    os.makedirs(category_path)
                
                # Pindahkan file
                destination = os.path.join(category_path, filename)
                
                # Jika file sudah ada, tambahkan angka
                if os.path.exists(destination):
                    base, ext = os.path.splitext(filename)
                    counter = 1
                    while os.path.exists(destination):
                        new_filename = f"{base}_{counter}{ext}"
                        destination = os.path.join(category_path, new_filename)
                        counter += 1
                
                shutil.move(file_path, destination)
                print(f"{filename} → {category}/")
                moved = True
                break
        
        # Jika tidak ada kategori yang cocok, pindah ke "Others"
        if not moved:
            others_path = os.path.join(folder_path, 'Others')
            if not os.path.exists(others_path):
                os.makedirs(others_path)
            
            destination = os.path.join(others_path, filename)
            shutil.move(file_path, destination)
            print(f"📦 {filename} → Others/")
    
    print("\n✨ Selesai! File sudah terorganisir.")

# Cara pakai
if __name__ == "__main__":
    # Ganti dengan path folder yang ingin diorganisir
    folder = r"C:\Users\Lenovo\Downloads"  # Windows
    # folder = "/Users/YourName/Downloads"    # Mac/Linux
    
    organize_files(folder)
