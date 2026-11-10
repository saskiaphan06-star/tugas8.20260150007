import modul_sensor

log_kebun = [] # berisi tuple (suhu, kelembaban)


def input_angka(pesan, minimum, maksimum):
    """Meminta input angka dengan validasi tipe data rentang."""
    while True:
        try:
            nilai = float(input(pesan))
            if minimum <= nilai <= maksimum:
                return nilai
            print(f" [!] Nilai harus antara {minimum} dan {maksimum}. ")
        except ValueError:
            print(" [!] Input tidak valid. Masukkan angka, bukan huruf.")

def input_sensor():
    """Mengembalikan tuple (suhu, kelembaban) yang sudah tervalidasi."""
    suhu = input_angka("Masukkan Suhu Udara (0-100 C) :", 0,100)
    lembab = input_angka("Masukkan Kelembaban Tanah (0-100 %) :", 0,100)
    return (suhu, lembab)

def rekam_data():
    data = input_sensor()
    log_kebun.append(data)
    print(f"Data berhasil direkam: Suhu {data[0]} C, {data[1]} %")

def analisis_tren():
    if len(log_kebun) == 0:
        print("Belum ada data. Silahkan rekam data terlebih dahulu (menu 1). ")
        return

    # Slicing: maksimal 3 data terakhir
    tiga_terakhir = log_kebun[-3:]

    print(f"\nLokasi: {modul_sensor.LOKASI[0]}") 
    print(f"{modul_sensor.LOKASI[1], {modul_sensor.LOKASI[2]}}")
    print(f"--- {len(tiga_terakhir)} Data Terakhir ---")
    for i, (suhu, lembab) in enumerate(tiga_terakhir, start=1):
        print(f"{i}. Suhu: {suhu} C | Kelembaban: {lembab} %")

    rata_suhu, rata_lembab = modul_sensor.hitung_tren(tiga_terakhir)
    print(f"\n Rata-rata Suhu: {rata_suhu:.2f} C")
    print(f"Rata-rata Kelembaban: {rata_lembab:.2f} %")

    status = modul_sensor.evalusi_irigasi(rata_suhu, rata_lembab, modul_sensor.AMBANG_KITIS)
    print(f"Satus Irigasi : {status}")

def main():
    while True:
        print("\n === MONITORING IoI KAMPUNG ANGGUR PLUMBUNGAN ===")
        print("[1] Rekam Data")
        print("[2] Analisis Tren (3 Terakhir)")
        print("[3] Keluar")
        pilihan = input("Pilih Menu:").strip()

        if pilihan == "1":
            rekam_data()
        elif pilihan == "2":
            analisis_tren()
        elif pilihan == "3":
            print("Terima Kasih. Progam Selesai.")
            break 
        else:
            print("Pilihan tidak valid. Pilih 1, 2, atau 3.")

if __name__ == "__main__":
    main()




        