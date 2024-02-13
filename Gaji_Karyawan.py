while True:
    print("=====================================")
    print("APLIKASI PENGGAJIAN KARYAWAN PT. ILW")
    print("=====================================")

    nama = input("Masukkan Nama Karyawan: ").title()
    print("1. Direktur")
    print("2. Manager")
    print("3. Superviser")
    print("4. Operator")
    jabatan = input("Pilih Jenis Jabatan: ")

    if jabatan == "1":
        n_j = "Direktur"
        gaji_pokok = 15000000
        tunjangan = 10000000
    elif jabatan == "2":
        n_j = "Manager"
        gaji_pokok = 8000000
        tunjangan = 5000000
    elif jabatan == "3":
        n_j = "Superviser"
        gaji_pokok = 5000000
        tunjangan = 3000000
    elif jabatan == "4":
        n_j = "Operator"
        gaji_pokok = 3000000
        tunjangan = 1000000
    else:
        print("=========================")
        print("-Jabatan Tidak Tersedia-")
        print("--Mohon Ulangi Kembali--")
        print("=========================")
        print()
        continue

    hari_kerja = int(input("Masukkan Jumlah Hari Kerja: "))

    if hari_kerja <= 30:
        hari_tidakkerja = 30 - hari_kerja
        print("===============")
        print(f"Slip Gaji {nama}")
        print("===============")
        print(f"Jabatan: {n_j}")
        print(f"Gaji Pokok: Rp. {gaji_pokok}")
        total_gaji = (gaji_pokok + tunjangan + (hari_kerja * 10000)) - (hari_tidakkerja * 15000)
        print(f"Total Gaji: Rp. {total_gaji}")
        pengeluaran = float(input("Masukkan Pengeluaran Bulanan: Rp. "))
        sisa = (total_gaji-pengeluaran)
        print(f"Pengeluaran Bulanan: Rp. {sisa}")
    else:
        print("======================")
        print("---Maksimal 30 Hari---")
        print("-Mohon Ulangi Kembali-")
        print("======================")

    ulangi = str(input("Apakah Anda ingin mengulang? (Yes/No): ")).lower()
    if ulangi != "yes":
        break

