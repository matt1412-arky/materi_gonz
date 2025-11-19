import tkinter as tk
from tkinter import messagebox
import sqlite3

# ======================
# 1. Koneksi Database
# ======================
conn = sqlite3.connect("C:/Users/Lenovo/Materi Gonzaga/materi_gonz/kelas 11/GUI Programming/db/siswa.db")
cursor = conn.cursor()

# Buat tabel jika belum ada
cursor.execute("""
CREATE TABLE IF NOT EXISTS siswa (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama TEXT NOT NULL
)
""")
conn.commit()

# ======================
# 2. GUI Tkinter
# ======================
window = tk.Tk()
window.title("Daftar Siswa")
window.geometry("400x450")

# Judul
judul = tk.Label(window, text="📚 DAFTAR SISWA KELAS XI-A", 
                 font=("Arial", 14, "bold"))
judul.pack(pady=10)

# Frame untuk input
frame_input = tk.Frame(window)
frame_input.pack(pady=10)

tk.Label(frame_input, text="Nama Siswa:", font=("Arial", 10)).grid(row=0, column=0, padx=5)
entry_nama = tk.Entry(frame_input, font=("Arial", 10), width=20)
entry_nama.grid(row=0, column=1, padx=5)

# ======================
# Fungsi Tambah Siswa
# ======================
def tambah_siswa():
    nama = entry_nama.get()
    if nama:
        # Simpan ke database
        cursor.execute("INSERT INTO siswa (nama) VALUES (?)", (nama,))
        conn.commit()

        # Tambahkan ke listbox
        listbox.insert(tk.END, nama)
        entry_nama.delete(0, tk.END)
    else:
        messagebox.showwarning("Peringatan", "Nama tidak boleh kosong!")

# ======================
# Fungsi Hapus Siswa
# ======================
def hapus_siswa():
    try:
        index = listbox.curselection()[0]
        nama = listbox.get(index)

        # Hapus dari database
        cursor.execute("DELETE FROM siswa WHERE nama = ?", (nama,))
        conn.commit()

        # Hapus dari listbox
        listbox.delete(index)

        messagebox.showinfo("Berhasil", f"{nama} telah dihapus!")
    except IndexError:
        messagebox.showwarning("Peringatan", "Pilih siswa yang akan dihapus!")

# Tombol tambah
btn_tambah = tk.Button(frame_input, text="Tambah", command=tambah_siswa,
                       bg="lightgreen", width=10)
btn_tambah.grid(row=0, column=2, padx=5)

# Frame listbox + scrollbar
frame_list = tk.Frame(window)
frame_list.pack(pady=10)

scrollbar = tk.Scrollbar(frame_list)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(frame_list, font=("Arial", 11), width=35, height=12,
                     yscrollcommand=scrollbar.set)
listbox.pack(side=tk.LEFT)
scrollbar.config(command=listbox.yview)

# ======================
# Load data dari database
# ======================
cursor.execute("SELECT nama FROM siswa ORDER BY id")
for row in cursor.fetchall():
    listbox.insert(tk.END, row[0])

# Tombol hapus
btn_hapus = tk.Button(window, text="Hapus Siswa Terpilih", command=hapus_siswa,
                      bg="lightcoral", font=("Arial", 10), width=20)
btn_hapus.pack(pady=10)

window.mainloop()

# Tutup koneksi saat aplikasi ditutup
conn.close()
