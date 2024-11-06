class Shaxs:
    def __init__(self,name, lastname, age, course, ability):
        #Shaxsning hususiyatlari
        self.name=name
        self.lastname=lastname
        self.age=age
        self.course=course
        self.ability=ability
    def get_info(self):
        #Shaxs haqida ma'lumot
        info=f"{self.name} {self.lastname}. {self.age}yoshda va {self.course} kurs talabasi. {self.ability}  tillarini biladi"
        return info
    def name_info(self):
        #Shaxsning faqat ismiga murojat
        return self.name
    def year(self,years):
        return years-self.age 
    def cours(self):
        return self.course
class Talaba(Shaxs):
    def __init__(self, name, lastname, age, course, ability,nomer,address):
        super().__init__(name, lastname, age, course, ability)
        self.nomer=nomer
        self.address=address
    def get_nomer(self):
        return self.nomer
    def get_info(self):
        return f"{self.name} {self.lastname}. {self.age}yoshda va {self.course} kurs talabasi. {self.ability}  tillarini biladi telefon nomeri {self.nomer}"
class Address():
    def __init__(self,home, street, district, region):
        self.home=home
        self.district=district
        self.street=street
        self.region=region
        self.district=district
        self.region=region
    def get_home(self):
        return self.home
    def get_street(self):
        return self.street
    def get_address(self):
        address=f"{self.region} viloyatining {self.district} tumanining {self.street} ko'chasi {self.home}-uyida yashaydi!"
        return address
talaba_address=Address(67,"Ibrat", "Bekobod", "Toshkent")
talaba=Talaba('Shohjahon',"G'aybullayev", 20, 3, "C++, Python, MySQL, C#","+99894-654-19-22",talaba_address)
print(talaba.get_info())
print(talaba.address.get_address())


