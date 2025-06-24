import os
import time
from termcolor import colored, cprint

# Clear screen
os.system('cls')

#LOADING
print(colored("\nL O A D I N G", "yellow"), end="")
for i in range(5):
        print(colored(".", "green"), end="", flush=True)
        time.sleep(0.5)
print()
print()
print()

# Header / Logo
print(colored('\t\t\t\t\t\t\t  ███      ███   ██   ███████ \t\t █████   ██    ██    █████     ███      ███','cyan'))
print(colored('\t\t\t\t\t\t\t  ██ █    █ ██   ██   ██      \t\t██   ██   ██  ██    ██   ██    ██ █    █ ██','cyan')) 
print(colored('\t\t\t\t\t\t\t  ██  █  █  ██   ██   █████   \t\t███████     ██      ███████    ██  █  █  ██','cyan'))
print(colored('\t\t\t\t\t\t\t  ██   ██   ██   ██   ██      \t\t██   ██     ██      ██   ██    ██   ██   ██','cyan'))
print(colored('\t\t\t\t\t\t\t  ██        ██   ██   ███████ \t\t██   ██     ██      ██   ██    ██        ██','cyan'))
print()
print(colored('\t\t\t\t\t\t\t\t\t\t██████    █████   ██  ██  ███████  █████ ','light_blue'))
print(colored('\t\t\t\t\t\t\t\t\t\t██   ██  ██   ██  ██ ██   ██      ██   ██','light_blue'))
print(colored('\t\t\t\t\t\t\t\t\t\t██████   ███████  ████    ███████ ██   ██','light_blue'))
print(colored('\t\t\t\t\t\t\t\t\t\t██   ██  ██   ██  ██ ██        ██ ██   ██','light_blue'))
print(colored('\t\t\t\t\t\t\t\t\t\t██████   ██   ██  ██  ██  ███████  █████ ','light_blue'))
print()
print(colored('\t\t\t\t\t\t\t██        ██  ██    ██   █████   ███    ██  ██  ██       ██████   ███████  ███████   █████','cyan'))
print(colored('\t\t\t\t\t\t\t██   ██   ██  ██    ██  ██   ██  ██ █   ██  ██ ██        ██   ██  ██       ██       ██   ██','cyan'))
print(colored('\t\t\t\t\t\t\t██  █  █  ██  ████████  ██   ██  ██  █  ██  ████         ██   ██  █████    ███████  ██   ██','cyan'))
print(colored('\t\t\t\t\t\t\t██ █    █ ██  ██    ██  ██   ██  ██   █ ██  ██ ██        ██   ██  ██            ██  ██   ██','cyan'))
print(colored('\t\t\t\t\t\t\t████     ███  ██    ██   █████   ██    ███  ██  ██       ██████   ███████  ███████   █████','cyan'))
print()
print('-----'*15,'PEMESANAN DELIVERY','-----'*15)

# Input Customer
nama = input("\nMasukkan nama customer  : ")
alamat = input("Masukkan alamat customer: ")

# MENU
def tampilkan_menu():
    print("\n==== MENU MAKANAN ====")
    print("1. Mie Ayam             - Rp 13.000")
    print("2. Bakso Urat           - Rp 13.000 (opsi mie putih/kuning/campur)")
    print("3. Bakso Telur          - Rp 15.000 (opsi mie putih/kuning/campur)")
    print("4. Bakso Beranak        - Rp 20.000 (opsi mie putih/kuning/campur)")
    print("5. Mie Ayam Bakso       - Rp 17.000")
    print("========================")

    print("\n==== MENU MINUMAN ====")
    print("1. Teh Manis            - Rp 4.000")
    print("2. Es Teh Manis         - Rp 5.000")
    print("3. Chocolatos Coklat    - Rp 7.000")
    print("4. Chocolatos Matcha    - Rp 7.000")
    print("5. Es Jeruk             - Rp 5.000")
    print("6. Nutrisari            - Rp 4.000")
    print("7. Air Mineral          - Rp 4.000")
    print("8. Air Mineral Dingin   - Rp 4.000")
    print("========================")

# PEMESANAN MAKANAN
def pesan_makanan():
    pesanan = []
    while True:
        pilihan = input("\nPilih menu makanan (1-5) atau ketik 'selesai': ").lower()
        if pilihan == 'selesai':
            break
        if pilihan not in ['1','2','3','4','5']:
            print("Pilihan tidak valid.")
            continue
        jumlah_input = input("Jumlah porsi: ")
        if not jumlah_input.isdigit():
            print("Masukkan angka yang valid.")
            continue
        jumlah = int(jumlah_input)

        menu = {
            '1': "Mie Ayam",
            '2': "Bakso Urat",
            '3': "Bakso Telur",
            '4': "Bakso Beranak",
            '5': "Mie Ayam Bakso"
        }[pilihan]

        item = {"Menu": menu, "Jumlah": jumlah}
        if menu in ["Bakso Urat", "Bakso Telur", "Bakso Beranak"]:
            pakai_mie = input("Ingin pakai mie? (ya/tidak): ").lower()
            if pakai_mie == "ya":
                while True:
                    jenis = input("Jenis mie (putih/kuning/campur): ").lower()
                    if jenis in ["putih", "kuning", "campur"]:
                        item["pakai_mie"] = "ya"
                        item["jenis_mie"] = jenis
                        break
                    print("Jenis mie tidak valid.")
            else:
                item["pakai_mie"] = "tidak"
        pesanan.append(item)
    return pesanan

