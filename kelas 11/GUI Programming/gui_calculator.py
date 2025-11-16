import tkinter as tk
from tkinter import messagebox

class Kalkulator:
    def __init__(self, window):
        self.window = window
        self.window.title("Kalkulator Sederhana")
        self.window.geometry("400x400")
        self.window.configure(bg="#f0f0f0")
        
        # Judul
        judul = tk.Label(window, text="🧮 KALKULATOR", 
                         font=("Arial", 20, "bold"), bg="#f0f0f0")
        judul.pack(pady=20)
        
        # Frame untuk input
        frame_input = tk.Frame(window, bg="#3104f8")
        frame_input.pack(pady=10)
        
        # Input angka pertama
        tk.Label(frame_input, text="Angka 1:", font=("Arial", 12), 
                bg="#f0f0f0").grid(row=0, column=0, padx=5, pady=5)
        self.entry_angka1 = tk.Entry(frame_input, font=("Arial", 12), width=15)
        self.entry_angka1.grid(row=0, column=1, padx=5, pady=5)
        
        # Input angka kedua
        tk.Label(frame_input, text="Angka 2:", font=("Arial", 12),
                bg="#f0f0f0").grid(row=1, column=0, padx=5, pady=5)
        self.entry_angka2 = tk.Entry(frame_input, font=("Arial", 12), width=15)
        self.entry_angka2.grid(row=1, column=1, padx=5, pady=5)
        
        # Frame untuk tombol operasi
        frame_tombol = tk.Frame(window, bg="#ff0000")
        frame_tombol.pack(pady=20)
        
        # Tombol operasi
        btn_tambah = tk.Button(frame_tombol, text="+", command=self.tambah,
                               font=("Arial", 16, "bold"), bg="#90EE90", width=5, height=2)
        btn_tambah.grid(row=0, column=0, padx=5, pady=5)
        
        btn_kurang = tk.Button(frame_tombol, text="-", command=self.kurang,
                               font=("Arial", 16, "bold"), bg="#FFB6C1", width=5, height=2)
        btn_kurang.grid(row=0, column=1, padx=5, pady=5)
        
        btn_kali = tk.Button(frame_tombol, text="×", command=self.kali,
                            font=("Arial", 16, "bold"), bg="#87CEEB", width=5, height=2)
        btn_kali.grid(row=1, column=0, padx=5, pady=5)
        
        btn_bagi = tk.Button(frame_tombol, text="÷", command=self.bagi,
                            font=("Arial", 16, "bold"), bg="#FFD700", width=5, height=2)
        btn_bagi.grid(row=1, column=1, padx=5, pady=5)
        
        # Label hasil
        self.label_hasil = tk.Label(window, text="Hasil: -", 
                                    font=("Arial", 16, "bold"), 
                                    bg="#f0f0f0", fg="blue")
        self.label_hasil.pack(pady=20)
    
    def get_angka(self):
        """Mengambil nilai dari entry dan validasi"""
        try:
            angka1 = float(self.entry_angka1.get())
            angka2 = float(self.entry_angka2.get())
            return angka1, angka2
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid!")
            return None, None
    
    def tambah(self):
        angka1, angka2 = self.get_angka()
        if angka1 is not None:
            hasil = angka1 + angka2
            self.label_hasil.config(text=f"Hasil: {hasil}")
    
    def kurang(self):
        angka1, angka2 = self.get_angka()
        if angka1 is not None:
            hasil = angka1 - angka2
            self.label_hasil.config(text=f"Hasil: {hasil}")
    
    def kali(self):
        angka1, angka2 = self.get_angka()
        if angka1 is not None:
            hasil = angka1 * angka2
            self.label_hasil.config(text=f"Hasil: {hasil}")
    
    def bagi(self):
        angka1, angka2 = self.get_angka()
        if angka1 is not None:
            if angka2 != 0:
                hasil = angka1 / angka2
                self.label_hasil.config(text=f"Hasil: {hasil:.2f}")
            else:
                messagebox.showerror("Error", "Tidak bisa dibagi dengan nol!")

# Main program
if __name__ == "__main__":
    window = tk.Tk()
    app = Kalkulator(window)
    window.mainloop()