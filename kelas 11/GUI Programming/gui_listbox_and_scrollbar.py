import tkinter as tk
from tkinter import messagebox

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

# Fungsi untuk menambah siswa
def tambah_siswa():
    nama = entry_nama.get()
    if nama:
        listbox.insert(tk.END, nama)  # Menambah ke akhir list
        entry_nama.delete(0, tk.END)  # Kosongkan entry
    else:
        messagebox.showwarning("Peringatan", "Nama tidak boleh kosong!")

# Fungsi untuk menghapus siswa yang dipilih
def hapus_siswa():
    try:
        index = listbox.curselection()[0]  # Ambil index yang dipilih
        nama = listbox.get(index)
        listbox.delete(index)
        messagebox.showinfo("Berhasil", f"{nama} telah dihapus!")
    except IndexError:
        messagebox.showwarning("Peringatan", "Pilih siswa yang akan dihapus!")

# Tombol
btn_tambah = tk.Button(frame_input, text="Tambah", command=tambah_siswa,
                       bg="lightgreen", width=10)
btn_tambah.grid(row=0, column=2, padx=5)

# Frame untuk listbox
frame_list = tk.Frame(window)
frame_list.pack(pady=10)

# Scrollbar
scrollbar = tk.Scrollbar(frame_list)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Listbox
listbox = tk.Listbox(frame_list, font=("Arial", 11), width=35, height=12,
                     yscrollcommand=scrollbar.set)
listbox.pack(side=tk.LEFT)
scrollbar.config(command=listbox.yview)

# Data awal
daftar_awal = ["Ali Rahman", "Budi Santoso", "Citra Dewi", "Dina Maharani"]
for siswa in daftar_awal:
    listbox.insert(tk.END, siswa)

# Tombol hapus
btn_hapus = tk.Button(window, text="Hapus Siswa Terpilih", command=hapus_siswa,
                      bg="lightcoral", font=("Arial", 10), width=20)
btn_hapus.pack(pady=10)

window.mainloop()
