class Monster:
    def __init__(self, nama, tipe_monster):
        self.nama = nama
        self.tipe_monster = tipe_monster
        self.health = 100
        self.is_alive = True
        self.damage = 20

    def menyerang(self, target):
        if self.is_alive:
            target.health -= self.damage
            print(f"{self.nama} [{self.tipe_monster}] menyerang {target.nama} dan memberikan {self.damage} damage!")
            target.cek_status()
        else:
            print(f"{self.nama} tidak bisa menyerang karena telah dikalahkan.")

    def cek_status(self):
        if self.health <= 0:
            self.health = 0
            self.is_alive = False
            print(f"-> {self.nama} telah dikalahkan! (Health: 0)")
        else:
            print(f"-> Sisa health {self.nama}: {self.health}")

    def info_monster(self):
        print(f"Nama Monster : {self.nama}")
        print(f"Tipe/Elemen  : {self.tipe_monster}")
        print(f"Health       : {self.health}")
        print(f"Damage Serang: {self.damage}")
        print(f"Status Hidup : {'Masih Hidup' if self.is_alive else 'Kalah/Mati'}")


# --- PENGUJIAN OBJEK ---
if __name__ == "__main__":
    print("=== UJI COBA SISTEM PERTARUNGAN MONSTER RPG ===\n")

    # 1. Instansiasi Objek
    monster1 = Monster("Naga", "Api")
    monster2 = Monster("Golem", "Batu")

    print("Status Awal Monster:")
    monster1.info_monster()
    print("-" * 30)
    monster2.info_monster()
    print("\n" + "=" * 40 + "\n")

    print("=== PERTARUNGAN DIMULAI ===")
    # Ronde 1: Saling serang
    print("[Ronde 1]")
    monster1.menyerang(monster2)
    monster2.menyerang(monster1)

    # Ronde 2 & seterusnya hingga salah satu kalah
    print("\n[Ronde 2 - Serangan Beruntun dari Draco]")
    monster1.menyerang(monster2)
    monster1.menyerang(monster2)
    monster1.menyerang(monster2)
    monster1.menyerang(monster2)

    # Mencoba menyerang kembali setelah kalah
    print("\n[Uji Coba Serangan Monster yang Sudah Kalah]")
    monster2.menyerang(monster1)

    print("\n=== STATUS AKHIR ===")
    print("Status Naga:")
    monster1.info_monster()
    print("\nStatus Golem:")
    monster2.info_monster()