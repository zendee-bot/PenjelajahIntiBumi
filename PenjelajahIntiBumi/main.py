import os
from character import polisi, pocong, kuntilanak, kuyang, banispati
from senjata import ketapel, keris, damagepocong, damagekuntilanak, damagebanispati, damagekuyang, Tombak
from ceritagame import ceritag
from sidefungsi import angkainputulang, angkadariinputsenajata, resetdarah, berantem, versus

cerita = ceritag()

def maingame():
    os.system('cls')
    cerita.pembatass()
    cerita.charinput = input("Masukan Nama dari Karakter kamu : ")
    cerita.pilihsenjata()
    dipake = angkadariinputsenajata()

    if dipake == 1:
        polisii = polisi(name=cerita.charinput, darah=130)
        senjata_awal=keris
    elif dipake == 2:
        polisii = polisi(name=cerita.charinput, darah=110)
        senjata_awal=ketapel
    elif dipake == 3:
        polisii = polisi(name=cerita.charinput, darah=150)
        senjata_awal=Tombak

    polisii.gunakan(senjata_awal)

    Pocong = pocong(name="Pocong", darah=100, senjata=damagepocong)
    Kuntilanak = kuntilanak(name="Kuntilanak", darah=100, senjata=damagekuntilanak)
    Kuyang = kuyang(name="Kuyang", darah=100, senjata=damagekuyang)
    Banaspati = banispati(name="Banaspati", darah=100, senjata=damagebanispati)

    cerita.cerita1()

    # LAWAN POCONG
    versus(polisii, Pocong)
    while Pocong.darah > 0 and polisii.darah > 0:
        berantem(polisii, Pocong, senjata_awal)
    if polisii.darah == 0:
        cerita.kalahh()
        input("Tekan Enter untuk melanjutkan...")
        return False  # Player lost

    resetdarah(polisii)
    cerita.cerita2()

    # LAWAN KUNTILANAK
    versus(polisii, Kuntilanak)
    while Kuntilanak.darah > 0 and polisii.darah > 0:
        berantem(polisii, Kuntilanak, senjata_awal)
    if polisii.darah == 0:
        cerita.kalahh()
        input("Tekan Enter untuk melanjutkan...")
        return False  # Player lost

    resetdarah(polisii)
    cerita.cerita3()

    # LAWAN KUYANG
    versus(polisii, Kuyang)
    while Kuyang.darah > 0 and polisii.darah > 0:
        berantem(polisii, Kuyang, senjata_awal)
    if polisii.darah == 0:
        cerita.kalahh()
        input("Tekan Enter untuk melanjutkan...")
        return False  # Player lost

    resetdarah(polisii)
    cerita.cerita4()

    # LAWAN BANASPATI
    versus(polisii, Banaspati)
    while Banaspati.darah > 0 and polisii.darah > 0:
        berantem(polisii, Banaspati, senjata_awal)
    if polisii.darah == 0:
        cerita.kalahh()
        input("Tekan Enter untuk melanjutkan...")
        return False  # Player lost

    print(f"{Banaspati.name} telah dikalahkan!")
    resetdarah(polisii)

    if polisii.darah > 0:
        print(f"{polisii.name} telah mengalahkan semua musuh!")
        cerita.ending()
    else:
        print(f"{polisii.name} telah kalah dalam pertarungan!")

os.system('cls')
cerita.judul()
input("Tekan Enter untuk melanjutkan...")

while True:
    result = maingame()
    if result == False:
    
        os.system("cls")
        print("{|=================================|}\n")
        print("PENGEN MAIN ULANG GA?\n 1. AKU MAU ULANG BANH..\n 2. UDAHAN AJA")
        ulang = angkainputulang()

    if ulang != 1:
        break
