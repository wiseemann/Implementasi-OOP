class KatakZuma:
    def __init__(self, warna_awal):
        self.warna_peluru = warna_awal
        self.skor = 0
        self.is_active = True

    def ganti_warna(self, warna_baru):
        self.warna_peluru = warna_baru
        print(f"Mengganti warna peluru menjadi: {self.warna_peluru}")

    def tembak(self, bola_target=None):
        if not self.is_active:
            print("Katak tidak aktif, tidak bisa menembak!")
            return

        # Jika bola_target tidak diberikan, gunakan warna default peluru saat ini
        if bola_target is None:
            bola_target = self.warna_peluru

        print(f"Menembak bola target '{bola_target}' dengan peluru '{self.warna_peluru}'")
        if self.warna_peluru == bola_target:
            self.skor += 50
            print("-> Tepat sasaran! (+50 skor)")
        else:
            self.skor -= 10
            if self.skor < 0:
                self.skor = 0
            print("-> Warna tidak cocok! (-10 skor)")
        self.bola_target = bola_target

    def info_status(self):
        print(f"Warna Peluru: {self.warna_peluru}")
        print(f"Skor: {self.skor}")
        print(f"Status: {'Aktif' if self.is_active else 'Tidak Aktif'}")

print("=== UJI COBA ZUMA ===\n")

k_merah = KatakZuma("Merah")
print("Objek Katak Merah berhasil dibuat!\n")

print("=== EKSEKUSI METHOD ===")
# Memanggil method tembak beberapa kali (warna cocok & tidak cocok)
k_merah.tembak("Merah")
k_merah.tembak("Kuning")

# Mengganti warna peluru
k_merah.ganti_warna("Biru")

# Memanggil method tembak lagi
k_merah.tembak("Biru")

print("\n=== INFO STATUS AKHIR ===")
# Memanggil method info_status untuk melihat hasil
k_merah.info_status()
