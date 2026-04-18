# --- INPUT PARAMETER UTAMA ---
# Pengguna memasukkan batasan dasar program secara manual
energi = int(input("Energi  : ")) 
batas_waktu = int(input("Batas waktu kehancuran: ")) 
kapasitas_maks = int(input("Kapasitas maksimum pesawat (termasuk kamu): ")) 
jumlah_zona_input = int(input("Jumlah zona: ")) 

zona_data = []

# --- INPUT DATA ZONA (MANUAL) ---
# Mengumpulkan data penduduk dan profesi di tiap zona
for i in range(jumlah_zona_input):
    print(f"\nZona {i+1}")
    x = int(input(f"  X{i+1}: ")) 
    y = int(input(f"  Y{i+1}: ")) 
    jml_orang = int(input("  Jumlah orang: ")) 
    # Profesi: 1=Prioritas (Kesehatan/Teknologi/Penelitian), 0=Biasa
    profesi = int(input("  Profesi (1 untuk Prioritas, 0 untuk Biasa): ")) 
    
    zona_data.append({
        "koordinat": (x, y),
        "orang": jml_orang,
        "prioritas": profesi
    })

# Inisialisasi variabel bantuan
orang_selamat = 0
waktu_terpakai = 0
rute = [(0, 0)] # Memulai dari titik awal
sisa_kapasitas = kapasitas_maks - 1 # Dikurangi 1 untuk kamu sebagai pilot

# --- LOGIKA EVAKUASI ---
for zona in zona_data:
    # Syarat 1: Cek apakah energi, waktu, dan kapasitas masih tersedia
    if energi >= 2 and waktu_terpakai + 2 <= batas_waktu and sisa_kapasitas > 1:
        
        # Biaya perjalanan (asumsi energi dan waktu berkurang setiap pindah zona)
        energi -= 2
        waktu_terpakai += 2
        
        # Syarat 2 (Pengkondisian Bersarang): Hanya ambil jika profesi prioritas
        if zona["prioritas"] == 1:
            # Aturan Peradaban: Harus ada keseimbangan gender (50:50)
            # Kita ambil setengah dari jumlah orang di zona tersebut, atau sisa kuota gender
            kuota_gender = sisa_kapasitas // 2
            jumlah_per_gender = min(zona["orang"] // 2, kuota_gender)
            
            # Update data penumpang
            total_diangkut = jumlah_per_gender * 2
            orang_selamat += total_diangkut
            sisa_kapasitas -= total_diangkut
            
            # Catat koordinat zona yang berhasil dievakuasi
            rute.append(zona["koordinat"])
    else:
        # Berhenti jika sumber daya habis
        break

# --- OUTPUT (Sesuai format pada file PDF) ---
print("\nStatus: BERHASIL")
print(f"Rute: {', '.join(map(str, rute))}")
print(f"Orang diselamatkan: {orang_selamat}")
print(f"Sisa energi: {energi}")
print(f"Waktu terpakai: {waktu_terpakai}")