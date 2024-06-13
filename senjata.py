class senjata:
    def __init__(self, name: str, senjata_tipe: str, damage: int, value: int) -> None:
        self.name = name
        self.senjata_tipe = senjata_tipe
        self.damage = damage
        self.value = value

keris = senjata(name = "Keris", senjata_tipe="Tajam", damage=15, value=0)
ketapel = senjata(name = "Ketapel", senjata_tipe="Jarak Jauh", damage=20, value=0)
Tombak = senjata(name = "Tombak", senjata_tipe="Tidak Tajam", damage=10, value=0)
TanganKosong = senjata(name = "Tangan Kosong", senjata_tipe="Tumpul", damage=5, value=0)
damagepocong=senjata(name = "Kuasa Gelap", senjata_tipe="Tajam", damage=8, value=0)
damagekuntilanak=senjata(name = "Kuasa Gelap", senjata_tipe="Tajam", damage=10, value=0)
damagekuyang=senjata(name = "Kuasa Gelap", senjata_tipe="Tajam", damage=12, value=0)
damagebanispati=senjata(name = "Kuasa Gelap", senjata_tipe="Tajam", damage=14, value=0)