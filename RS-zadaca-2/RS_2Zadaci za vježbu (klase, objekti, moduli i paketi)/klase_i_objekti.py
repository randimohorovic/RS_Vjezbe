# 6. Zadaci za vježbu - Klase, objekti, moduli i
# paketi
# Zadatak 4: Klase i objekti

# 1. Definirajte klasu Automobil s atributima marka , model , godina_proizvodnje i kilometraža .
# Dodajte metodu ispis koja će ispisivati sve atribute automobila.
# Stvorite objekt klase Automobil s proizvoljnim vrijednostima atributa i pozovite metodu ispis .
# Dodajte novu metodu starost koja će ispisivati koliko je automobil star u godinama, trenutnu
# godine dohvatite pomoću datetime modula.

from datetime import datetime

class automobili:
    def __init__(self, marka, model, godina_proizvodnje, kilometraza):
        self.marka = marka
        self.godina_proizvodnje = godina_proizvodnje
        self.model = model
        self.kilometraza = kilometraza

    def ispis(self):
        return f"ispis svih atributa , marka: {self.marka} model: {self.model} godina proizvodnje: {self.godina_proizvodnje} km: {self.kilometraza} "        

    def starost(self):
        trenutna_godina = datetime.now().year  
        starost = trenutna_godina - self.godina_proizvodnje
        return f"Automobil {self.marka} {self.model} star je {starost} godina."


auto1= automobili("BMW", "m4 coupe", "2018", 60000)

print(auto1.ispis())
print(auto1.starost())


# 2. Definirajte klasu Kalkulator s atributima a i b . Dodajte metode zbroj , oduzimanje , mnozenje ,
# dijeljenje , potenciranje i korijen koje će izvršavati odgovarajuće operacije nad atributima a i
# b .


import math

class kalkulator:
    def __init__(self,a,b):
        self.a = a 
        self.b =b
    
    def zbrajanje(self):
        return f"zbroj rezultat {self.a+self.b}"
    
        
    def oduzimanje(self):
        return f"oduzimanje rezultat:  {self.a-self.b}"

    
    def mnozenje(self):
        return f"umnozak rezultat:  {self.a*self.b}"

    
    def dijeljenje(self):
        if self.b == 0:
            return "nije moguce djelit s nulom"
        return f"dijeljenje rezultat:  {self.a/self.b}"
    
        
    def potenciranje(self):
        return f"potenciranje rezultat {self.a**self.b}"

    
    def korijen(self):
        return f"rezultat je {math.sqrt(self.a)}, {math.sqrt(self.b)}"



broj1 =kalkulator(5,5)


print(broj1.zbrajanje())
print(broj1.oduzimanje())
print(broj1.mnozenje())
print(broj1.dijeljenje())
print(broj1.potenciranje())
print(broj1.korijen())
    

# 3. Definirajte klasu Student s atributima ime , prezime , godine i ocjene .
# Iterirajte kroz sljedeću listu studenata i za svakog studenta stvorite objekt klase Student i dodajte ga u
# novu listu studenti_objekti :

studenti = [
{"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
{"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
{"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
{"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
{"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
{"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]}
]


# 4. Definirajte klasu Krug s atributom r . Dodajte metode opseg i povrsina koje će računati opseg i
# površinu kruga.
# Stvorite objekt klase Krug s proizvoljnim radijusom i ispišite opseg i površinu kruga.

import math

class Krug:
    def __init__(self, r):
        self.r = r  
    
    def opseg(self):
        return 2 * math.pi * self.r 
    
    def povrsina(self):
        return math.pi * self.r ** 2  


radijus = 5  
krug = Krug(radijus)


print(f"Opseg kruga s radijusom {radijus} je: {krug.opseg():.2f}")
print(f"Površina kruga s radijusom {radijus} je: {krug.povrsina():.2f}")



# 5. Definirajte klasu Radnik s atributima ime , pozicija , placa . Dodajte metodu work koja će ispisivati
# "Radim na poziciji {pozicija}".
# Dodajte klasu Manager koja nasljeđuje klasu Radnik i definirajte joj atribut department . Dodajte
# metodu work koja će ispisivati "Radim na poziciji {pozicija} u odjelu {department}".
# U klasu Manager dodajte metodu give_raise koja prima parametre radnik i povecanje i
# povećava plaću radnika ( Radnik ) za iznos povecanje .
# Definirajte jednu instancu klase Radnik i jednu instancu klase Manager i pozovite metode work i
# give_raise .