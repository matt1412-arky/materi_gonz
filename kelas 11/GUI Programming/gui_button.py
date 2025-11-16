# import tkinter as tk
# from tkinter import messagebox

# window = tk.Tk()
# window.title("Aplikasi Button")
# window.geometry("400x300")

# # Fungsi yang akan dipanggil saat button diklik
# def sapa():
#     messagebox.showinfo("Pesan", "Halo! Selamat datang 😊")

# def keluar():
#     window.quit()

# # Label
# label = tk.Label(window, text="Klik tombol di bawah!", font=("Arial", 14))
# label.pack(pady=20)

# # Button
# btn_sapa = tk.Button(window, text="Sapa Saya", command=sapa, 
#                       font=("Arial", 12), bg="lightblue", width=15)
# btn_sapa.pack(pady=10)

# btn_keluar = tk.Button(window, text="Keluar", command=keluar,
#                         font=("Arial", 12), bg="lightcoral", width=15)
# btn_keluar.pack(pady=10)

# window.mainloop()

import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Aplikasi Button")
window.geometry("400x300")

# Fungsi yang akan dipanggil saat button diklik
def sapa():
    messagebox.showinfo("Pesan", "Halo! Selamat datang 😊")

def keluar():
    window.quit()

frame_tombol = tk.Frame(window, bg="#ff0000")
frame_tombol.pack(pady=20)

# Gunakan grid layout sepenuhnya
label = tk.Label(frame_tombol, text="Klik tombol di bawah!", font=("Arial", 14))
label.grid(row=0, column=0, columnspan=2, pady=20)

# Tombol 1: Sapa Saya
btn_sapa = tk.Button(frame_tombol, text="Sapa Saya", command=sapa,
                      font=("Arial", 12), bg="lightblue", width=15)
btn_sapa.grid(row=1, column=0, padx=10, pady=10)

# Tombol 2: Keluar
btn_keluar = tk.Button(frame_tombol, text="Keluar", command=keluar,
                        font=("Arial", 12), bg="lightcoral", width=15)
btn_keluar.grid(row=2, column=1, padx=10, pady=10)

window.mainloop()
