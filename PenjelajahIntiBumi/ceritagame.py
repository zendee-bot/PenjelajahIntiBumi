import os


class ceritag:
    jeniswarna:dict ={"brown":"\33[33m", "reset":"\033[0m"}
    pembatas:str = "\n{|=================================|}\n"
    selamatan:str = "\n\tSelamat Datang di Game\n\tPENJELAJAH INTI BUMI\n"

    kalah:str="\n\tKAMU KALAH BROKSSS !!\n"
    pilihansenjata:str="\n1. Keris\n2. Ketapel\n3. Tombak\nPilih senjata apa yang akan digunakan :  "

    teks1_1:str="\n{charinput} telah Masuk dalam sebuah GOA yang sangat MISTERIUS.\n\nLalu {charinput} Masuk dan Menjelajahinya karena Kamu Penasaran dengan INTI BUMI\n"
    teks1_2:str="\nDalam perjalanan {charinput} bertemu sosok yang menghalangi perjalananmu\n   Wahh ituuu... \n\t\tPOCONGGG!!!\n"    
    
    teks2_1:str="\nWah Pocong itu akhirnya telah Kalah\n\t{charinput} menyebuhkan diri dengan RAMUAN yang di dapat dari POCONG\n"
    teks2_2:str="\nSetelah sudah pulih {charinput} melanjutkan perjalanan ke tempat yang lebih dalam lagi\n "
    teks2_3:str="\nDalam perjalanan {charinput} bertemu sosok yang menghalangi perjalananmu\nWahh ituuu... \n\t\tKUNTILANAK!!!\n"

    teks3_1:str="\nWah KUNTILANAK itu sudah dikalahkan\nLalu {charinput} menyebuhkan diri dengan RAMUAN yang di dapat dari KUNTILANAK\n"
    teks3_2:str="\nSetelah sudah pulih {charinput} melihat sekitar apakah ada hal menarik lainnya.... \n"
    teks3_3:str="\nTernyata tidak ada hal yang menarik.\n{charinput} pun langusung masuk ke daerah yang lebih dalam lagi.....  \n"
    teks3_4:str="\nHah sepertinya ada sesuatu yang menunggu di depan....\n\tlalu {charinput} menghapirinyaa..\n"
    teks3_5:str="\nTernyta itu adalah KUYANG!!!!... \n"

    teks4_1:str="\nKUYANG itupum sudah dikalahkan\nLalu {charinput} menyebuhkan diri dengan RAMUAN yang di dapat dari KUYANG\n"
    teks4_2:str="\nSetelah sudah pulih {charinput} melihat ada yang menarik di daerah paling bawah dari GOA itu... \n"
    teks4_3:str="\n{charinput}pun langusung masuk ke dalam lagi.....  \n"
    teks4_4:str="\nSepertinya {charinput} sudah menemukan apa yang ingin dicarinya...\n \ttetapi....\nApa yang dicari teryata dijaga oleh...\n"
    teks4_5:str="\n\tBANASPATI!!!!......\n"

    ending_1:str="\nAkhirnya BANASPATI itu kalah juga\nLalu {charinput} langsung pergi untuk melihat INTI BUMI \n"
    ending_2:str="\nTernyata di dalam\n\t INTI BUMI\n\t ADAAAAAAA......\n"
    ending_3:str="\nDunia baru yang penuh dengan keajaiban dan rahasia yang belum terungkap.\n"
    ending_4:str="\n\t TERIMA KASIH SUDAH BERMAIN\n"

    #JUDUL + CERITA

    def judul (self):
        os.system('cls')
        print(self.pembatas , self.selamatan , self.pembatas)
    def pilihsenjata(self):
        print(self.pilihansenjata)

    def cerita1_1(self):
        os.system('cls')
        print(self.pembatas , self.teks1_1.format(charinput=self.charinput), self.pembatas)
    def cerita1_2(self):
        os.system('cls')
        print(self.pembatas , self.teks1_2.format(charinput=self.charinput), self.pembatas)

    def cerita2_1(self):
        os.system('cls')
        print(self.pembatas , self.teks2_1.format(charinput=self.charinput), self.pembatas)
    def cerita2_2(self):
        os.system("cls")
        print(self.pembatas , self.teks2_2.format(charinput=self.charinput), self.pembatas)
    def cerita2_3(self):
        os.system('cls')
        print(self.pembatas , self.teks2_3.format(charinput=self.charinput), self.pembatas)

    def cerita3_1(self):
        os.system('cls')
        print(self.pembatas , self.teks3_1.format(charinput=self.charinput), self.pembatas)
    def cerita3_2(self):
        os.system('cls')
        print(self.pembatas , self.teks3_2.format(charinput=self.charinput), self.pembatas)
    def cerita3_3(self):
        os.system('cls')
        print(self.pembatas , self.teks3_3.format(charinput=self.charinput), self.pembatas)
    def cerita3_4(self):
        os.system('cls')
        print(self.pembatas , self.teks3_4.format(charinput=self.charinput), self.pembatas)
    def cerita3_5(self):
        os.system('cls')
        print(self.pembatas , self.teks3_5, self.pembatas)

    def cerita4_1(self):
        os.system('cls')
        print(self.pembatas , self.teks4_1.format(charinput=self.charinput), self.pembatas)
    def cerita4_2(self):
        os.system('cls')
        print(self.pembatas , self.teks4_2.format(charinput=self.charinput), self.pembatas)
    def cerita4_3(self):
        os.system('cls')
        print(self.pembatas , self.teks4_3.format(charinput=self.charinput), self.pembatas)
    def cerita4_4(self):
        os.system('cls')
        print(self.pembatas , self.teks4_4.format(charinput=self.charinput), self.pembatas)
    def cerita4_5(self):
        os.system('cls')
        print(self.pembatas , self.teks4_5, self.pembatas)

    def ending1(self):
        os.system('cls')
        print(self.pembatas , self.ending_1.format(charinput=self.charinput), self.pembatas)
    def ending2(self):
        os.system('cls')
        print(self.pembatas , self.ending_2, self.pembatas)
    def ending3(self):
        os.system('cls')
        print(self.pembatas , self.ending_3, self.pembatas)
    def ending4(self):
        os.system('cls')
        print(self.pembatas , self.ending_4, self.pembatas)

    def kalahh(self):
        os.system('cls')
        print (self.pembatas , self.kalah, self.pembatas)

    #ATRIBUT TAMBAHAN
    def __init__(self, charinput=""):
        self.charinput = charinput
    def pembatass(self):
        print(self.pembatas)