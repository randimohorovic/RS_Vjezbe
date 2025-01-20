from fastapi import FastAPI
from pydantic import BaseModel
from typing import TypedDict
from datetime import datetime

app = FastAPI()

@app.get("/")
def get_all():
    pass

#nasljedivanje pydantic modela

class A(BaseModel):
    at_a: str
    at_b: str

class B(A):
    at_c: str

klasaA= A(at_a="string1", at_b = "string2")
klasaB= B(at_a="12", at_b="string6" ,at_c="string3")

print(klasaA,"-- ")
print(klasaB)

# objektb tj. klasaB sadrzi nasljedeno klasu A, 
# tako da se moraju unjest tocni kljucevi i tip podataka vrijdnosti, objekt B sadrzi u sebi strukturu klase a dodatno
# proizvodid = Klasa(nesto= id, **klasa-model_dump())

# poizvodid: klasaA= {"nesto": id, **klasa.model_dump()}


class korisnikBase(BaseModel):
    ime: str
    prezime: str
    email: str

class KorisnikCreate(korisnikBase):
    lozinka_text: str

class KorisnikResponse(korisnikBase):
    lozinka_hash: str
    datum_registracije: datetime

korisnici= []

@app.post("/korisnici", response_model=KorisnikResponse) #validacija http odgovora prema modelu korisnikresposne
def registracija_korisnika(korisnik: KorisnikCreate):
        lozinka_hash = str(hash(korisnik.lozinka_text))
        datum_registracije = datetime.now()
        korisnik_spreman: KorisnikResponse = {**korisnik.model_dump(), "lozinka_hash": lozinka_hash, "datum_registracije": datum_registracije}
        korisnici.append(korisnik_spreman)
        return korisnik_spreman



@app.get("/korisnici/all")
def get_all():
     return korisnici
     