# PEMESANAN MINUMAN
def pesan_minuman():
    pesanan = []
    daftar = {
        '1': "Teh Manis", 
        '2': "Es Teh Manis",
        '3': "Chocolatos Coklat",
        '4': "Chocolatos Matcha", 
        '5': "Es Jeruk", 
        '6': "Nutrisari",
        '7': "Air Mineral", 
        '8': "Air Mineral Dingin"
    }
    while True:
        pilihan = input("\nPilih menu minuman (1-8) atau ketik 'selesai': ").lower()
        if pilihan == 'selesai':
            break
        if pilihan not in daftar:
            print("Pilihan tidak valid.")
            continue
        jumlah_input = input("Jumlah porsi: ")
        if not jumlah_input.isdigit():
            print("Masukkan angka yang valid.")
            continue
        jumlah = int(jumlah_input)
        pesanan.append({"Menu": daftar[pilihan], "Jumlah": jumlah})
    return pesanan

# HITUNG TOTAL
def hitung_total(makanan, minuman):
    harga_makanan = {
        "Mie Ayam": 13000, 
        "Bakso Urat": 13000, 
        "Bakso Telur": 15000,
        "Bakso Beranak": 20000, 
        "Mie Ayam Bakso": 17000
    }
    harga_minuman = {
        "Teh Manis": 4000, 
        "Es Teh Manis": 5000, 
        "Chocolatos Coklat": 7000,
        "Chocolatos Matcha": 7000, 
        "Es Jeruk": 5000, 
        "Nutrisari": 4000,
        "Air Mineral": 4000, 
        "Air Mineral Dingin": 4000
    }
    total = 0
    for item in makanan:
        total += harga_makanan[item["Menu"]] * item["Jumlah"]
    for item in minuman:
        total += harga_minuman[item["Menu"]] * item["Jumlah"]
    return total

# DISKON
def hitung_diskon(total):
    if total >= 100000:
        return int(total * 0.10)
    elif total >= 50000:
        return int(total * 0.05)
    else:
        return 0

# TAMPILKAN STRUK
def tampilkan_ringkasan(makanan, minuman, total, diskon):
    print("\n===== RINGKASAN PESANAN =====")
    print(f"Nama Customer  : {nama}")
    print(f"Alamat Customer: {alamat}\n")
    if makanan:
        print(">> Makanan:")
        for item in makanan:
            detail = f"{item['Jumlah']} x {item['Menu']}"
            if item.get("pakai_mie") == "ya":
                detail += f" (mie {item['jenis_mie']})"
            elif item.get("pakai_mie") == "tidak":
                detail += " (tanpa mie)"
            print(detail)

    if minuman:
        print("\n>> Minuman:")
        for item in minuman:
            print(f"{item['Jumlah']} x {item['Menu']}")

    print(f"\nTOTAL SEBELUM DISKON : Rp {total:,}")
    print(f"DISKON               : Rp {diskon:,}")
    print(f"TOTAL BAYAR          : Rp {total - diskon:,}")
    print("==============================")

# SIMPAN STRUK KE FILE
def simpan_struk(nama, alamat, makanan, minuman, total, diskon):
    with open("struk_pesanan.txt", "w", encoding="utf-8") as file:
        file.write("===== STRUK PEMESANAN =====\n")
        file.write(f"Nama Customer  : {nama}\n")
        file.write(f"Alamat Customer: {alamat}\n\n")
        if makanan:
            file.write(">> Makanan:\n")
            for item in makanan:
                detail = f"{item['Jumlah']} x {item['Menu']}"
                if item.get("pakai_mie") == "ya":
                    detail += f" (mie {item['jenis_mie']})"
                elif item.get("pakai_mie") == "tidak":
                    detail += " (tanpa mie)"
                file.write(detail + "\n")
        if minuman:
            file.write("\n>> Minuman:\n")
            for item in minuman:
                file.write(f"{item['Jumlah']} x {item['Menu']}\n")
        file.write(f"\nTOTAL SEBELUM DISKON : Rp {total:,}\n")
        file.write(f"DISKON               : Rp {diskon:,}\n")
        file.write(f"TOTAL BAYAR          : Rp {total - diskon:,}\n")
        file.write("==============================\n")



# LOADING / ESTIMASI PESANAN
def estimasi_pesanan():
    
    for i in range(101):
        print(colored("\nMemproses pesanan Anda", "yellow"))
        cprint(' '*i,'white','on_blue',end='')
        print(f'{i}%')
        time.sleep(0.05)
        os.system('cls')
    print(colored("\nPesanan anda telah diterima", "light_green"))
    time.sleep(2)
    print(colored('Estimasi pesanan tiba dalam 10-15 menit.\n', "light_blue"))

#PROGRAM UTAMA
tampilkan_menu()
makanan = pesan_makanan()
minuman = pesan_minuman()
total = hitung_total(makanan, minuman)
diskon = hitung_diskon(total)
tampilkan_ringkasan(makanan, minuman, total, diskon)
simpan_struk(nama, alamat, makanan, minuman, total, diskon)
estimasi_pesanan()
