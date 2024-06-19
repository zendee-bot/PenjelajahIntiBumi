import random

class Senjata:
    def __init__(self, name: str, senjata_tipe: str, min_damage: int, max_damage: int, value: int) -> None:
        self.name = name
        self.senjata_tipe = senjata_tipe
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.value = value

    def damage(self):
        return random.randint(self.min_damage, self.max_damage)

# Define weapons
keris = Senjata(name="Keris", senjata_tipe="Tajam", min_damage=10, max_damage=20, value=0)
ketapel = Senjata(name="Ketapel", senjata_tipe="Jarak Jauh", min_damage=15, max_damage=25, value=0)
Tombak = Senjata(name="Tombak", senjata_tipe="Tidak Tajam", min_damage=10, max_damage=18, value=0)
TanganKosong = Senjata(name="Tangan Kosong", senjata_tipe="Tumpul", min_damage=0, max_damage=0, value=0)
damagepocong = Senjata(name="Kuasa Gelap", senjata_tipe="Sihir", min_damage=10, max_damage=20, value=0)
damagekuntilanak = Senjata(name="Kuasa Gelap", senjata_tipe="Sihir", min_damage=12, max_damage=22, value=0)
damagekuyang = Senjata(name="Kuasa Gelap", senjata_tipe="Sihir", min_damage=15, max_damage=25, value=0)
damagebanispati = Senjata(name="Kuasa Gelap", senjata_tipe="Sihir", min_damage=20, max_damage=30, value=0)
Juruspambungkas = Senjata(name="Jurus Pambungkas", senjata_tipe="Keahlian", min_damage=38, max_damage=38, value=0)
