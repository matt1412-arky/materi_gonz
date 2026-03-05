from PIL import Image, ImageDraw, ImageFont
import os

def add_watermark(input_folder, output_folder, watermark_text="© 2026"):
    
    # Tambah watermark ke banyak foto
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    formats = (".jpg", ".jpeg", ".png")
    files = [f for f in os.listdir(input_folder) if f.lower().endswith(formats)]

    print(f"📂 Menambah watermark ke {len(files)} gambar")
    print(f"🔖 Watermark: '{watermark_text}'\n")

    for filename in files:
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        try:
            # Buka gambar
            img = Image.open(input_path)
            width, height = img.size

            # Buat layer untuk watermark
            draw = ImageDraw.Draw(img)

            # Font (gunakan font default jika tidak ada)
            try:
                font = ImageFont.truetype("arial.ttf", int(width * 0.03))
            except:
                font = ImageFont.load_default()

            # Hitung posisi (kanan bawah)
            text_bbox = draw.textbbox((0, 0), watermark_text, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]

            margin = 20
            x = width - text_width - margin
            y = height - text_height - margin

            # Tambahkan shadow
            shadow_offset = 2
            draw.text(
                (x + shadow_offset, y + shadow_offset),
                watermark_text,
                font=font,
                fill=(0, 0, 0, 128)
            )

            # Tambahkan watermark
            draw.text(
                (x, y),
                watermark_text,
                font=font,
                fill=(255, 255, 255, 200)
            )

            # Save
            img.save(output_path, quality=95)
            print(f"✔ {filename}")

        except Exception as e:
            print(f"❌ Error pada {filename}: {e}")

    print(f"\n✨ Selesai! Hasil disimpan di: {output_folder}")


# Cara pakai
input_folder = r"C:\Users\Lenovo\OneDrive\Documents\materi_gonz\kelas 11\Otomasi\Images"
output_folder = r"C:\Users\Lenovo\OneDrive\Documents\materi_gonz\kelas 11\Otomasi\Watermarked"

add_watermark(input_folder, output_folder, watermark_text="© SMA Ku 2026")