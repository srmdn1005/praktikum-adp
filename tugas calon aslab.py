
energi = int(input("Energi  : ")) 
batas_waktu = int(input("Batas waktu kehancuran: ")) 
kapasitas_maks = int(input("Kapasitas maksimum pesawat (termasuk kamu): ")) 
jumlah_zona_input = int(input("Jumlah zona: ")) 

zona_data = []


for i in range(jumlah_zona_input):
    print(f"\nZona {i+1}")
    x = int(input(f"  X{i+1}: ")) 
    y = int(input(f"  Y{i+1}: ")) 
    jml_orang = int(input("  Jumlah orang: ")) 
    
    profesi = int(input("  Profesi (1 untuk Prioritas, 0 untuk Biasa): ")) 
    
    zona_data.append({
        "koordinat": (x, y),
        "orang": jml_orang,
        "prioritas": profesi
    })

orang_selamat = 0
waktu_terpakai = 0
rute = [(0, 0)] 
sisa_kapasitas = kapasitas_maks - 1 


for zona in zona_data:
  
    if energi >= 2 and waktu_terpakai + 2 <= batas_waktu and sisa_kapasitas > 1:
      
        energi -= 2
        waktu_terpakai += 2
        
        if zona["prioritas"] == 1:
            kuota_gender = sisa_kapasitas // 2
            jumlah_per_gender = min(zona["orang"] // 2, kuota_gender)
    
            total_diangkut = jumlah_per_gender * 2
            orang_selamat += total_diangkut
            sisa_kapasitas -= total_diangkut
            
            rute.append(zona["koordinat"])
    else:
        break

print("\nStatus: BERHASIL")
print(f"Rute: {', '.join(map(str, rute))}")
print(f"Orang diselamatkan: {orang_selamat}")
print(f"Sisa energi: {energi}")
print(f"Waktu terpakai: {waktu_terpakai}")