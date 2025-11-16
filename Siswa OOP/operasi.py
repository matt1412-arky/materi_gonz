from siswa import Siswa
from guru import Guru
from nilai import Nilai
from mapel import MataPelajaran
import json

# List data
data_siswa = []
data_guru = []
data_mapel = []
data_nilai = []

# ===============================
# UTIL
# ===============================
def input_non_kosong(pesan):
    """Minta input yang tidak boleh kosong"""
    while True:
        data = input(pesan).strip()
        if data != "":
            return data
        print("⚠️ Input tidak boleh kosong!")

# ===============================
# SISWA
# ===============================
def tambah_siswa():
    print("\n=== TAMBAH SISWA BARU ===")
    nama = input_non_kosong("Masukkan nama: ")
    kelas = input_non_kosong("Masukkan kelas: ")
    siswa_baru = Siswa(nama, kelas)
    data_siswa.append(siswa_baru)
    print(f"✅ Siswa {nama} berhasil ditambahkan!")

def tampilkan_siswa():
    print("\n=== DAFTAR SISWA ===")
    if not data_siswa:
        print("📝 Belum ada data siswa")
        return
    for i, siswa in enumerate(data_siswa, 1):
        print(f"{i}. ", end=""); siswa.info()

def edit_siswa():
    print("\n=== EDIT SISWA ===")
    if not data_siswa:
        print("📝 Belum ada data siswa untuk diedit")
        return
    tampilkan_siswa()
    try:
        nomor = int(input("\nMasukkan nomor siswa yang ingin diedit: "))
        if 1 <= nomor <= len(data_siswa):
            siswa = data_siswa[nomor - 1]
            nama_baru = input("Nama baru (kosongkan jika tidak mengubah): ")
            kelas_baru = input("Kelas baru (kosongkan jika tidak mengubah): ")
            if nama_baru.strip(): siswa.nama = nama_baru
            if kelas_baru.strip(): siswa.kelas = kelas_baru
            print("✅ Data siswa berhasil diperbarui!")
        else:
            print("❌ Nomor tidak valid!")
    except ValueError:
        print("❌ Masukkan nomor yang benar!")

def hapus_siswa():
    print("\n=== HAPUS SISWA ===")
    if not data_siswa:
        print("📝 Belum ada data siswa")
        return
    tampilkan_siswa()
    try:
        nomor = int(input("\nMasukkan nomor siswa yang ingin dihapus: "))
        if 1 <= nomor <= len(data_siswa):
            siswa_terhapus = data_siswa.pop(nomor - 1)
            print(f"✅ Siswa {siswa_terhapus.nama} berhasil dihapus!")
        else:
            print("❌ Nomor tidak valid!")
    except ValueError:
        print("❌ Masukkan nomor yang benar!")

def cari_siswa():
    print("\n=== CARI SISWA ===")
    if not data_siswa:
        print("📝 Belum ada data siswa")
        return
    nama_cari = input("Masukkan nama yang dicari: ").lower()
    ditemukan = False
    for i, siswa in enumerate(data_siswa, 1):
        if nama_cari in siswa.nama.lower():
            print(f"{i}. ", end=""); siswa.info()
            ditemukan = True
    if not ditemukan:
        print("❌ Siswa tidak ditemukan!")

# ===============================
# GURU
# ===============================
def tambah_guru():
    print("\n=== TAMBAH GURU ===")
    nama = input_non_kosong("Masukkan nama guru: ")
    mapel = input_non_kosong("Masukkan mata pelajaran: ")
    guru_baru = Guru(nama, mapel)
    data_guru.append(guru_baru)
    print(f"✅ Guru {nama} berhasil ditambahkan!")

def tampilkan_guru():
    print("\n=== DAFTAR GURU ===")
    if not data_guru:
        print("📝 Belum ada data guru")
        return
    for i, guru in enumerate(data_guru, 1):
        print(f"{i}. ", end=""); guru.info()

def edit_guru():
    print("\n=== EDIT GURU ===")
    if not data_guru:
        print("📝 Belum ada data guru untuk diedit")
        return
    tampilkan_guru()
    try:
        nomor = int(input("\nMasukkan nomor guru yang ingin diedit: "))
        if 1 <= nomor <= len(data_guru):
            guru = data_guru[nomor - 1]
            nama_baru = input("Nama baru (kosongkan jika tidak mengubah): ")
            mapel_baru = input("Mapel baru (kosongkan jika tidak mengubah): ")
            if nama_baru.strip(): guru.nama = nama_baru
            if mapel_baru.strip(): guru.mapel = mapel_baru
            print("✅ Data guru berhasil diperbarui!")
        else:
            print("❌ Nomor tidak valid!")
    except ValueError:
        print("❌ Masukkan nomor yang benar!")

