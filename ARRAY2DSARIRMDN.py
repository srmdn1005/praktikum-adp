huruf = ['A','A-','B+','B','B-','C+','C','D','E']
angka = [4.00,3.75,3.50,3.00,2.75,2.50,2.00,1.00,0.00]
m = int(input('jumlah mahasiswa : '))
k = int(input('jumlah mata kuliah : '))
mata_kuliah = []
for i in range (k):
    mata_kuliah.append(input(f'Nama Mata Kuliah ke - {i+1} : ')) 
dt = []
for i in range(m):
    print(f'\nMahasiswa ke -{i+1} : ')
    nama = input('Nama : ')
    nilai = []
    total = 0
    for j in range(k) :
        n = input(f'Nilai {mata_kuliah[j]} :').upper()
        nilai.append(n)
        total+= angka[huruf.index(n)]
    ip = total/k
    dt.append([nama,nilai,ip])
for i in range(len(dt)):
    for j in range (i+1,len(dt)):
        if dt[i][2]<dt[j][2]:
            tm=dt[i]
            dt[i]=dt[j]
            dt[j]= tm
print('\nTABEL IP MAHASISWA')
print('---'*20)
print(f'{'NAMA':<20}{'NILAI':<30}{'IP':>5}')
print('---'*20)
for x in dt :
    nama = x[0]
    n_str=', '.join(x[1])
    IP = x[2]
    print(f'{nama:<20}{n_str:<30}{IP:5}')
print('---'*20)
