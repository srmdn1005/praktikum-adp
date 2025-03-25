import os #diajarin bapak narwen
os.system('cls')
print()
print("SOAL 1. MENCETAK POLA 'X' DAN 'O' ")
print()
n = int(input('Masukkan jumlah baris = '))
m = int(input('Masukkan jumlah Kolom = '))
s = 1
for s in range(1,n):
    y = 1
    for y in range(1,m):
        if (s+y)%2==0:
            print("X  ", end=" ")
        else :
            print("O  ", end=" ")
    print()
