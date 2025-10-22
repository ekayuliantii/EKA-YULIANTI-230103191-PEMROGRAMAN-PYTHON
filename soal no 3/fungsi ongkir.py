tarif_dasar = {
    "Jakarta": 10000,
    "Bandung": 12000,
    "Surabaya": 15000,
    "Yogyakarta": 13000
}

def hitung_ongkir(berat_kg, kota, asuransi=False):

    """
    Menghitung ongkir RapidSend berdasarkan kota, berat, dan opsi asuransi.
    """
    ongkir = tarif_dasar[kota] + (2000 * berat_kg)
    if asuransi:
        ongkir += 3000
    return ongkir

# Contoh pemanggilan
print(hitung_ongkir(2, "Jakarta"))           
print(hitung_ongkir(5, "Surabaya", True))    
