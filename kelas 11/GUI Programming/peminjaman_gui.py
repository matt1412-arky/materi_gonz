import tkinter as tk
from tkinter import messagebox
import sqlite3

# ==========================
# 1. KONEKSI DATABASE
# ==========================

conn = sqlite3.connect("C:/Users/Lenovo/Materi Gonzaga/materi_gonz/kelas 11/GUI Programming/db/perpustakaan.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS peminjaman (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama TEXT NOT NULL,
    judul TEXT NOT NULL
)
""")
conn.commit()

# ==========================
# 2. GUI TKINTER
# ==========================

window = tk.Tk()
window.title("Aplikasi Peminjaman Buku")
window.geometry("450x500")

# Judul
label_judul = tk.Label(window, text="📚 APLIKASI PEMINJAMAN BUKU",
                       font=("Arial", 14, "bold"))
label_judul.pack(pady=10)

# Frame Input
frame_input = tk.Frame(window)
frame_input.pack(pady=10)

# Label + Entry Nama
tk.Label(frame_input, text="Nama Peminjam:", font=("Arial", 11)).grid(row=0, column=0, padx=5, pady=5)
entry_nama = tk.Entry(frame_input, width=25, font=("Arial", 11))
entry_nama.grid(row=0, column=1, padx=5)

# Label + Entry Judul
tk.Label(frame_input, text="Judul Buku:", font=("Arial", 11)).grid(row=1, column=0, padx=5, pady=5)
entry_judul = tk.Entry(frame_input, width=25, font=("Arial", 11))
entry_judul.grid(row=1, column=1, padx=5)

# ==========================
# 3. FUNGSI
# ==========================

# Simpan Data
def simpan_data():
    nama = entry_nama.get()
    judul = entry_judul.get()

    if nama == "" or judul == "":
        messagebox.showwarning("Peringatan", "Semua field harus diisi!")
        return

    cursor.execute("INSERT INTO peminjaman (nama, judul) VALUES (?, ?)", (nama, judul))
    conn.commit()

    messagebox.showinfo("Berhasil", "Data berhasil disimpan!")
    entry_nama.delete(0, tk.END)
    entry_judul.delete(0, tk.END)
    lihat_data()  # refresh listbox

# Lihat Data
def lihat_data():
    listbox.delete(0, tk.END)
    cursor.execute("SELECT id, nama, judul FROM peminjaman")
    rows = cursor.fetchall()

    for row in rows:
        listbox.insert(tk.END, f"{row[0]}. {row[1]} - {row[2]}")

# Hapus Data
def hapus_data():
    try:
        selected = listbox.curselection()[0]
        data = listbox.get(selected)

        id_data = data.split(".")[0]  # Ambil ID sebelum titik

        cursor.execute("DELETE FROM peminjaman WHERE id = ?", (id_data,))
        conn.commit()

        messagebox.showinfo("Berhasil", "Data berhasil dihapus!")
        lihat_data()

    except:
        messagebox.showwarning("Peringatan", "Pilih data yang akan dihapus!")


# ==========================
# 4. BUTTON
# ==========================

btn_simpan = tk.Button(window, text="Simpan", command=simpan_data,
                       width=15, bg="lightgreen", font=("Arial", 11))
btn_simpan.pack(pady=5)

btn_lihat = tk.Button(window, text="Lihat Data", command=lihat_data,
                      width=15, bg="lightblue", font=("Arial", 11))
btn_lihat.pack(pady=5)

btn_hapus = tk.Button(window, text="Hapus", command=hapus_data,
                      width=15, bg="lightcoral", font=("Arial", 11))
btn_hapus.pack(pady=5)

# ==========================
# 5. LISTBOX + SCROLLBAR
# ==========================

frame_list = tk.Frame(window)
frame_list.pack(pady=10)

scrollbar = tk.Scrollbar(frame_list)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(frame_list, width=40, height=15, font=("Arial", 11),
                     yscrollcommand=scrollbar.set)
listbox.pack()

scrollbar.config(command=listbox.yview)

# Load awal
lihat_data()

window.mainloop()

# Tutup koneksi
conn.close()
