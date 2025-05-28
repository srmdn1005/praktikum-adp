def glbb(v0,a,t):
    v=v0+a*t
    s=v0+t+1/2*a*t**2
    return v,s
n=int(input('Masukkan Jumlah Data : '))
data = []

for i in range(n):
    print(f'\n data ke-{i+1} :')
    v0 = float(input('Masukkan Kecepatan Awal(V0) : '))
    a = float(input('Masukkan Percepatan(a) : '))
    t = float(input('Masukkan Waktu(t) : '))
    v,s=glbb(v0,a,t)
    data.append([i+1,v0,a,t,v,s])
print('---'*27)
print('\n{:<5}{:<18}{:<18}{:<12}{:<20}{:<18}'.format(
'NO','KECEPATAN AWAL','PERCEPATAN','WAKTU','KECEPATAN AKHIR','JARAK'))
print('---'*27)
for x in data:
    print('{:<5}{:<18}{:<18}{:<12}{:<20}{:<18}'.format(
    x[0],x[1],x[2],x[3],x[4],x[5]))


