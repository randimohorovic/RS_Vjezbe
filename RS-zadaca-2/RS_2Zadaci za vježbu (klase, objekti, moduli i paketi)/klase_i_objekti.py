# 6. Zadaci za vježbu - Klase, objekti, moduli i
# paketi
# Zadatak 4: Klase i objekti
class automobili:
    def __init__(self, marka, model, godina_proizvodnje, kilometraza):
        self.marka = marka
        self.godina_proizvodnje = godina_proizvodnje
        self.model = model
        self.kilometraza = kilometraza

    def ispis(self):
        return f"ispis svih atributa , marka: {self.marka} model: {self.model} godina proizvodnje: {self.godina_proizvodnje} km: {self.kilometraza} "        


auto1= automobili("BMW", "m4 coupe", "2018", 60000)

print(auto1.ispis())

# 1. Definirajte klasu Automobil s atributima marka , model , godina_proizvodnje i kilometraža .
# Dodajte metodu ispis koja će ispisivati sve atribute automobila.
# Stvorite objekt klase Automobil s proizvoljnim vrijednostima atributa i pozovite metodu ispis .
# Dodajte novu metodu starost koja će ispisivati koliko je automobil star u godinama, trenutnu
# godine dohvatite pomoću datetime modula.



# 2. Definirajte klasu Kalkulator s atributima a i b . Dodajte metode zbroj , oduzimanje , mnozenje ,
# dijeljenje , potenciranje i korijen koje će izvršavati odgovarajuće operacije nad atributima a i
# b .


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



# 5. Definirajte klasu Radnik s atributima ime , pozicija , placa . Dodajte metodu work koja će ispisivati
# "Radim na poziciji {pozicija}".
# Dodajte klasu Manager koja nasljeđuje klasu Radnik i definirajte joj atribut department . Dodajte
# metodu work koja će ispisivati "Radim na poziciji {pozicija} u odjelu {department}".
# U klasu Manager dodajte metodu give_raise koja prima parametre radnik i povecanje i
# povećava plaću radnika ( Radnik ) za iznos povecanje .
# Definirajte jednu instancu klase Radnik i jednu instancu klase Manager i pozovite metode work i
# give_raise .