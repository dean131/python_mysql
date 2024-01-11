# -*- coding: utf-8 -*-
"""PBO PRAKTIK Pertemuan 11 .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Gx4KwZrGSvr7R7Zpr85O8P7Ik7_698t7
"""

from os import system, name
def clear_terminal():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


class TeknologiDigital:
    def __init__(self, nama, merk, tahun_produksi, warna, sistem_operasi):
        self.nama = nama
        self.merk = merk
        self.tahun_produksi = tahun_produksi
        self.warna = warna
        self.sistem_operasi = sistem_operasi

    def display_info(self):
        print("\n" + "=" * 30)
        print(f"Info Teknologi Digital ({self.nama}):")
        print("=" * 30)
        print(f"Merk: {self.merk}")
        print(f"Tahun Keluaran: {self.tahun_produksi}")
        print(f"Warna: {self.warna}")
        print(f"Sistem Operasi: {self.sistem_operasi}")


class Handphone(TeknologiDigital):
    def __init__(self, nama, merk, tahun_produksi, warna, sistem_operasi, jaringan, kamera):
        super().__init__(nama, merk, tahun_produksi, warna, sistem_operasi)
        self.jaringan = jaringan
        self.kamera = kamera
        self.riwayat_telepon = []
        self.riwayat_pesan = []

    def display_info(self):
        super().display_info()
        print(f"Jaringan: {self.jaringan}")
        print(f"Kamera: {self.kamera} MP")

    def display_riwayat_telepon(self):
        print("\nRiwayat Telepon:")
        for telepon in self.riwayat_telepon:
            print(f"Telepon ke: {telepon}")

    def display_riwayat_pesan(self):
        print("\nRiwayat Pesan:")
        for pesan in self.riwayat_pesan:
            print(f"Pesan ke: {pesan['nomor']} - Isi: {pesan['isi']}")

    def telepon(self, nomor):
        print(f"Menelpon ke {nomor}")
        self.riwayat_telepon.append(nomor)

    def kirim_pesan(self, nomor, isi):
        print(f"Mengirim pesan ke {nomor} - Isi: {isi}")
        self.riwayat_pesan.append({'nomor': nomor, 'isi': isi})


class Laptop(TeknologiDigital):
    def __init__(self, nama, merk, tahun_produksi, warna, sistem_operasi, ukuran_layar, kapasitas_ram, kapasitas_harddisk):
        super().__init__(nama, merk, tahun_produksi, warna, sistem_operasi)
        self.ukuran_layar = ukuran_layar
        self.kapasitas_ram = kapasitas_ram
        self.kapasitas_harddisk = kapasitas_harddisk

    def display_info(self):
        super().display_info()
        print(f"Ukuran Layar: {self.ukuran_layar} inch")
        print(f"Kapasitas RAM: {self.kapasitas_ram} GB")
        print(f"Kapasitas Hard Disk: {self.kapasitas_harddisk} GB")


class LaptopGaming(Laptop):
    def __init__(self, nama, merk, tahun_produksi, warna, sistem_operasi, ukuran_layar, kapasitas_ram, kapasitas_harddisk, jenis_vga):
        super().__init__(nama, merk, tahun_produksi, warna, sistem_operasi, ukuran_layar, kapasitas_ram, kapasitas_harddisk)
        self.jenis_vga = jenis_vga
        self.game_history = []

    def display_info(self):
        super().display_info()
        print(f"Jenis VGA: {self.jenis_vga}")
        print("Fitur Gaming: Dukungan tingkat tinggi untuk gaming")

    def display_game_history(self):
        print("\nGame yang pernah dimainkan:")
        for game in self.game_history:
            print(game)

    def play_game(self, game_title):
        print(f"Bermain game: {game_title}")
        self.game_history.append(game_title)


# Program utama
list_teknologi_digital = []

