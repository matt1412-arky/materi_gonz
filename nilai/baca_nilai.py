# Program: baca_nilai.py
# Tujuan: Membaca file nilai.txt dan menampilkan data serta rata-rata nilai

def main():
    try:
        # Buka file dalam mode baca
        with open("nilai.txt", "r") as file:
            baris_data = file.readlines()

        total_nilai = 0
        jumlah_siswa = 0

        # Proses setiap baris dalam file
        for baris in baris_data:
            # Hapus newline (\n) dan pisahkan dengan koma
            nama, nilai = baris.strip().split(",")
            nilai = float(nilai)

            # Tampilkan hasil dalam format rapi
            print(f"Nama  : {nama:<6} | Nilai: {nilai:.0f}")

            total_nilai += nilai
            jumlah_siswa += 1

        # Hitung rata-rata
        if jumlah_siswa > 0:
            rata_rata = total_nilai / jumlah_siswa
            print(f"Rata-rata: {rata_rata:.2f}")
        else:
            print("Tidak ada data siswa di dalam file.")

    except FileNotFoundError:
        print("❌ File 'nilai.txt' tidak ditemukan. Pastikan file ada di folder yang sama.")
    except ValueError:
        print("⚠️ Format data salah! Pastikan setiap baris memiliki format: Nama,Nilai")

if __name__ == "__main__":
    main()
