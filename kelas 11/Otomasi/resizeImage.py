from PIL import Image
import os

def batch_resize(input_folder, output_folder, width=800, height=600):
    """
    Resize banyak foto sekaligus
    """
    
    # Buat folder output jika belum ada
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Format gambar yang didukung
    formats = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')
    
    files = [f for f in os.listdir(input_folder) if f.lower().endswith(formats)]
    
    print(f"🖼️  Ditemukan {len(files)} gambar")
    print(f"📏 Ukuran target: {width}x{height}px\n")
    
    for filename in files:
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        
        try:
            # Buka gambar
            img = Image.open(input_path)
            
            # Resize (maintain aspect ratio)
            img.thumbnail((width, height), Image.Resampling.LANCZOS)
            
            # Save
            img.save(output_path, quality=90, optimize=True)
            
            print(f"✅ {filename} → {img.size[0]}x{img.size[1]}px")
            
        except Exception as e:
            print(f"❌ Error pada {filename}: {e}")
    
    print(f"\n✨ Selesai! Hasil disimpan di: {output_folder}")

# Cara pakai
if __name__ == "__main__":
    input_folder = r"C:\Users\Lenovo\OneDrive\Documents\materi_gonz\kelas 11\Otomasi\Images"
    output_folder = r"C:\Users\Lenovo\OneDrive\Documents\materi_gonz\kelas 11\Otomasi\Resized"
    
    batch_resize(input_folder, output_folder, width=1920, height=1080)
