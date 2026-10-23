class KarakterSurfer:
    def __init__(self, nama):
        # TODO 1: Inisialisasi properties (nama, skor = 0, koin = 0, is_running = True)
        self.nama = nama
        self.skor = 0
        self.koin = 0
        self.is_running = True

    def berlari(self):
        # TODO 2: Buat behavior agar karakter mulai berlari (cetak pesan dan ubah is_running menjadi True)
        self.is_running = True
        print(f"{self.nama} mulai berlari!")

    def ambil_koin(self, jumlah):
        # TODO 3: Tambahkan jumlah koin ke properties koin dan berikan output informasi
        self.koin += jumlah
        print(f"{self.nama} mengambil {jumlah} koin. Total koin sekarang: {self.koin}")

    def tabrak_rintangan(self):
        # TODO 4: Jika menabrak rintangan, ubah is_running menjadi False dan cetak pesan game over
        self.is_running = False
        print(f"{self.nama} menabrak rintangan! Game Over.")

    def info_player(self):
        # TODO 5: Cetak status terkini (nama, skor, jumlah koin, dan status berlari)
        print(f"Nama           : {self.nama}")
        print(f"Skor           : {self.skor}")
        print(f"Jumlah Koin    : {self.koin}")
        print(f"Status Berlari : {'Sedang Berlari' if self.is_running else 'Berhenti (Game Over)'} ({self.is_running})")


# --- PENGUJIAN OBJEK ---
print("=== UJI COBA SUBWAY SURF ===\n")

# Buat objek dengan nama variabel "player1" (misal: "Jake")
player1 = KarakterSurfer("Jake")
print(f"Objek Karakter Surfer '{player1.nama}' berhasil dibuat!\n")

print("=== EKSEKUSI METHOD ===")
# Memanggil method berlari()
player1.berlari()

# Memanggil method ambil_koin() beberapa kali
player1.ambil_koin(10)
player1.ambil_koin(20)

# Memanggil method tabrak_rintangan()
player1.tabrak_rintangan()

# Memanggil method info_player() untuk melihat hasil
print("\n=== INFO STATUS AKHIR ===")
player1.info_player()