while True:
    clear_terminal()
    print("\n" + "=" * 30)
    print("Menu:")
    print("=" * 30)
    print("1. Daftar Teknologi Digital")
    print("2. List Teknologi Digital")
    print("3. Keluar")

    choice_menu = input("Pilih menu (1/2/3): ")

    if choice_menu == "1":
        clear_terminal()
        print("\n" + "=" * 30)
        print("Jenis Teknologi Digital:")
        print("=" * 30)
        print("1. Handphone")
        print("2. Laptop")
        choice_teknologi = input("Pilih jenis teknologi digital (1/2): ")

        if choice_teknologi == "1":
            clear_terminal()
            nama = input("Nama Handphone: ")
            merk = input("Merk Handphone: ")
            tahun = input("Tahun Produksi: ")
            warna = input("Warna Handphone: ")
            os = input("Sistem Operasi: ")
            jaringan = input("Jaringan: ")
            kamera = input("Resolusi Kamera (MP): ")

            handphone = Handphone(nama, merk, tahun, warna, os, jaringan, kamera)
            list_teknologi_digital.append(handphone)

            # Menu Handphone
            while True:
                print("\n" + "=" * 30)
                print("Menu Handphone:")
                print("=" * 30)
                print("1. Telepon")
                print("2. Kirim Pesan")
                print("3. Kembali ke Menu Utama")

                choice_handphone = input("Pilih menu Handphone (1/2/3): ")

                if choice_handphone == "1":
                    nomor = input("Masukkan nomor telepon: ")
                    handphone.telepon(nomor)
                elif choice_handphone == "2":
                    nomor = input("Masukkan nomor tujuan: ")
                    isi_pesan = input("Masukkan isi pesan: ")
                    handphone.kirim_pesan(nomor, isi_pesan)
                elif choice_handphone == "3":
                    break
                else:
                    print("Pilihan tidak valid. Silakan pilih antara 1-3.")

        elif choice_teknologi == "2":
            nama = input("Nama Laptop: ")
            merk = input("Merk Laptop: ")
            tahun = input("Tahun Produksi: ")
            warna = input("Warna Laptop: ")
            os = input("Sistem Operasi: ")
            layar = input("Ukuran Layar (inch): ")
            ram = input("Kapasitas RAM (GB): ")
            harddisk = input("Kapasitas Hard Disk (GB): ")

            choice_laptop = input("Apakah laptop ini khusus gaming? (ya/tidak): ")
            if choice_laptop.lower() == "ya":
                jenis_vga = input("Jenis VGA: ")
                laptop = LaptopGaming(nama, merk, tahun, warna, os, layar, ram, harddisk, jenis_vga)
                list_teknologi_digital.append(laptop)

                # Menu Laptop Gaming
                while True:
                    print("\n" + "=" * 30)
                    print("Menu Laptop Gaming:")
                    print("=" * 30)
                    print("1. Mainkan Game")
                    print("2. Tampilkan Riwayat Game")
                    print("3. Kembali ke Menu Utama")

                    choice_game = input("Pilih menu Laptop Gaming (1/2/3): ")

                    if choice_game == "1":
                        game_title = input("Masukkan judul game: ")
                        laptop.play_game(game_title)
                    elif choice_game == "2":
                        laptop.display_game_history()
                    elif choice_game == "3":
                        break
                    else:
                        print("Pilihan tidak valid. Silakan pilih antara 1-3.")

            else:
                laptop = Laptop(nama, merk, tahun, warna, os, layar, ram, harddisk)
                list_teknologi_digital.append(laptop)

    elif choice_menu == "2":
        print("\n" + "=" * 30)
        print("List Teknologi Digital:")
        print("=" * 30)
        for idx, teknologi in enumerate(list_teknologi_digital, start=1):
            print(f"{idx}. {teknologi.nama} ({teknologi.__class__.__name__})")
            print(f"   Tahun Keluaran: {teknologi.tahun_produksi}")

        choice_detail = int(input("\nPilih nomor teknologi digital untuk melihat detail (0 untuk kembali): "))

        if 0 < choice_detail <= len(list_teknologi_digital):
            teknologi_terpilih = list_teknologi_digital[choice_detail - 1]
            teknologi_terpilih.display_info()

            if isinstance(teknologi_terpilih, Handphone):
                choice_riwayat = input("Tampilkan riwayat telepon/pesan? (ya/tidak): ")
                if choice_riwayat.lower() == "ya":
                    teknologi_terpilih.display_riwayat_telepon()
                    teknologi_terpilih.display_riwayat_pesan()
            elif isinstance(teknologi_terpilih, LaptopGaming):
                choice_game_history = input("Tampilkan riwayat game? (ya/tidak): ")
                if choice_game_history.lower() == "ya":
                    teknologi_terpilih.display_game_history()

        elif choice_detail == 0:
            continue
        else:
            print("Pilihan tidak valid. Silakan pilih nomor teknologi digital yang valid.")

    elif choice_menu == "3":
        print("\n" + "=" * 30)
        print("Program selesai. Sampai jumpa!")
        print("=" * 30)
        break
    else:
        print("\n" + "=" * 30)
        print("Pilihan tidak valid. Silakan pilih antara 1-3.")
        print("=" * 30)