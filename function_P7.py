print("=" * 50)

def biodata():
    print("Nama: Ahmad Fauzi")
    print("Kelas: 11 IPA 2")
    print("Hobi: Membaca dan Coding")

biodata()

print("=" * 50)

def luas_persegi(sisi):
    luas = sisi * sisi
    return luas

# Test
print("Luas Persegi: " + str(luas_persegi(5)))  # Output: 25

print("=" * 50)

def nilai_akhir(tugas, uts, uas):
    na = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)
    return na

# Test
print("Nilai Akhir : " + str(nilai_akhir(85, 80, 90)))  # Output: 85.25

print("=" * 50)

def grade(nilai):
    if nilai >= 90:
        return "A"
    elif nilai >= 80:
        return "B"
    elif nilai >= 70:
        return "C"
    elif nilai >= 60:
        return "D"
    else:
        return "E"

# Test
print("Grade: " + grade(85))  # Output: B

print("=" * 50)

def cari_maksimal(angka_list):
    if len(angka_list) == 0:
        return None
    
    maksimal = angka_list[0]
    for angka in angka_list:
        if angka > maksimal:
            maksimal = angka
    return maksimal

# Test
data = [23, 45, 12, 78, 34]
print("Nilai Maksimal: " + str(cari_maksimal(data)))  # Output: 78

print("=" * 50)