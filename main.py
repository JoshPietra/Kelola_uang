import json
import os
from datetime import datetime

saldo = 0
riwayat = []
file_saldo = "saldo.json"

def simpan_saldo():
    with open(file_saldo, "w") as f:
        json.dump({"saldo": saldo, "riwayat": riwayat}, f)

def muat_saldo():
    global saldo, riwayat
    if os.path.exists(file_saldo):
        with open(file_saldo, "r") as f:
            data = json.load(f)
            saldo = data["saldo"]
            riwayat = data.get("riwayat", [])

def tambah_pemasukan():
    global saldo, riwayat
    try:
        jumlah = int(input("Masukkan jumlah pemasukan: "))
        if jumlah <= 0:
            print("Jumlah harus lebih dari 0!")
            return
        saldo += jumlah
        riwayat.append({"tipe": "Pemasukan", "jumlah": jumlah, "waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
        print(f"Pemasukan berhasil ditambahkan! Saldo sekarang: Rp {saldo}")
        simpan_saldo()
    except ValueError:
        print("Input tidak valid! Masukkan angka saja.")

def tambah_pengeluaran():
    global saldo, riwayat
    try:
        jumlah = int(input("Masukkan jumlah pengeluaran: "))
        if jumlah <= 0:
            print("Jumlah harus lebih dari 0!")
            return
        if jumlah > saldo:
            print(f"Peringatan! Saldo tidak cukup. Saldo Anda: Rp {saldo}")
        else:
            saldo -= jumlah
            riwayat.append({"tipe": "Pengeluaran", "jumlah": jumlah, "waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
            print(f"Pengeluaran berhasil! Saldo sekarang: Rp {saldo}")
            simpan_saldo()
    except ValueError:
        print("Input tidak valid! Masukkan angka saja.")

def lihat_saldo():
    print("=" * 35)
    print(f"   Saldo Anda saat ini: Rp {saldo}")
    print("=" * 35)

def lihat_laporan():
    total_pemasukan = 0
    total_pengeluaran = 0
    
    print("\n" + "=" * 50)
    print("   LAPORAN PEMASUKAN DAN PENGELUARAN")
    print("=" * 50)
    
    if not riwayat:
        print("Belum ada transaksi")
    else:
        for transaksi in riwayat:
            tipe = transaksi["tipe"]
            jumlah = transaksi["jumlah"]
            waktu = transaksi["waktu"]
            
            if tipe == "Pemasukan":
                total_pemasukan += jumlah
                print(f"[+] {tipe:12} Rp {jumlah:>10} ({waktu})")
            else:
                total_pengeluaran += jumlah
                print(f"[-] {tipe:12} Rp {jumlah:>10} ({waktu})")
    
    print("=" * 50)
    print(f"Total Pemasukan    : Rp {total_pemasukan}")
    print(f"Total Pengeluaran  : Rp {total_pengeluaran}")
    print(f"Saldo Akhir        : Rp {saldo}")
    print("=" * 50 + "\n")

def menu():
    print("=== Aplikasi Pengelola Uang Saku ===")
    print("1. Tambah pemasukan")
    print("2. Tambah pengeluaran")
    print("3. Lihat saldo")
    print("4. Lihat laporan")
    print("5. Keluar")

muat_saldo()

while True:
    try:
        menu()
        pilihan = input("Pilih menu: ").strip()
        
        if not pilihan:
            continue

        if pilihan == "1":
            tambah_pemasukan()
        elif pilihan == "2":
            tambah_pengeluaran()
        elif pilihan == "3":
            lihat_saldo()
        elif pilihan == "4":
            lihat_laporan()
        elif pilihan == "5":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid")
    except KeyboardInterrupt:
        print("\n\nProgram dihentikan. Data sudah disimpan!")
        break