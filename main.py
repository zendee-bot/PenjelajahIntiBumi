import os
from character import polisi,pocong, kuntilanak, kuyang, banispati
from senjata import  ketapel,keris,damagepocong, damagekuntilanak, damagebanispati, damagekuyang, Tombak

def angkainputulang(huruf=""):
    try:
        return int(input(huruf))
    except:
        os.system("cls")
        print ("{|=================================|}\n") 
        print("PENGEN MAIN ULANG GA ?\n 1. AKU MAU ULANG BANH..\n 2. UDAHAN AJA")
        print("YANG DIMASUKAN BUKAN ANGKA....\nisi kembali : ")
        return angkainputulang()

def angkadariinputsenajata(huruf=""):
    try:
        return int(input(huruf))
    except:
        os.system("cls")
        print ("{|=================================|}\n")
        print ("1. Keris\n2. Ketapel\n3. Tombak ")
        print ("Pilih senjata apa yang akan digunakan!!! \n")
        print("YANG DIMASUKAN BUKAN ANGKA....\nisi kembali : ")
        return angkadariinputsenajata()


def resetdarah (char):
     char.darah=char.darah_max


def maingame():
    os.system("cls")
    print ("{|=================================|}\n")
    charinput = input("Masukan Nama dari Karakter kamu : ")
    print ("1. Keris\n2. Ketapel\n3. Tombak ")
    print ("Pilih senjata apa yang akan digunakan : ")
    dipake = angkadariinputsenajata()


    if dipake == 1:
            polisii=polisi(name=charinput,darah=130)
            polisii.gunakan(keris)
    elif dipake == 2:
            polisii=polisi(name=charinput, darah=110)
            polisii.gunakan(ketapel)
    elif dipake == 3:
            polisii =polisi(name=charinput, darah=150)
            polisii.gunakan(Tombak)
    else :
        print ("TIDAK VALID")
        return

    Pocong = pocong (name="Pocong", darah=100, senjata=damagepocong)
    Kuntilanak = kuntilanak (name="Kuntilanak", darah=100, senjata=damagekuntilanak)
    Kuyang = kuyang (name="Kuyang", darah=100, senjata=damagekuyang)
    Banaspati = banispati (name="Banaspati", darah=100,senjata=damagebanispati)

    os.system("cls")
    print ("{|=================================|}\n")   
    print(f"{charinput} telah Masuk dalam sebuah GOA yang sangat MISTERIUS.\n\nLalu {charinput} Masuk dan Menjelajahinya karena Kamu Penasaran dengan INTI BUMI")
    print ("\n{|=================================|}")  
    input("Tekan Enter untuk melanjutkan...")

    os.system("cls")
    print ("{|=================================|}\n")
    print (f"Dalam perjalanan {charinput} bertemu sosok yang menghalangi perjalananmu\n   Wahh ituuu... \n\t\tPOCONGGG!!!")
    print ("\n{|=================================|}")
    input("Tekan Enter untuk melawan POCONG itu...")


    while Pocong.darah > 0 and polisii.darah > 0:
        os.system("cls") 
        print ("{|=================================|}")
        polisii.serang(Pocong)
        Pocong.serang(polisii)
        print ("\n<-------FIGHT------->")
        polisii.kotak_darah.gambar()
        Pocong.kotak_darah.gambar()
        print ("{|=================================|}")
        input("Tekan Enter untuk menyerang...")

    if polisii.darah <= 0:
        print(f"{polisii.name} telah kalah!")
    else:
        print(f"{Pocong.name} telah dikalahkan!")
        resetdarah(polisii)

        
    os.system("cls")
    print ("{|=================================|}\n")
    print (f"Wah Pocong itu akhirnya telah Kalah\n\t{charinput} menyebuhkan diri dengan RAMUAN yang di dapat dari POCONG")
    print ("\n{|=================================|}")
    input("Tekan Enter untuk melanjutkan...")
    os.system("cls")
    print ("{|=================================|}\n")
    print (f"Setelah sudah pulih {charinput} melanjutkan perjalanan ke tempat yang lebih dalam lagi ")
    print ("\n{|=================================|}")
    input("Tekan Enter untuk melanjutkan...")
    os.system("cls")
    print ("{|=================================|}\n")
    print (f"Dalam perjalanan {charinput} bertemu sosok yang menghalangi perjalananmu\nWahh ituuu... \n\t\tKUNTILANAK!!!")
    print ("\n{|=================================|}")
    input("Tekan Enter untuk melawan KUNTILANAK itu...")


    while Kuntilanak.darah > 0 and polisii.darah > 0:
        os.system("cls")
        print ("{|=================================|}")
        polisii.serang(Kuntilanak)
        Kuntilanak.serang(polisii)
        print ("<-------FIGHT----------->")
        polisii.kotak_darah.gambar()
        Kuntilanak.kotak_darah.gambar()
        print ("{|=================================|}")
        input("Tekan Enter untuk menyerang...")

    if polisii.darah <= 0:
        print(f"{polisii.name} telah kalah!")
    else:
        print(f"{Kuntilanak.name} telah dikalahkan!")
        resetdarah(polisii)

    os.system("cls")
    print ("{|=================================|}\n")
    print (f"Wah KUNTILANAK itu sudah dikalahkan\nLalu {charinput} menyebuhkan diri dengan RAMUAN yang di dapat dari KUNTILANAK")
    print ("\n{|=================================|}")
    input("Tekan Enter untuk melanjutkan...")
    os.system("cls")
    print ("{|=================================|}\n")
    print (f"Setelah sudah pulih {charinput} melihat sekitar apakah ada hal menarik lainnya.... ")
    print ("\n{|=================================|}")
    input("Tekan Enter untuk melanjutkan...")
    os.system("cls")
    print ("{|=================================|}\n")
    print (f"Ternyata tidak ada hal yang menarik.\n{charinput} pun langusung masuk ke daerah yang lebih dalam lagi.....  ")
    print ("\n{|=================================|}")
    input("Tekan Enter untuk melanjutkan...")
    os.system("cls")
    print ("{|=================================|}\n")
    print (f"Hah sepertinya ada sesuatu yang menunggu di depan....\n\tlalu {charinput} menghapirinyaa..")
    print ("\n{|=================================|}")
    input("Tekan Enter untuk melanjutkan...")
    os.system("cls")
    print ("{|=================================|}\n")
    print (f"Ternyta itu adalah KUYANG!!!!... ")
    print ("\n{|=================================|}")
    input("Tekan Enter untuk melawan KUYANG itu...")


    while Kuyang.darah > 0 and polisii.darah > 0:
        os.system("cls")    
        print ("{|=================================|}")
        polisii.serang(Kuyang)
        Kuyang.serang(polisii)
        print ("\n<-------FIGHT----------->")
        polisii.kotak_darah.gambar()
        Kuyang.kotak_darah.gambar()
        print ("{|=================================|}")
        input("Tekan Enter untuk menyerang...")

    if polisii.darah <= 0:
        print(f"{polisii.name} telah kalah!")
    else:
        print(f"{Kuyang.name} telah dikalahkan!")
        resetdarah(polisii)

    os.system("cls")
    print ("{|=================================|}\n")
    print (f"KUYANG itupum sudah dikalahkan\nLalu {charinput} menyebuhkan diri dengan RAMUAN yang di dapat dari KUYANG")
    print ("\n{|=================================|}")
    input("Tekan Enter untuk melanjutkan...")
    os.system("cls")
    print ("{|=================================|}\n")
    print (f"Setelah sudah pulih {charinput} melihat ada yang menarik di daerah paling bawah dari GOA itu... ")
    print ("\n{|=================================|}")
    input("Tekan Enter untuk melanjutkan...")
    os.system("cls")
    print ("{|=================================|}\n")
    print (f"{charinput}pun langusung masuk ke dalam lagi.....  ")
    print ("\n{|=================================|}")
    input("Tekan Enter untuk melanjutkan...")
    os.system("cls")
    print ("{|=================================|}\n")
    print (f"Sepertinya {charinput} sudah menemukan apa yang ingin dicarinya...\n \ttetapi....\nApa yang dicari teryata dijaga oleh...")
    print ("\n{|=================================|}")
    input("Tekan Enter untuk melanjutkan...")
    os.system("cls")
    print ("{|=================================|}\n")
    print ("\tBANASPATI!!!!......")
    print ("\n{|=================================|}")
    input("Tekan Enter untuk melawan BANASPATI itu...")


    while Banaspati.darah > 0 and polisii.darah > 0:
        os.system("cls")   
        print ("{|=================================|}")
        polisii.serang(Banaspati)
        Banaspati.serang(polisii)
        print ("\n<-------FIGHT----------->")
        polisii.kotak_darah.gambar()
        Banaspati.kotak_darah.gambar()
        print ("{|=================================|}")
        input("Tekan Enter untuk menyerang...")

    if polisii.darah <= 0:
        print(f"{polisii.name} telah kalah!")
    else:
        print(f"{Banaspati.name} telah dikalahkan!")
        resetdarah(polisii)

    if polisii.darah > 0:
        print(f"{polisii.name} telah mengalahkan semua musuh!")
    else:
        print(f"{polisii.name} telah kalah dalam pertarungan!")

    os.system("cls")
    print ("{|=================================|}\n")
    print (f"Akhirnya BANASPATI itu kalah juga\nLalu {charinput} langsung pergi untuk melihat INTI BUMI ")
    print ("\n{|=================================|}")
    input("Tekan Enter untuk melanjutkan...")
    os.system("cls")
    print ("{|=================================|}\n")
    print ("Ternyata di dalam\n\t INTI BUMI\n\t ADAAAAAAA......")
    print ("\n{|=================================|}")
    input("Tekan Enter untuk melanjutkan...")
    os.system("cls")
    print ("{|=================================|}\n")
    print ("Dunia baru yang penuh dengan keajaiban dan rahasia yang belum terungkap.")
    print ("\n{|=================================|}")
    input("Tekan Enter untuk melanjutkan...")
    os.system("cls")
    print ("{|=================================|}\n")
    print ("\t TERIMA KASIH SUDAH BERMAIN")
    print ("\n{|=================================|}")
    input("Tekan Enter untuk melanjutkan...")

os.system("cls")
print ("{|=================================|}")  
print ("\tSelamat Datang di Game\n\tPENJELAJAH INTI BUMI")
print ("{|=================================|}")  
input("Tekan Enter untuk melanjutkan...")  

while True:
    maingame()
    os.system("cls")
    print ("{|=================================|}\n") 
    print("PENGEN MAIN ULANG GA ?\n 1. AKU MAU ULANG BANH..\n 2. UDAHAN AJA")
    ulang = angkainputulang()
    
    if ulang == 2:  # Jika pemain memilih 2, keluar dari loop
        break