import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Aplikasi Input Nama")
window.geometry("400x250")

# Fungsi untuk menampilkan nama
def tampilkan_nama():
    nama = entry_nama.get()  # Mengambil nilai dari entry
    
    if nama:
        messagebox.showinfo("Hasil", f"Halo, {nama}! 👋")
    else:
        messagebox.showwarning("Peringatan", "Nama tidak boleh kosong!")

# Label
label = tk.Label(window, text="Masukkan Nama Anda:", font=("Arial", 12))
label.pack(pady=20)

# Entry (kotak input)
entry_nama = tk.Entry(window, font=("Arial", 12), width=25)
entry_nama.pack(pady=10)

# Button
btn_submit = tk.Button(window, text="Submit", command=tampilkan_nama,
                        font=("Arial", 12), bg="lightgreen", width=15)
btn_submit.pack(pady=10)

window.mainloop()
