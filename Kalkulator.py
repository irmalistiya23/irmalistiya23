print("Calkulator Sederhana")
angka1 = int(input("Masukkan Angka Pertama "))
angka2 = int(input("Masukkan Angka Kedua "))
print("Pilih Operasi")
operasi = input("Masukkan Operasi (+, -, *, /) ")
if operasi == '+':
    hitung = int(angka1) + int(angka2)
    print(f"Hasil: {hitung}")
elif operasi == '-':
    hitung = int(angka1) - int(angka2)
    print(f"Hasil: {hitung}")
elif operasi == '*':
    hitung = int(angka1) * int(angka2)
    print(f"Hasil: {hitung}")
elif operasi == '/':
        if angka2 != 0:
            hitung = int(angka1) / int(angka2)
            print(f"Hasil: {hitung}")
        else:
            print("Angka Tidak Valid")
