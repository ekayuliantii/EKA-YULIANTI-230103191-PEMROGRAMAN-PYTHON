def main():
    try:
        # Input tiga setoran dari user
        setoran1 = int(input("Masukkan setoran pertama: "))
        setoran2 = int(input("Masukkan setoran kedua: "))
        setoran3 = int(input("Masukkan setoran ketiga: "))
    except ValueError:
        # Jika input bukan angka, tampilkan error
        print("Input tidak valid. Harus berupa angka.")
        return

    # Cek apakah ada setoran bernilai 0
    if setoran1 <= 0 or setoran2 <= 0 or setoran3 <= 0:
        print("Input tidak valid.")
        return

    # Hitung total setoran
    total = setoran1 + setoran2 + setoran3
    print(f"Total setoran: {total}")

    # Klasifikasi total dengan if–elif–else
    if total < 300000:
        # Jika total kurang dari 300 ribu
        print("Keterangan: Rendah")
    elif 300000 <= total <= 600000:
        # Jika total antara 300 ribu dan 600 ribu
        print("Keterangan: Sedang")
    else:
        # Jika lebih dari 600 ribu
        print("Keterangan: Tinggi")

if __name__ == "__main__":
    main()

