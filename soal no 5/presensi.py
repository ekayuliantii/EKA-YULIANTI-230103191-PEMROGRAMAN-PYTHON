from pathlib import Path
import csv
import json
import logging

# --- 1) Atur logging sederhana ---
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

# --- 2) Membuat folder data (jika belum ada) ---
try:
    data_path = Path("data")
    # Cek dulu apakah sudah ada sebelum membuat
    if data_path.exists():
        logging.info("Folder 'data' sudah ada.")
    else:
        data_path.mkdir(exist_ok=True)
        logging.info("Folder 'data' berhasil dibuat.")
except Exception as e:
    logging.error(f"Gagal membuat folder 'data': {e}")

# --- 3) Menulis CSV data/presensi.csv ---
csv_path = data_path / "presensi.csv"

try:
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["nim", "nama", "hadir_uts"])
        writer.writerow(["230103191", "Eka Yulianti", 1])
        writer.writerow(["12346", "Siti", 0])
        writer.writerow(["12347", "Andi", 1])
    logging.info("File presensi.csv berhasil dibuat.")
except Exception as e:
    logging.error(f"Gagal menulis file 'presensi.csv': {e}")

# --- 4) Membaca CSV dan menghitung ringkasan ---
try:
    logging.info("Membaca file presensi.csv...")
    total = 0
    hadir = 0

    with csv_path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total += 1
            if int(row["hadir_uts"]) == 1:
                hadir += 1

    persentase = (hadir / total * 100) if total > 0 else 0

    # Tampilkan hasil ringkasan di terminal
    print(f"\nTotal data : {total}")
    print(f"Hadir      : {hadir}")
    print(f"Persentase : {round(persentase, 2)}%\n")

    ringkasan = {
        "total_mahasiswa": total,
        "hadir": hadir,
        "persentase_hadir": round(persentase, 2)
    }

except Exception as e:
    logging.error(f"Gagal membaca/menghitung dari CSV: {e}")
    ringkasan = {}

# --- 5) Menyimpan hasil ke JSON data/ringkasan.json ---
json_path = data_path / "ringkasan.json"

try:
    logging.info("Menyimpan ringkasan ke ringkasan.json...")
    with json_path.open("w", encoding="utf-8") as f:
        json.dump(ringkasan, f, indent=4)
    logging.info("Ringkasan berhasil disimpan ke data/ringkasan.json.")
except Exception as e:
    logging.error(f"Gagal menulis file 'ringkasan.json': {e}")