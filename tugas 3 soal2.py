print()
print("SOAL 2:MELAKUKAN VALIDASI SUATU PASSWORD")
print() 
import re
pw= input("PASSWORD : \n")
pw_len = len(pw)
valid = False
while True :
    if pw_len <8 : 
        print('Password minimal 8 karakter') 
    elif not re.search('[a-z]',pw): 
        print("Password minimal mengandung 1 huruf kecil")
    elif not re.search('[A-Z]',pw):
        print("Password minimal mengandung 1 huruf kapital ")
    elif not re.search(r'[0-9]',pw):
        print("Password minimal mengandung 1 buah angka")
    elif not re.search(r'[!@#$%^&*()-_=+{}[|?;:<>/]',pw):
        print("Password minimal mengandung 1 karakter khusus")
    else:
        valid = True
        print("PASSWORD VALID")
    break