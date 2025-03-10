a = "Dibawah Payung"
b = "Magic Iland"
c = "Petaka Telaga Biru"
d = "LDR Paliang Jauah"
e = "Rain Renjana"
film = (f"(1){a}      : RP.42.000\n(2){b}         : RP.45.000\n(3){c}  : Rp.45.000\n(4){d}   : Rp.40.000\n(5){e}        : Rp.42.000")
print("CODE       JUDUL       HARGA TIKET")
print(film)
judul = input("Masukkan Judul Film = ")
kode = int(input("Masukkan Kode Film Anda : ")) 
if kode == 1:
    harga = 42000
    print(f'Harga Tiket = Rp.{harga}')
elif kode == 2:
    harga = 42000
    print(f'Harga Tiket = RP.{harga}')
elif kode == 3:
    harga = 42000
    print(f'Harga Tiket = RP.{harga}')
elif kode == 4:
    harga = 42000
    print(f'Harga Tiket = Rp.{harga}')
elif kode == 5:
    harga = 42000
    print(f'Harga Tiket = Rp.{harga}')
else:
   print("ERROR")
jumlah = int(input("Jumlah Tiket= "))
total = harga*jumlah
if total > 2500000 :
    diskon = 35/100
elif total > 100000 :
    diskon = 15/100
else :
    diskon = 0/100
potongan = total*diskon
total_setelah_diskon = total-potongan
nama = str(input("Nama Pembeli = "))
print("\n    STRUK PEMESANAN")
print(f'Nama Pembeli              :{nama}')
print(f'Judul Film                :{judul}')
print(f'Jumlah Tiket              :{jumlah}')
print(f'Harga Satuan Tiket        :Rp.{harga} ')
print(f'Potongan Harga            :Rp.{potongan}')
print(f'Total Harga Setelah Diskon:Rp.{total_setelah_diskon}')




