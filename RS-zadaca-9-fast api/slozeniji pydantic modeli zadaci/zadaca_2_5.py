from fastapi import FastAPI
from pydantic import BaseModel
from typing import TypedDict, Optional, Literal, Tuple
from datetime import datetime

app = FastAPI()

@app.get("/")
def get_all():
    pass


#1. zadatak
class Knjiga(BaseModel):
    naslov: str
    ime_autora: str
    prezime_autora: str
    godina_izdavanja: Optional[int] = datetime.now()
    broj_stranica: int
    broj_izdavaca: int

class Izdavac(BaseModel):
    naziv: str
    adresa: str



#2. zadatak
class Admin():
    ime: str
    prezime: str
    korisnicko_ime: str
    email: str
    ovlasti: Literal["dodavanje", "brisanje", "ažuriranje", "čitanje"]

#3.zadatak


class Stol_info(TypedDict):
    broj: int
    lokacija: str

class Jelo(BaseModel):
    id: str
    naziv: str
    cijena: str


class RestaurantOrder(BaseModel):
    id: str
    ime_kupca: str
    stol_info: Stol_info
    lista_jela: list[Jelo]
    cjena: float

#4.zadatak
class CCTV_frame(BaseModel):
    id: int
    vrijeme_snimanja: datetime
    koordinate: Tuple[float, float] = (0.0,0.0)