def hapus_guru():
    print("\n=== HAPUS GURU ===")
    if not data_guru:
        print("📝 Belum ada data guru")
        return
    tampilkan_guru()
    try:
        nomor = int(input("\nMasukkan nomor guru yang ingin dihapus: "))
        if 1 <= nomor <= len(data_guru):
            guru_terhapus = data_guru.pop(nomor - 1)
            print(f"✅ Guru {guru_terhapus.nama} berhasil dihapus!")
        else:
            print("❌ Nomor tidak valid!")
    except ValueError:
        print("❌ Masukkan nomor yang benar!")

def cari_guru():
    print("\n=== CARI GURU ===")
    if not data_guru:
        print("📝 Belum ada data guru")
        return
    nama_cari = input("Masukkan nama guru yang dicari: ").lower()
    ditemukan = False
    for i, guru in enumerate(data_guru, 1):
        if nama_cari in guru.nama.lower():
            print(f"{i}. ", end=""); guru.info()
            ditemukan = True
    if not ditemukan:
        print("❌ Guru tidak ditemukan!")

# ===============================
# MAPEL
# ===============================
def tambah_mapel():
    print("\n=== TAMBAH MATA PELAJARAN ===")
    nama = input_non_kosong("Masukkan nama mapel: ")
    kode = input_non_kosong("Masukkan kode mapel: ")
    mapel_baru = MataPelajaran(nama, kode)
    data_mapel.append(mapel_baru)
    print(f"✅ Mapel {nama} berhasil ditambahkan!")

def tampilkan_mapel():
    print("\n=== DAFTAR MATA PELAJARAN ===")
    if not data_mapel:
        print("📝 Belum ada data mapel")
        return
    for i, mapel in enumerate(data_mapel, 1):
        print(f"{i}. ", end=""); mapel.info()

def edit_mapel():
    print("\n=== EDIT MAPEL ===")
    if not data_mapel:
        print("📝 Belum ada data mapel untuk diedit")
        return
    tampilkan_mapel()
    try:
        nomor = int(input("\nMasukkan nomor mapel yang ingin diedit: "))
        if 1 <= nomor <= len(data_mapel):
            mapel = data_mapel[nomor - 1]
            nama_baru = input("Nama baru (kosongkan jika tidak mengubah): ")
            kode_baru = input("Kode baru (kosongkan jika tidak mengubah): ")
            if nama_baru.strip(): mapel.nama = nama_baru
            if kode_baru.strip(): mapel.kode = kode_baru
            print("✅ Data mapel berhasil diperbarui!")
        else:
            print("❌ Nomor tidak valid!")
    except ValueError:
        print("❌ Masukkan nomor yang benar!")

def hapus_mapel():
    print("\n=== HAPUS MAPEL ===")
    if not data_mapel:
        print("📝 Belum ada data mapel")
        return
    tampilkan_mapel()
    try:
        nomor = int(input("\nMasukkan nomor mapel yang ingin dihapus: "))
        if 1 <= nomor <= len(data_mapel):
            mapel_terhapus = data_mapel.pop(nomor - 1)
            print(f"✅ Mapel {mapel_terhapus.nama} berhasil dihapus!")
        else:
            print("❌ Nomor tidak valid!")
    except ValueError:
        print("❌ Masukkan nomor yang benar!")

def cari_mapel():
    print("\n=== CARI MAPEL ===")
    if not data_mapel:
        print("📝 Belum ada data mapel")
        return
    nama_cari = input("Masukkan nama mapel yang dicari: ").lower()
    ditemukan = False
    for i, mapel in enumerate(data_mapel, 1):
        if nama_cari in mapel.nama.lower():
            print(f"{i}. ", end=""); mapel.info()
            ditemukan = True
    if not ditemukan:
        print("❌ Mapel tidak ditemukan!")

# ===============================
# NILAI
# ===============================
def tambah_nilai():
    print("\n=== INPUT NILAI SISWA ===")
    if not data_siswa or not data_mapel:
        print("⚠️ Tambahkan siswa dan mapel terlebih dahulu!")
        return
    tampilkan_siswa()
    try:
        no_siswa = int(input("Pilih nomor siswa: "))
        siswa = data_siswa[no_siswa - 1]
    except (ValueError, IndexError):
        print("❌ Pilihan siswa tidak valid!")
        return
    tampilkan_mapel()
    try:
        no_mapel = int(input("Pilih nomor mapel: "))
        mapel = data_mapel[no_mapel - 1]
    except (ValueError, IndexError):
        print("❌ Pilihan mapel tidak valid!")
        return
    try:
        nilai = float(input("Masukkan nilai: "))
    except ValueError:
        print("❌ Nilai harus berupa angka!")
        return
    nilai_baru = Nilai(siswa, mapel, nilai)
    data_nilai.append(nilai_baru)
    print(f"✅ Nilai {siswa.nama} untuk {mapel.nama} berhasil ditambahkan!")

