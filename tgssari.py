def hitung_nilai(pengalaman, wawancara, bidang_pilihan):
    bonus = 0
    pengalaman = pengalaman.lower()
    if "ketua" in pengalaman:
        bonus += 2
    if bidang_pilihan.lower() in pengalaman:
        bonus += 3
    return wawancara + bonus

def urutkan_descending(data_list):
    n = len(data_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data_list[j]['nilai'] < data_list[j + 1]['nilai']:
                data_list[j], data_list[j + 1] = data_list[j + 1], data_list[j]
    return data_list

def input_data_cakoor():
    jumlah = int(input("Masukkan jumlah cakoor: "))
    data_per_bidang = {
        "Acara": [],
        "Pubdok": [],
        "Perlengkapan": [],
        "Danus": []
    }
    for i in range(jumlah):
        print(f"\nData cakoor ke-{i+1}")
        nama = input("Nama: ")
        nim = input("NIM: ")
        kelas = input("Kelas: ")
        pengalaman = input("Pengalaman kepanitiaan: ")
        wawancara = int(input("Nilai wawancara (0-100): "))
        bidang = input("Pilihan bidang (Acara/Pubdok/Perlengkapan/Danus): ")

        nilai_akhir = hitung_nilai(pengalaman, wawancara, bidang)
        data = {
            "nama": nama,
            "nim": nim,
            "kelas": kelas,
            "nilai": nilai_akhir
        }

        if bidang in data_per_bidang:
            data_per_bidang[bidang].append(data)
        else:
            print("Bidang tidak valid, data tidak dimasukkan.")

    return data_per_bidang

def tampilkan_hasil(data_per_bidang):
    print("\n=== Hasil Seleksi Koordinator PSB 22 ===\n")
    hasil_output = "=== Hasil Seleksi Koordinator PSB 22 ===\n\n"

    for bidang in data_per_bidang:
        print(f"Bidang {bidang}:")
        hasil_output += f"Bidang {bidang}:\n"
        daftar = urutkan_descending(data_per_bidang[bidang])
        for i in range(min(2, len(daftar))):
            d = daftar[i]
            output_line = f"  {i+1}. {d['nama']} ({d['nim']}) - Nilai: {d['nilai']}"
            print(output_line)
            hasil_output += output_line + "\n"
        print()
        hasil_output += "\n"

    # Simpan ke file
    with open("OrPSB22.txt", "w") as file:
        file.write(hasil_output)

# Main Program
data_bidang = input_data_cakoor()
tampilkan_hasil(data_bidang)
