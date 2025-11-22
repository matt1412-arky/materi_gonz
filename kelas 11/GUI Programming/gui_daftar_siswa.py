import tkinter as tk              # Mengimpor library Tkinter untuk GUI
from tkinter import messagebox     # Mengimpor messagebox untuk menampilkan popup
import sqlite3                     # Mengimpor library sqlite3 untuk database

# ======================
# 1. Koneksi Database
# ======================
conn = sqlite3.connect("C:/Users/Lenovo/Materi Gonzaga/materi_gonz/kelas 11/GUI Programming/db/siswa.db")
# Membuat koneksi ke file database siswa.db, otomatis membuat file jika belum ada

cursor = conn.cursor()  
# Membuat objek cursor untuk menjalankan perintah SQL

# Buat tabel jika belum ada
cursor.execute("""
CREATE TABLE IF NOT EXISTS siswa (      # Membuat tabel siswa jika belum ada
    id INTEGER PRIMARY KEY AUTOINCREMENT,   # Kolom id sebagai primary key
    nama TEXT NOT NULL                      # Kolom nama yang tidak boleh kosong
)
""")
conn.commit()   # Menyimpan perubahan ke database

# ======================
# 2. GUI Tkinter
# ======================
window = tk.Tk()                 # Membuat window utama
window.title("Daftar Siswa")     # Judul window
window.geometry("400x450")       # Ukuran window (lebar x tinggi)

# Judul aplikasi
judul = tk.Label(window, text="📚 DAFTAR SISWA KELAS XI-A", 
                 font=("Arial", 14, "bold"))   # Membuat label judul
judul.pack(pady=10)               # Menempatkan label ke window dengan jarak atas

# Frame untuk input
frame_input = tk.Frame(window)    # Membuat frame untuk menampung form input
frame_input.pack(pady=10)         # Menempatkan frame dengan jarak

tk.Label(frame_input, text="Nama Siswa:", font=("Arial", 10)).grid(row=0, column=0, padx=5)
# Label input nama

entry_nama = tk.Entry(frame_input, font=("Arial", 10), width=20)
# Kotak input nama siswa
entry_nama.grid(row=0, column=1, padx=5)   # Posisi di grid

# ======================
# Fungsi Tambah Siswa
# ======================
def tambah_siswa():
    nama = entry_nama.get()   # Mengambil nama yang diinput

    if nama:   # Jika tidak kosong
        cursor.execute("INSERT INTO siswa (nama) VALUES (?)", (nama,))
        # Menyimpan nama ke database
        conn.commit()       # Menyimpan hasil ke file DB

        listbox.insert(tk.END, nama)    # Menambah nama ke listbox
        entry_nama.delete(0, tk.END)    # Membersihkan input
    else:
        messagebox.showwarning("Peringatan", "Nama tidak boleh kosong!")
        # Pesan peringatan jika input kosong

# ======================
# Fungsi Hapus Siswa
# ======================
def hapus_siswa():
    try:
        index = listbox.curselection()[0]   # Mendapatkan index item yang dipilih
        nama = listbox.get(index)           # Mengambil nama dari listbox

        cursor.execute("DELETE FROM siswa WHERE nama = ?", (nama,))
        # Menghapus dari database

        conn.commit()        # Simpan perubahan
        listbox.delete(index)         # Menghapus dari listbox

        messagebox.showinfo("Berhasil", f"{nama} telah dihapus!")
    except IndexError:
        messagebox.showwarning("Peringatan", "Pilih siswa yang akan dihapus!")
        # Jika tidak memilih apa-apa

# Tombol tambah
btn_tambah = tk.Button(frame_input, text="Tambah", command=tambah_siswa,
                       bg="lightgreen", width=10)
btn_tambah.grid(row=0, column=2, padx=5)      # Menempatkan tombol tambah

# Frame listbox + scrollbar
frame_list = tk.Frame(window)     # Frame untuk listbox dan scrollbar
frame_list.pack(pady=10)

scrollbar = tk.Scrollbar(frame_list)    # Membuat scrollbar
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(frame_list, font=("Arial", 11), width=35, height=12,
                     yscrollcommand=scrollbar.set)
# Listbox untuk menampilkan data siswa
listbox.pack(side=tk.LEFT)
scrollbar.config(command=listbox.yview)   # Menghubungkan scrollbar ke listbox

# ======================
# Load data dari database
# ======================
cursor.execute("SELECT nama FROM siswa ORDER BY id")   # Mengambil semua nama
for row in cursor.fetchall():       # Loop setiap data
    listbox.insert(tk.END, row[0])  # Menampilkan ke listbox

# Tombol hapus
btn_hapus = tk.Button(window, text="Hapus Siswa Terpilih", command=hapus_siswa,
                      bg="lightcoral", font=("Arial", 10), width=20)
btn_hapus.pack(pady=10)

window.mainloop()    # Menjalankan GUI Tkinter

# Tutup koneksi saat aplikasi ditutup
conn.close()
