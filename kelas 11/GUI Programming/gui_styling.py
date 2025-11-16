import tkinter as tk

window = tk.Tk()
window.title("Palet Warna")
window.geometry("500x400")

colors = [
    ("Red", "#FF0000"),
    ("Green", "#00FF00"),
    ("Blue", "#0000FF"),
    ("Yellow", "#FFFF00"),
    ("Orange", "#FFA500"),
    ("Purple", "#800080"),
    ("Pink", "#FFC0CB"),
    ("Cyan", "#00FFFF")
]

row = 0
col = 0

for nama, kode in colors:
    frame = tk.Frame(window, bg=kode, width=120, height=80)
    frame.grid(row=row, column=col, padx=5, pady=5)
    
    label = tk.Label(frame, text=f"{nama}\n{kode}", 
                     bg=kode, font=("Arial", 10, "bold"))
    label.pack(expand=True)
    
    col += 1
    if col > 3:
        col = 0
        row += 1

window.mainloop()
