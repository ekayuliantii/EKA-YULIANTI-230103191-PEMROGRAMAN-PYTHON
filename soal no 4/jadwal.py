# List jadwal kuliah, berisi string "Hari: Mata Kuliah"
jadwal = [
    "Senin: Teknik Digital",
    "Selasa: Pemrograman Web",
    "Rabu: Basis Data",
    "Kamis: Jaringan Komputer",
    "Jumat: Sistem Operasi"
]

def jadwal_hari(hari):
    """
    Menampilkan jadwal berdasarkan nama hari.
    Pencarian dilakukan dengan mengecek satu per satu isi list.
    """
    # Loop melalui semua item dalam list jadwal
    for item in jadwal:
        # Jika nama hari ditemukan di item (misalnya "Selasa")
        if hari in item:
            return item   # Kembalikan string jadwal yang sesuai
    # Jika tidak ada hari yang cocok (diletakkan di luar loop)
    return f"{hari}: Tidak ada jadwal pada hari tersebut."

# Contoh pemanggilan fungsi
print(jadwal_hari("Selasa"))   # Output: "Selasa: Pemrograman Web"
print(jadwal_hari("Minggu"))   # Output: "Minggu: Tidak ada jadwal pada hari tersebut."
