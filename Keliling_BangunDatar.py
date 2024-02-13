phi = 3.14
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("--Hitung Keliling Bangun Datar--")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print()
print("Lihat Bangun Datar Berikut")
print("1. Persegi")
print("2. Persegi Panjang")
print("3. Lingkaran")
print("4. Segitiga")
print("5. Trapesium")
print("6. Jajar Genjang")
print("7. Belah Ketupat")
print("8. Layang-Layang")
pilih = (input("Masukkan Pilihan Anda: "))
if pilih == "1":
    n_b = "Persegi"
    sisi = float(input("Masukkan Sisi: "))
    rumus = (4*sisi)
elif pilih == "2":
    n_b = "Persegi Panjang"
    panjang = float(input("Masukkan Panjang: "))
    lebar = float(input("Masukkan Lebar: "))
    rumus = (2*(panjang+lebar))
elif pilih == "3":
    n_b = "Lingkaran"
    jr = float(input("Masukkan Jari-jari: "))
    rumus = (2*phi*jr)
elif pilih == "4":
    n_b = "Segitiga"
    sisi1 = float(input("Masukkan Sisi1: "))
    sisi2 = float(input("Masukkan Sisi2: "))
    sisi3 = float(input("Masukkan Sisi3: "))
    rumus = (sisi1+sisi2+sisi3)
elif pilih == "5":
    n_b = "Trapesium"
    AB = float(input("Masukkan AB: "))
    BC = float(input("Masukkan BC: "))
    CD = float(input("Masukkan CD: "))
    AD = float(input("Masukkan AD: "))
    rumus = (AB + BC + CD + AD)
elif pilih == "6":
    n_b = "Jajar Genjang"
    sisi1 = float(input("Masukkan Sisi1: "))
    sisi2 = float(input("Masukkan Sisi2: "))
    rumus = (2*(sisi1+sisi2))
elif pilih == "7":
    n_b = "Belah Ketupat"
    sisi = float(input("Masukkan Sisi: "))
    rumus = (4*sisi)
elif pilih == "8":
    n_b = "Layang-layang"
    sisi1 = float(input("Masukkan Sisi1: "))
    sisi2 = float(input("Masukkan Sisi2: "))
    rumus = (2*(sisi1+sisi2))
else:
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("--Bangun Datar Tidak Tersedia--")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    exit()
    
print(f"Keliling Bangun Datar {n_b} adalah: {rumus}")
