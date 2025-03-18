import os #diajarin bapak narwen
os.system('cls')
print() #diajarin bapak narwen
print("      menghitung pertumbuhan modal setiap tahun\nhingga mencapai jumlah target investasi yang diinginkan")
print()
print("*********************************************************")
print()
M = int(input("Masukkan modal awal investasi = Rp. "))
r = float(input("Masukkan suku bunga tahunan (%) = "))
T = int(input("Target investasi yang ingin dicapai =Rp. "))
print('---------------------------------------------------------')
n = 0
while (M<T):
    JB = M*r/100
    M = M+JB
    n = n+1
    print(f'tahun ke{n} : Rp.{M}')
    if M>=T :
        break
print(f'bunga =Rp.{JB}')
print (f'Target Tercapai dalam {n} tahun!')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~SELESAI~~~~~~~~~~~~~~~~~~~~~~~~')