def tampilkan_nilai():
    print("\n=== DAFTAR NILAI SISWA ===")
    if not data_nilai:
        print("📝 Belum ada data nilai")
        return
    for i, n in enumerate(data_nilai, 1):
        print(f"{i}. ", end=""); n.info()

def edit_nilai():
    print("\n=== EDIT NILAI ===")
    if not data_nilai:
        print("📝 Belum ada data nilai untuk diedit")
        return
    tampilkan_nilai()
    try:
        nomor = int(input("\nMasukkan nomor nilai yang ingin diedit: "))
        if 1 <= nomor <= len(data_nilai):
            nilai = data_nilai[nomor - 1]
            try:
                nilai_baru = float(input("Masukkan nilai baru: "))
                nilai.nilai = nilai_baru
                print("✅ Data nilai berhasil diperbarui!")
            except ValueError:
                print("❌ Nilai harus angka!")
        else:
            print("❌ Nomor tidak valid!")
    except ValueError:
        print("❌ Masukkan nomor yang benar!")

def hapus_nilai():
    print("\n=== HAPUS NILAI ===")
    if not data_nilai:
        print("📝 Belum ada data nilai")
        return
    tampilkan_nilai()
    try:
        nomor = int(input("\nMasukkan nomor nilai yang ingin dihapus: "))
        if 1 <= nomor <= len(data_nilai):
            nilai_terhapus = data_nilai.pop(nomor - 1)
            print(f"✅ Nilai {nilai_terhapus.siswa.nama} berhasil dihapus!")
        else:
            print("❌ Nomor tidak valid!")
    except ValueError:
        print("❌ Masukkan nomor yang benar!")

def cari_nilai():
    print("\n=== CARI NILAI SISWA ===")
    if not data_nilai:
        print("📝 Belum ada data nilai")
        return
    nama_cari = input("Masukkan nama siswa yang dicari: ").lower()
    ditemukan = False
    for i, n in enumerate(data_nilai, 1):
        if nama_cari in n.siswa.nama.lower():
            print(f"{i}. ", end=""); n.info()
            ditemukan = True
    if not ditemukan:
        print("❌ Nilai untuk siswa tersebut tidak ditemukan!")

# ===============================
# SIMPAN & LOAD
# ===============================
def simpan_data(filename="data.json"):
    """Simpan semua data ke file JSON"""
    with open(filename, "w") as f:
        json.dump({
            "siswa": [{"nama": s.nama, "kelas": s.kelas} for s in data_siswa],
            "guru": [{"nama": g.nama, "mapel": g.mapel} for g in data_guru],
            "mapel": [{"nama": m.nama, "kode": m.kode} for m in data_mapel],
            "nilai": [{"siswa": n.siswa.nama, "mapel": n.mapel.nama, "nilai": n.nilai} for n in data_nilai]
        }, f, indent=4)
    print(f"💾 Semua data berhasil disimpan ke {filename}")

def load_data(filename="data.json"):
    """Load semua data dari file JSON"""
    global data_siswa, data_guru, data_mapel, data_nilai
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            data_siswa = [Siswa(d["nama"], d["kelas"]) for d in data.get("siswa", [])]
            data_guru = [Guru(d["nama"], d["mapel"]) for d in data.get("guru", [])]
            data_mapel = [MataPelajaran(d["nama"], d["kode"]) for d in data.get("mapel", [])]
            # nilai tricky, kita simpan hanya nama & mapel
            data_nilai = []  
            for d in data.get("nilai", []):
                siswa_obj = next((s for s in data_siswa if s.nama == d["siswa"]), None)
                mapel_obj = next((m for m in data_mapel if m.nama == d["mapel"]), None)
                if siswa_obj and mapel_obj:
                    data_nilai.append(Nilai(siswa_obj, mapel_obj, d["nilai"]))
        print(f"📂 Semua data berhasil dimuat dari {filename}")
    except FileNotFoundError:
        print("⚠️ File data belum ada, mulai dengan data kosong.")
    except json.JSONDecodeError:
        print("❌ Gagal memuat data, format file tidak valid.")