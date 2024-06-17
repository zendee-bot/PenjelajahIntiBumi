import os
from ceritagame import ceritag
from senjata import Juruspambungkas
cerita = ceritag()

def angkainputulang(huruf=""):
    try:
        return int(input(huruf))
    except:
        os.system("cls")
        cerita.pembatass() 
        print("PENGEN MAIN ULANG GA ?\n 1. AKU MAU ULANG BANH..\n 2. UDAHAN AJA")
        print("YANG DIMASUKAN BUKAN ANGKA....\nisi kembali : ")
        return angkainputulang()

def angkadariinputsenajata(huruf=""):
    try:
        return int(input(huruf))
    except:
        os.system("cls")
        cerita.pembatass()
        cerita.pilihsenjata()
        print("YANG DIMASUKAN BUKAN ANGKA....\nisi kembali : ")
        return angkadariinputsenajata()

def angkainputulangjurus(huruf=""):
    try:
        return int(input(huruf))
    except:
        os.system("cls")
        cerita.pembatass() 
        print ("Pilih serangan: 1. Serang biasa 2. Jurus Pambungkas\nPilihan: ")
        print("YANG DIMASUKAN BUKAN ANGKA....\nisi kembali : ")
        return angkainputulangjurus()

def resetdarah (char):
     char.darah=char.darah_max

def tanyapakejurus(polisii, enemy):
    choice = angkainputulangjurus("Pilih serangan: 1. Serang biasa 2. Jurus Pambungkas\nPilihan: ")
    if choice == '2':
        polisii.gunakan(Juruspambungkas)
        polisii.serang(enemy, special=True)
    else:
        polisii.serang(enemy)

def berantem(polisii, enemy):
        os.system("cls") 
        cerita.pembatass()
        polisii.serang(enemy)
        enemy.serang(polisii)
        print ("\n<-------FIGHT------->")
        polisii.kotak_darah.gambar()
        enemy.kotak_darah.gambar()
        cerita.pembatass()
        input("Tekan Enter untuk menyerang...")

