from senjata import TanganKosong
from kotak_darah import kotakdarah


class char:

    def __init__(self, name: str, darah: int) -> None :
        self.name = name
        self.darah = darah
        self.darah_max=darah

        self.senjata = TanganKosong

    def serang (self, target ) -> None:
        target.darah -= self.senjata.damage
        target.darah = max(target.darah, 0)
        target.kotak_darah.update()
        print (f"{self.name} memeberikan {self.senjata.damage} damage ke {target.name} dengan {self.senjata.name}")

class polisi(char):
    def __init__(self, name:str, darah:int)->None:
        super().__init__(name=name, darah=darah)
        self.senjata_biasa = TanganKosong
        self.kotak_darah = kotakdarah(self, warna = "green")

    def gunakan(self,senjata)-> None:
        self.senjata=senjata
        print (f"{self.name} menggunakan {self.senjata.name} !")

    def menjatuhkan(self) -> None:
        print (f"{self.name} menjatuhkan {self.senjata.name} !")
        self.senjata = self.senjata_biasa

class pocong(char):
    def __init__(self, name:str, darah:int, senjata)->None:
        super().__init__(name=name, darah=darah)
        self.senjata=senjata
        self.kotak_darah = kotakdarah(self, warna = "yellow")

class kuntilanak(char):
    def __init__(self, name:str, darah:int, senjata)->None:
        super().__init__(name=name, darah=darah)
        self.senjata=senjata
        self.kotak_darah = kotakdarah(self, warna = "purple")

class kuyang(char):
    def __init__(self, name:str, darah:int, senjata)->None:
        super().__init__(name=name, darah=darah)
        self.senjata=senjata
        self.kotak_darah = kotakdarah(self, warna = "blue")

class banispati(char):
    def __init__(self, name:str, darah:int, senjata)->None:
        super().__init__(name=name, darah=darah)
        self.senjata=senjata
        self.kotak_darah = kotakdarah(self, warna = "red")