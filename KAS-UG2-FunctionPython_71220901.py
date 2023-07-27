import math
print ("==================== KALKULATOR CERDAS ====================")
print("Pilihlah bangun yang ingin anda hitung (input angka saja)")
print("1. Tabung")
print("2. Kubus")
print("3. Balok")

# Fungsi menghitung Volume Tabung
def volume_tabung(jari_jari, tinggi):
    return math.pi * jari_jari **2 * tinggi

# Fungsi menghitung volume kubus
def volume_kubus(sisi):
    return sisi**3

# Fungsi menghitung volume balok
def volume_balok(panjang, lebar, tinggi):
    return panjang * lebar * tinggi

pilihan = int(input("Masukkan pilihan (1/2/3): "))

if pilihan == 1:
        r = float(input("Masukkan diameter (cm): "))
        h = float(input("Masukkan tinggi (cm): "))
        print("Volume tabung adalah :", volume_tabung(r, h), "cm")
elif pilihan == 2:
    s = float(input("Masukkan sisi (cm): "))
    print("Volume kubus adalah :", volume_kubus(s), "cm")
elif pilihan == 3:
        p = float(input("Masukkan panjang (cm): "))
        l = float(input("Masukkan lebar (cm): "))
        t = float(input("Masukkan tinggi (cm): "))
        print("Volume balok:", volume_balok(p, l, t), "cm")
else:
        print("Inputan yang anda masukkan salah !!!")

