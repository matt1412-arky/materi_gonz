import tkinter as tk

window = tk.Tk()
window.title("Aplikasi Label")
window.geometry("400x300")

# Membuat label
label1 = tk.Label(window, text="Selamat Datang!", font=("Arial", 20, "bold"))
label1.pack(pady=20)  # pady = jarak atas-bawah

label2 = tk.Label(window, text="Ini adalah program GUI pertamaku", 
                  font=("Arial", 12), fg="blue")  # fg = warna text
label2.pack()

window.mainloop()
