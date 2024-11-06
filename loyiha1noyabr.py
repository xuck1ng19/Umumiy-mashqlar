##G'aybullayev Shohjahon 1.11.2024

from typing import Any
from uuid import uuid4
class Auto:
    __num_auto=0
    "Automillar haqida ma'lumot beruvchi"
    def __init__(self, narx, yili,karobkasi,nomi,rangi,km=0) -> None:
        self.nomi=nomi
        self.rangi=rangi
        self.yili=yili
        self.karobkasi=karobkasi
        self.narx=narx
        self.__km=km
        self.__id=uuid4
        Auto.__num_auto+=1
    @classmethod
    def get_method(cls):
        return cls.__num_auto
    def get_id(self):
        return self.__id
    def get_km(self):
        return self.__km
    def get_narx(self):
        return self.narx
    def get_yili(self):
        return self.yili               
 
    def add_km(self,km):
        "Moshinaning km ni oshirish"
        if km>=0:
            self.__km+=km
        else:
            print("Moshinaning km ni pasaytirib bo'lmaydi")
    def __repr__(self) -> str:
        return f"Avto: {self.nomi}, {self.yili}"
    
    def __eq__(self,y) -> bool:
        return self.narx==y.narx
    
    def __lt__(self,y):
        return self.narx>y.narx
    def __le__(self,y):
        return self.narx>=y.narx
    
    
class Salon():
    def __init__(self, nomi,) -> None:
        self.nomi=nomi
        self.avtolar=[]
    def __repr__(self) -> str:
        return f" {self.nomi} avtosaloni"
    
    def __getitem__(self,index):
        return self.avtolar[index]
    
    def __setitem__(self,index,qiymat):
        self.avtolar[index]=qiymat
        return qiymat
    
    def add_auto(self, *qiymat):
        for auto in qiymat:
            if isinstance(auto,Auto):
                self.avtolar.append(auto)
            else:
                print("Auto kiriting")
    def __call__(self,*qiymat) -> Any:
        if qiymat:
            for auto in qiymat:
                self.add_auto(auto)
        else:
            return [auto for auto in self.avtolar]
        
    def __add__(self, y):
        if isinstance(y, Salon):
            yangi_salon=Salon(f"{self.nomi} {y.nomi}")
            yangi_salon.avtolar=self.avtolar+y.avtolar
            return yangi_salon
        elif isinstance(y,Auto):
            self.add_auto(y)

    

salon1=Salon("Maxsalon")
salon2=Salon("Lider")

auto1=Auto(40000,2023,"mexanika",'KIA 5',"oq",50000)
auto2=Auto(13000,2020,"mexanika",'Cobalt',"oq",5000)
auto3=Auto(20000,2021,"mexanika",'Malibu',"qora",1000)
salon1(auto1,auto2,auto3)
salon2(auto2,auto3,auto1)
auto4=Auto(40000,2023,"mexanika",'Spark',"oq",50000)
auto5=Auto(40000,2023,"mexanika",'Mattiz',"oq",50000)
auto6=Auto(40000,2023,"mexanika",'Chip',"oq",50000)
#salon1=Auto(2000,2020,"mexanika", "Tico","yashil",1)
#salon2[0]="Tayotta"
salon2+auto4
print(salon2())