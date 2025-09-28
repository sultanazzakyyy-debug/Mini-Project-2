# Data nama-nama pesawat
nama_pesawat = ["Super air jet", "Garuda indonesia", "Citilink"]

arrival = []    
departure = []
runway = ""

def login():
    print("\n================================================")
    print("======      SISTEM LOGIN ATC BANDARA      ======")
    print("================================================")
    print("[1]. Login sebagai Manager")
    print("[2]. Login sebagai Karyawan")
    
    while True:
        try:
            pilihan = input("\nSilahkan pilih jenis login 1 or 2: ")
            
            if pilihan == "1":
                posisi = "Manager"
                print("\n=== Login sebagai Manager ===")
                username = input("Masukkan username: ")
                password = input("Masukkan password: ")
                
                if posisi == "Manager":
                    if username == "naltuS" and password == "gyj123":
                        jabatan = "Manager"
                        print(f"\nLogin success! Selamat datang:), {username} ({jabatan}).")
                        return jabatan
                
                print("Mungkin username atau password salah! Silahkan dicoba lagi ya.")
                
            elif pilihan == "2":
                posisi = "Karyawan"
                print("\n=== Login sebagai Karyawan ===")
                username = input("Masukkan username: ")
                password = input("Masukkan password: ")
                
                if posisi == "Karyawan":
                    if username == "Sultan" and password == "gyj321":
                        jabatan = "Karyawan"
                        print(f"\nLogin success! Selamat datang:), {username} ({jabatan}).")
                        return jabatan
                
                print("Mungkin username atau password salah! Silahkan dicoba lagi ya.")
                
            else:
                print("Pilihan tidak valid! Silakan pilih 1 atau 2.")
                
        except KeyboardInterrupt:
            print("\nProgram dihentikan oleh pengguna.")
        except ValueError:
            print("\nTolong Masukkan angka! ")
            exit()

def display_menu(jabatan):
    print("\n================================================")
    print("======          MENU ATC BANDARA         =======")
    print("================================================")
    print("[1]. Nama-nama pesawat")
    if jabatan == "Manager":
        print("[2]. Menambahkan pesawat")
        print("[3]. Menghapus pesawat")
        print("[4]. Mengubah pesawat")
    print("[5]. Tambahkan ke arrival")
    print("[6]. Tambahkan ke departure")
    print("[7]. Scheduler")
    print("[8]. Stop")

# Read
def daftar_pesawat():
    try:
        if nama_pesawat:
            print("\nDaftar pesawat:")
            nomor = 1
            for pesawat in nama_pesawat:
                print(f"{nomor}. {pesawat}")
                nomor += 1
        else:
            print("\nTidak ada pesawat terdaftar!")
    except ValueError:
        print("Terjadi kesalahan saat membaca data pesawat!")

# Create
def tambah_pesawat(jabatan):
    try:
        if jabatan == "Manager":
            nama = input("\nNama pesawat baru: ")
            if nama and nama not in nama_pesawat:
                nama_pesawat.append(nama)
                print(f"Pesawat ditambahkan: {nama}")
            else:
                print("Nama pesawat tidak valid atau sudah ada!")
        else:
            print("\nHanya Manager yang boleh menambah pesawat!")
    except ValueError:
        print("Error saat menambah pesawat baru!")

# Delete
def hapus_pesawat(jabatan):
    try:
        if jabatan == "Manager":
            daftar_pesawat()
            hapus = input("\nNama pesawat yang dihapus: ")
            if hapus in nama_pesawat:
                nama_pesawat.remove(hapus)
                print(f"Pesawat dihapus: {hapus}")
            else:
                print("Pesawat tidak ditemukan!")
        else:
            print("\nHanya Manager yang boleh menghapus pesawat!")
    except ValueError:
        print("Pesawat tidak ditemukan dalam daftar pesawat!")

# Update
def ubah_pesawat(jabatan):
    try:
        if jabatan == "Manager":
            daftar_pesawat()
            lama = input("\nNama pesawat yang diubah: ")
            if lama in nama_pesawat:
                baru = input("Masukkan nama pesawat baru: ")
                if baru and baru not in nama_pesawat:
                    nama_pesawat.remove(lama)
                    nama_pesawat.append(baru)
                    print(f"Pesawat '{lama}' diubah menjadi: {baru}")
                else:
                    print("Nama baru tidak valid atau sudah ada!")
            else:
                print("Pesawat tidak ditemukan!")
        else:
            print("\nHanya Manager yang boleh mengubah pesawat!")
    except ValueError:
        print("Data pesawat lama tidak dapat ditemukan!")

def tambah_arrival():
    try:
        daftar_pesawat()
        nama = input("\nNama pesawat yang dimasukkan ke Arrival: ")
        if nama in nama_pesawat:
            if nama not in arrival and nama not in departure:
                arrival.append(nama)
                print(f"Ditambahkan ke Arrival: {nama}")
            else:
                print("Pesawat sudah ada di Arrival atau Departure.")
        else:
            print("Pesawat tidak terdaftar.")
    except ValueError:
        print("Error saat memasukkan pesawat ke Arrival.")

def tambah_departure():
    try:
        daftar_pesawat()
        nama = input("\nNama pesawat yang dimasukkan ke Departure: ")
        if nama in nama_pesawat:
            if nama not in arrival and nama not in departure:
                departure.append(nama)
                print(f"Ditambahkan ke Departure: {nama}")
            else:
                print("Pesawat sudah ada di Arrival atau Departure.")
        else:
            print("Pesawat tidak terdaftar.")
    except ValueError:
        print("Error saat memasukkan pesawat ke Departure.")

def scheduler(runway):
    try:
        print("\n===============================================")
        print("======          Scheduler ATC            ======")
        print("===============================================")
        if runway != "":
            print(f"Runway sedang dipakai oleh: {runway}")
            print("Runway sekarang dikosongkan...")
            runway = ""
        elif arrival:
            runway = arrival.pop()
            print(f"Pesawat {runway} mendarat (Arrival)")
        elif departure:
            runway = departure.pop()
            print(f"Pesawat {runway} lepas landas (Departure)")
        else:
            print("Tidak ada pesawat yang menunggu...")
        
        print(f"\nStatus Arrival: {arrival}")
        print(f"Status Departure: {departure}")
        print(f"Runway saat ini sedang dipakai oleh pesawat: {runway if runway else 'Kosong'}")
        return runway
    except ValueError:
        print("Ada trouble pada scheduler...")
        return runway

def main():
    jabatan = login()
    runway = ""
    while True:
        try:
            display_menu(jabatan)
            menu = input("Pilih menu: ")
            
            if menu == "1":
                daftar_pesawat()
            elif menu == "2":
                tambah_pesawat(jabatan)
            elif menu == "3":
                hapus_pesawat(jabatan)
            elif menu == "4":
                ubah_pesawat(jabatan)
            elif menu == "5":
                tambah_arrival()
            elif menu == "6":
                tambah_departure()
            elif menu == "7":
                runway = scheduler(runway)
            elif menu == "8":
                print("Program dihentikan...")
                break
            else:
                print("Menu salah!")
        except KeyboardInterrupt:
            print("\nProgram dihentikan oleh pengguna.")
            break
        except ValueError:
            print("\nKetik nomor sesuai menu yang kamu mau.")
        except EOFError:
            print("\nJangan tekan CTRL+Z ya! ")

main()
