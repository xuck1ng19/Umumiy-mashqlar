
##Shohjahon G'aybullayev  30.10.2024 21:32 start
##finish 31.10.2024 06:49
class auto_salon:
    def __init__(self, name, year, number, result) -> None:
        self.name=name
        self.year=year
        self.number=number
        self.result=result
    def get_info(self):
        x=f"{self.name} nomi Auto salomimiz {self.year}-yildan buyun ishlamoqda hozirda {self.number} "
        x+=f" automobillarimiz bor va shu paytgacha {self.result} ta automobillarni sotganmiz"
        return x
    
class firma(auto_salon):
    def __init__(self, name, year, number, result, address, p_number,auto) -> None:
        super().__init__(name, year, number, result)
        self.address=address
        self.p_number=p_number
        self.auto=auto
    def get_p_number(self):
        return self.p_number
    def get_info1(self):
        x=f"{self.name} nomi Auto zavodimiz {self.year}-yildan buyun ishlamoqda hozirda {self.number} "
        x+=f" automobillarimiz bor va shu paytgacha {self.result} ta automobillarni sotganmiz bizning manzil" 
        x+=f"{self.address} bizda {self.p_number}ta odamlar ishlaydi"
        return x
class auto():
    def __init__(self, nexia3, cobalt, lasetti, kaptiva, malibu, kia) -> None:
        self.nexia3=nexia3
        self.cobalt=cobalt
        self.lasetti=lasetti
        self.kaptiva=kaptiva
        self.malibu=malibu
        self.kia=kia
    def get_auto(self):
        y=f"Bizning automobillarimiz, {self.nexia3} , {self.cobalt}, {self.lasetti}, {self.kaptiva}, "
        y+=f"{self.malibu}, {self.kia} automobillarimiz bor"
        return y

class autolar():
    def __init__(self, year, karobka, y_sarfi, masofa) -> None:
        self.year=year
        self.karobka=karobka
        self.y_sarfi=y_sarfi
        self.masofa=masofa
class nexia3(autolar):
    def __init__(self, year, karobka, y_sarfi, masofa) -> None:
        super().__init__(year, karobka, y_sarfi, masofa)
    def get_ninfo(self): 
        n=f"Nexia 3 automiz {self.year}-yil chiqib {self.karobka} rusumli "
        n+=f"{self.y_sarfi}- litr yoqilg'i sarfi {self.masofa}-km masofa bosib o'tgan"
        return n
class kobalt(autolar):
    def __init__(self, year, karobka, y_sarfi, masofa) -> None:
        super().__init__(year, karobka, y_sarfi, masofa)
    def get_kinfo(self): 
        c=f"Colabt automiz {self.year}-yil chiqib {self.karobka} rusumli "
        c+=f"{self.y_sarfi}- litr yoqilg'i sarfi {self.masofa}-km masofa bosib o'tgan"
        return c
class lasetti(autolar):
    def __init__(self, year, karobka, y_sarfi, masofa) -> None:
        super().__init__(year, karobka, y_sarfi, masofa)
    def get_linfo(self): 
        l=f"Lasetti automiz {self.year}-yil chiqib {self.karobka} rusumli "
        l+=f"{self.y_sarfi}- litr yoqilg'i sarfi {self.masofa}-km masofa bosib o'tgan"
        return l
class lkaptiva(autolar):
    def __init__(self, year, karobka, y_sarfi, masofa) -> None:
        super().__init__(year, karobka, y_sarfi, masofa)
    def get_kinfo(self): 
        k=f"Kaptiva automiz {self.year}-yil chiqib {self.karobka} rusumli "
        k+=f"{self.y_sarfi}- litr yoqilg'i sarfi {self.masofa}-km masofa bosib o'tgan"
        return k
class malibu(autolar):
    def __init__(self, year, karobka, y_sarfi, masofa) -> None:
        super().__init__(year, karobka, y_sarfi, masofa)
    def get_minfo(self): 
        j=f"Malibu automiz {self.year}-yil chiqib {self.karobka} rusumli "
        j+=f"{self.y_sarfi}- litr yoqilg'i sarfi {self.masofa}-km masofa bosib o'tgan"
        return j
class kia(autolar):
    def __init__(self, year, karobka, y_sarfi, masofa) -> None:
        super().__init__(year, karobka, y_sarfi, masofa)
    def get_kinfo(self): 
        o=f"KIA automiz {self.year}-yil chiqib {self.karobka} rusumli "
        o+=f"{self.y_sarfi}- litr yoqilg'i sarfi {self.masofa}-km masofa bosib o'tgan"
        return o
salon1=auto_salon("Asaka", 1996, 58966, 546978452)
cars=auto("Nexi 3","Cobalt", "Lasetti", "Kaptiva","Malibu", "KIA")
car=firma("asaka", 1996, 6496531,698745632145, "Andijon", 1462, cars)
salonlar=kobalt(2024,"Mexanika","8 litr","456123")
print(salonlar.get_kinfo())
  
