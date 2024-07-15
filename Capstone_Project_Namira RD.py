# Data awal barang di gudang
gudang_list = [
    {'id': 'A001', 'nama': 'Buku Hardcover', 'jumlah': 50, 'harga': 35000, 'supplier': 'PT. Buku Indah', 'kategori': 'Buku'},
    {'id': 'A002', 'nama': 'Pensil Warna', 'jumlah': 80, 'harga': 5000, 'supplier': 'PT. Warna Ceria', 'kategori': 'Alat Tulis'},
    {'id': 'A003', 'nama': 'Kertas HVS A4', 'jumlah': 200, 'harga': 30000, 'supplier': 'PT. Kertas Maju', 'kategori': 'Alat Tulis'},
    {'id': 'A004', 'nama': 'Sepatu Olahraga', 'jumlah': 100, 'harga': 250000, 'supplier': 'PT. Sporty Sejati', 'kategori': 'Fashion'},
    {'id': 'A005', 'nama': 'Tas Backpack', 'jumlah': 70, 'harga': 150000, 'supplier': 'PT. Travel Kuy', 'kategori': 'Fashion'},
    {'id': 'A006', 'nama': 'Kompor Gas', 'jumlah': 30, 'harga': 500000, 'supplier': 'PT. Dapur Berkah', 'kategori': 'Dapur'},
    {'id': 'A007', 'nama': 'Piring Keramik', 'jumlah': 120, 'harga': 25000, 'supplier': 'PT. Keramik Jaya', 'kategori': 'Dapur'},
    {'id': 'A008', 'nama': 'Sepeda Lipat', 'jumlah': 50, 'harga': 1500000, 'supplier': 'PT. Roda Maju', 'kategori': 'Transportasi'},
    {'id': 'A009', 'nama': 'Kacamata Hitam', 'jumlah': 80, 'harga': 100000, 'supplier': 'PT. Trendy Optik', 'kategori': 'Aksesori'},
    {'id': 'A010', 'nama': 'Jam Tangan Pria', 'jumlah': 60, 'harga': 300000, 'supplier': 'PT. Waktu Muda', 'kategori': 'Aksesori'},
    {'id': 'A011', 'nama': 'Boneka Beruang', 'jumlah': 40, 'harga': 75000, 'supplier': 'PT. Mainan Ceria', 'kategori': 'Mainan'},
    {'id': 'A012', 'nama': 'Laptop Backpack', 'jumlah': 25, 'harga': 200000, 'supplier': 'PT. Tas Berkualitas', 'kategori': 'Fashion'},
    {'id': 'A013', 'nama': 'Lampu Tidur', 'jumlah': 60, 'harga': 50000, 'supplier': 'PT. Cahaya Indah', 'kategori': 'Dekorasi'},
    {'id': 'A014', 'nama': 'Sandal Jepit', 'jumlah': 100, 'harga': 20000, 'supplier': 'PT. Nyaman Kaki', 'kategori': 'Fashion'},
    {'id': 'A015', 'nama': 'Sajadah Lipat', 'jumlah': 80, 'harga': 75000, 'supplier': 'PT. Sholat Yuk', 'kategori': 'Fashion'},
    {'id': 'A016', 'nama': 'Susu Formula Bayi', 'jumlah': 150, 'harga': 100000, 'supplier': 'PT. Gizi Sehat', 'kategori': 'Bayi'},
    {'id': 'A017', 'nama': 'Boneka Ragdoll', 'jumlah': 30, 'harga': 120000, 'supplier': 'PT. Mainan Seru', 'kategori': 'Mainan'},
    {'id': 'A018', 'nama': 'Bantal Guling', 'jumlah': 200, 'harga': 25000, 'supplier': 'PT. Tidur Nyenyak', 'kategori': 'Dekorasi'},
    {'id': 'A019', 'nama': 'Tas Selempang', 'jumlah': 150, 'harga': 80000, 'supplier': 'PT. Gaya Gen-Z', 'kategori': 'Fashion'},
    {'id': 'A020', 'nama': 'Kaos Kaki Anak', 'jumlah': 120, 'harga': 15000, 'supplier': 'PT. Kaki Bahagia', 'kategori': 'Fashion'}
]

# Confirm menu
def lanjut():
    while True:
        pilihan = input("Apakah ingin lanjut? (Y/N): \n").upper()
        if pilihan == 'Y':
            return True
        elif pilihan == 'N':
            return False
        else:
            print("Pilihan tidak valid, coba lagi.")

# Menampilkan daftar semua barang
def tampilkan_semua_barang():
    while True:
        tampilkan = input("Apakah anda ingin melihat daftar barang? (Y/N): ").upper()

        if tampilkan == 'Y':
            print("\nDaftar Semua Barang\n")
            print(f"{'ID'.ljust(10)}| {'Nama'.ljust(20)}| {'Jumlah'.ljust(10)}| {'Harga'.ljust(15)}| {'Supplier'.ljust(20)}| {'Kategori'.ljust(10)}")
            for barang in gudang_list:
                print(f"{barang['id'].ljust(10)}| {barang['nama'].ljust(20)}| {str(barang['jumlah']).ljust(10)}| {str(barang['harga']).ljust(15)}| {barang['supplier'].ljust(20)}| {barang['kategori'].ljust(10)}")
            print()
            break

        elif tampilkan == 'N':
            print("Barang tidak ditampilkan")
            break

        else:
            print("Pilihan tidak valid")
            
    menu1()

# Menampilkan barang berdasarkan ID
def tampilkan_barang_berdasarkan_id():
    while True:

        id_item = input("\nMasukkan ID Barang yang ingin ditampilkan: ")
        barang_ditemukan = False

        for barang in gudang_list:
            if barang['id'] == id_item:
                barang_ditemukan = True
                print("\nDetail Barang\n")
                print(f"{'ID'.ljust(10)}| {'Nama'.ljust(20)}| {'Jumlah'.ljust(10)}| {'Harga'.ljust(15)}| {'Supplier'.ljust(20)}| {'Kategori'.ljust(10)}")
                print(f"{barang['id'].ljust(10)}| {barang['nama'].ljust(20)}| {str(barang['jumlah']).ljust(10)}| {str(barang['harga']).ljust(15)}| {barang['supplier'].ljust(20)}| {barang['kategori'].ljust(10)}")
                break

        if not barang_ditemukan:
            print(f"\nID {id_item} salah, silahkan input kembali.\n")
            continue

        if not lanjut():
            break
    menu1()

# Memanggil Sub-menu 1
def menu1():
    while True:

        print("""\n\tSub Menu:
            1. Tampilkan Semua Data Barang
            2. Masukkan ID Barang
            3. Kembali ke Menu Utama""")
        pilihan = input("\n\tPilih opsi (1/2/3): ")

        if pilihan == '1':
            if not tampilkan_semua_barang():
                break

        elif pilihan == '2':
            tampilkan_barang_berdasarkan_id()
            break

        elif pilihan == '3':
            break

        else:
            print("\nPilihan tidak valid, coba lagi.\n")

# Menampilkan tambah barang
def menu2():
    while True:

        print("""\n\tSub Menu:
            1. Tambah Data Barang
            2. Kembali ke Menu Utama""")
        pilihan = input("\n\tPilih opsi (1/2): ")

        if pilihan == '1':
            while True:
                print("\nDaftar Barang")
                print(f"{'ID'.ljust(10)}| {'Nama'.ljust(20)}| {'Jumlah'.ljust(10)}| {'Harga'.ljust(15)}| {'Supplier'.ljust(20)}| {'Kategori'.ljust(10)}")
                for barang in gudang_list:
                    print(f"{barang['id'].ljust(10)}| {barang['nama'].ljust(20)}| {str(barang['jumlah']).ljust(10)}| {str(barang['harga']).ljust(15)}| {barang['supplier'].ljust(20)}| {barang['kategori'].ljust(10)}")

                id_item = input("\nMasukkan ID Barang Baru: ")
                id_sudah_ada = False
                for barang in gudang_list:
                    if barang['id'] == id_item:
                        id_sudah_ada = True
                        break
                
                if id_sudah_ada:
                    print("ID sudah ada, silahkan input kembali.")
                    continue
                
                nama = input("Masukkan Nama Barang: ")
                jumlah = input("Masukkan Jumlah Barang: ")
                harga = input("Masukkan Harga Barang: ")
                supplier = input("Masukkan Supplier Barang: ")
                kategori = input("Masukkan Kategori Barang: ")

                if not id_item:
                    print("ID Barang salah, silahkan input kembali.")
                elif not nama:
                    print("Nama Barang salah, silahkan input kembali.")
                elif not jumlah.isdigit():
                    print("Jumlah Barang salah, silahkan input kembali.")
                elif not harga.isdigit():
                    print("Harga Barang salah, silahkan input kembali.")
                elif not supplier:
                    print("Supplier Barang salah, silahkan input kembali.")
                elif not kategori:
                    print("Kategori Barang salah, silahkan input kembali.")
                else:
                    gudang_list.append({'id': id_item, 'nama': nama, 'jumlah': jumlah, 'harga': harga, 'supplier': supplier, 'kategori': kategori})
                    print(f"\nBarang {nama} sudah ditambahkan\n")

                    print("\nDaftar Barang")
                    print(f"{'ID'.ljust(10)}| {'Nama'.ljust(20)}| {'Jumlah'.ljust(10)}| {'Harga'.ljust(15)}| {'Supplier'.ljust(20)}| {'Kategori'.ljust(10)}")
                    for barang in gudang_list:
                        print(f"{barang['id'].ljust(10)}| {barang['nama'].ljust(20)}| {str(barang['jumlah']).ljust(10)}| {str(barang['harga']).ljust(15)}| {barang['supplier'].ljust(20)}| {barang['kategori'].ljust(10)}")
                    
                    konfirmasi = input("Apakah Anda ingin menyimpan barang ini? (Y/N): ")
                    if konfirmasi == 'Y' or konfirmasi == 'y':
                        print(f"\nBarang {nama} sudah ditambahkan\n")
                    else:
                        print("Penambahan barang dibatalkan.")

                    if not lanjut():
                        break

        elif pilihan == '2':
            break

        else:
            print("\nPilihan tidak valid, coba lagi.\n")

# Memperbarui barang
def menu3():
    while True:
        print("""\n\tSub Menu:
            1. Perbarui Data Barang
            2. Kembali ke Menu Utama""")
        pilihan = input("\n\tPilih opsi (1/2): ")

        if pilihan == '1':
            print("\nDaftar Barang")
            print(f"{'ID'.ljust(10)}| {'Nama'.ljust(20)}| {'Jumlah'.ljust(10)}| {'Harga'.ljust(15)}| {'Supplier'.ljust(20)}| {'Kategori'.ljust(10)}")
            for barang in gudang_list:
                print(f"{barang['id'].ljust(10)}| {barang['nama'].ljust(20)}| {str(barang['jumlah']).ljust(10)}| {str(barang['harga']).ljust(15)}| {barang['supplier'].ljust(20)}| {barang['kategori'].ljust(10)}")

            while True:
                id_item = input("\nMasukkan ID Barang yang ingin diperbarui: ")
                barang_ditemukan = False

                for barang in gudang_list:
                    if barang['id'] == id_item:
                        barang_ditemukan = True
                        print("\nDetail Barang")
                        print(f"{'ID'.ljust(10)}| {'Nama'.ljust(20)}| {'Jumlah'.ljust(10)}| {'Harga'.ljust(15)}| {'Supplier'.ljust(20)}| {'Kategori'.ljust(10)}")
                        print(f"{barang['id'].ljust(10)}| {barang['nama'].ljust(20)}| {str(barang['jumlah']).ljust(10)}| {str(barang['harga']).ljust(15)}| {barang['supplier'].ljust(20)}| {barang['kategori'].ljust(10)}")
                        
                        while True:
                            print("""\n\tSub Menu Perbarui Data Barang:
                                1. Nama Barang
                                2. Jumlah Barang
                                3. Harga Barang
                                4. Supplier Barang
                                5. Kategori Barang
                                6. Kembali ke Menu Utama""")
                            sub_pilihan = input("\n\tPilih opsi (1-6): ")

                            if sub_pilihan == '1':
                                nama_baru = input("Masukkan Nama Barang Baru: ")
                                if konfirmasi_ubah():
                                    barang['nama'] = nama_baru
                                    print("\nNama Barang sudah diperbarui\n")
                                else:
                                    print("\nPerubahan nama barang dibatalkan.\n")
                            elif sub_pilihan == '2':
                                jumlah_baru = input("Masukkan Jumlah Barang Baru: ")
                                if konfirmasi_ubah():
                                    barang['jumlah'] = int(jumlah_baru)
                                    print("\nJumlah Barang sudah diperbarui\n")
                                else:
                                    print("\nPerubahan jumlah barang dibatalkan.\n")
                            elif sub_pilihan == '3':
                                harga_baru = input("Masukkan Harga Barang Baru: ")
                                if konfirmasi_ubah():
                                    barang['harga'] = int(harga_baru)
                                    print("\nHarga Barang sudah diperbarui\n")
                                else:
                                    print("\nPerubahan harga barang dibatalkan.\n")
                            elif sub_pilihan == '4':
                                supplier_baru = input("Masukkan Supplier Barang Baru: ")
                                if konfirmasi_ubah():
                                    barang['supplier'] = supplier_baru
                                    print("\nSupplier Barang sudah diperbarui\n")
                                else:
                                    print("\nPerubahan supplier barang dibatalkan.\n")
                            elif sub_pilihan == '5':
                                kategori_baru = input("Masukkan Kategori Barang Baru: ")
                                if konfirmasi_ubah():
                                    barang['kategori'] = kategori_baru
                                    print("\nKategori Barang sudah diperbarui\n")
                                else:
                                    print("\nPerubahan kategori barang dibatalkan.\n")
                            elif sub_pilihan == '6':
                                break
                            else:
                                print("\nPilihan tidak valid, coba lagi.\n")
                        continue

                if not barang_ditemukan:
                    print(f"\nID {id_item} salah, silahkan input kembali.\n")
                    continue

                if not lanjut():
                    break

        elif pilihan == '2':
            break

        else:
            print("\nPilihan tidak valid, coba lagi.\n")

# Konfirmasi ubah data pada menu3
def konfirmasi_ubah():
    while True:
        konfirmasi = input("Apakah anda yakin ingin mengubah data ini? (Y/N): ").upper()
        if konfirmasi == 'Y':
            return True
        elif konfirmasi == 'N':
            return False
        else:
            print("Masukkan tidak valid. Silakan masukkan 'Y' atau 'N'.")    

# Menghapus barang
def menu4():
    while True:
        print("""\n\tSub Menu:
            1. Hapus Data Barang
            2. Kembali ke Menu Utama""")
        pilihan = input("\n\tPilih opsi (1/2): ")

        if pilihan == '1':
            while True:
                print("\nDaftar Barang")
                print(f"{'ID'.ljust(10)}| {'Nama'.ljust(20)}| {'Jumlah'.ljust(10)}| {'Harga'.ljust(15)}| {'Supplier'.ljust(20)}| {'Kategori'.ljust(10)}")
                for barang in gudang_list:
                    print(f"{barang['id'].ljust(10)}| {barang['nama'].ljust(20)}| {str(barang['jumlah']).ljust(10)}| {str(barang['harga']).ljust(15)}| {barang['supplier'].ljust(20)}| {barang['kategori'].ljust(10)}")

                hapus_id = input("\nMasukkan ID barang yang ingin dihapus: ")
                barang_ditemukan = False

                for i, barang in enumerate(gudang_list):
                    if barang['id'] == hapus_id:
                        print(f"\nDetail Barang\n")
                        print(f"{'ID'.ljust(10)}| {'Nama'.ljust(20)}| {'Jumlah'.ljust(10)}| {'Harga'.ljust(15)}| {'Supplier'.ljust(20)}| {'Kategori'.ljust(10)}")
                        print(f"{barang['id'].ljust(10)}| {barang['nama'].ljust(20)}| {str(barang['jumlah']).ljust(10)}| {str(barang['harga']).ljust(15)}| {barang['supplier'].ljust(20)}| {barang['kategori'].ljust(10)}")

                        hapus_confirm = input("\nApakah Anda ingin menghapus data barang ini? (Y/N): ").upper()

                        if hapus_confirm == 'Y':
                            del gudang_list[i]
                            print(f"\nBarang dengan ID {hapus_id} berhasil dihapus\n")
                        else:
                            print(f"\nPenghapusan barang dengan ID {hapus_id} dibatalkan\n")
                        barang_ditemukan = True
                        break

                if not barang_ditemukan:
                    print(f"\nID {hapus_id} salah, silahkan input kembali.\n")
                    continue

                if not lanjut():
                    break

        elif pilihan == '2':
            break

        else:
            print("\nPilihan tidak valid, coba lagi.\n")

# Exit Program
def menu5():
    print("\nProgram berakhir")

# Main Menu
def main_menu():
    print("\tSelamat Datang di Gudang\n")
    print("""\tList Menu :
        1. Menampilkan Daftar Barang
        2. Menambah Barang
        3. Memperbarui Barang
        4. Menghapus Barang
        5. Exit Program\n""")
    
    while True:
        list_menu = input("\tMasukkan angka Menu yang ingin dijalankan: ")
        
        if list_menu == '1':
            menu1()
            main_menu()
        elif list_menu == '2':
            menu2()
            main_menu()
        elif list_menu == '3':
            menu3()
            main_menu()
        elif list_menu == '4':
            menu4()
            main_menu()
        elif list_menu == '5':
            menu5()
            break
        else:
            print("\n\tPilihan tidak valid, coba lagi\n")

# Memanggil main_menu untuk menjalankan program
main_menu()
