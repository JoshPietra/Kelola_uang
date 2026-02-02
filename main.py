import json
import os

saldo = 0
file_saldo = "saldo.json"

def simpan_saldo():
    with open(file_saldo, "w") as f:
        json.dump({"saldo": saldo}, f)

def muat_saldo():
    global saldo
    if os.path.exists(file_saldo):
        with open(file_saldo, "r") as f:
            data = json.load(f)
            saldo = data["saldo"]

def tambah_pemasukan():
    global saldo
    jumlah = int(input("Masukkan jumlah pemasukan: "))
    saldo += jumlah
    print(f"Pemasukan berhasil ditambahkan! Saldo sekarang: Rp {saldo}")
    simpan_saldo()

def tambah_pengeluaran():
    global saldo
    jumlah = int(input("Masukkan jumlah pengeluaran: "))
    if jumlah > saldo:
        print(f"Peringatan! Saldo tidak cukup. Saldo Anda: Rp {saldo}")
    else:
        saldo -= jumlah
        print(f"Pengeluaran berhasil! Saldo sekarang: Rp {saldo}")
        simpan_saldo()

def lihat_saldo():
    print("=" * 35)
    print(f"   Saldo Anda saat ini: Rp {saldo}")
    print("=" * 35)

def menu():
    print("=== Aplikasi Pengelola Uang Saku ===")
    print("1. Tambah pemasukan")
    print("2. Tambah pengeluaran")
    print("3. Lihat saldo")
    print("4. Keluar")

muat_saldo()

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_pemasukan()
    elif pilihan == "2":
        tambah_pengeluaran()
    elif pilihan == "3":
        lihat_saldo()
    elif pilihan == "4":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid")