def penjumlahan(a, b):
    return a + b

def pengurangan(a,b):
    return a - b

def perkalian(a,b):
    if a != 0 and b != 0:
        return a * b
    else :
        return 0

def pembagian (a,b):
    if a != 0 and b != 0:
        return a / b
    else:
        return "Error: Pembagian dengan nol tidak diperbolehkan."    
 
while True:
    print("\n====Kalkulator Sederhana====")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Keluar")
    pilihan = input("Pilih menu (1-5): ")

    if pilihan =="1":
        a = int(input("Masukkan angka pertama: "))
        b = int(input("Masukkan angka kedua: "))
        print (f"Hasil penjumlahan: " + str(penjumlahan(a, b)))
    elif pilihan =="2":
        a = int(input("Masukkan angka pertama: "))
        b = int(input("Masukkan angka kedua: "))
        print (f"Hasil pengurangan: " + str(pengurangan(a, b)))
    elif pilihan =="3":
        a = int(input("Masukkan angka pertama: "))
        b = int(input("Masukkan angka kedua: "))
        print (f"Hasil perkalian: " + str(perkalian(a, b)))
    elif pilihan =="4":
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        print (f"Hasil pembagian: " + str(pembagian(a, b)))
    elif pilihan =="5":
        print("Terima kasih telah menggunakan kalkulator sederhana!")
        break
    else:
        print("Menu tidak valid, silakan coba lagi.")