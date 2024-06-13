import os

os.system("")


class kotakdarah:
    simbol_menunggu: str = "█"
    simbol_hilang: str = "_"
    tembok: str = "|"
    jeniswarna:dict ={"red":"\033[91m", "purple":"\33[95m","blue":"\33[34m", "green":"\033[92m", "default":"\033[0m", "yellow":"\33[93m"}

    def __init__(self,entity,panjang: int = 20, diwarnai:bool=True, warna: str ="")-> None:
        self.entity = entity
        self.panjang = panjang
        self.darahpenuh = entity.darah_max
        self.darahsekarang = entity.darah

        self.diwarnai = diwarnai
        self.warna = self.jeniswarna.get(warna) or self.jeniswarna["default"]

    def update(self) -> None:
        self.darahsekarang=self.entity.darah

    def gambar(self)-> None:
        remaining_bars = round(self.darahsekarang / self.darahpenuh * self.panjang )
        lost_bars = self.panjang - remaining_bars
        print (f"{self.entity.name} Darah : {self.entity.darah}/{self.entity.darah_max}")
        print (f"{self.tembok}"
        f"{self.warna if self.diwarnai else ''}"
        f"{remaining_bars * self.simbol_menunggu}"
        f"{lost_bars * self.simbol_hilang}"
        f"{self.jeniswarna ['default'] if self.diwarnai else ''}"
        f"{self.tembok}")
