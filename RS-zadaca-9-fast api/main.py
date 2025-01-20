from fastapi import FastAPI
from pydantic import BaseModel
from typing import TypedDict


app = FastAPI()
class SnagaMotora(BaseModel):
    kW: int
    KS: int
class Cijena(BaseModel):
    osnovna: float
    sa_pdv: float
class Automobil(BaseModel):
    id: int
    marka: str
    model: str
    boja: Literal["crvena", "plava", "zelena", "bijela", "crna"]
    godina_proizvodnje: Optional[int]
    snaga_motora: SnagaMotora
    cijena: Cijena

automobil = Automobil(
    id=1,
    marka="Audi",
    model="A4",
    boja="crvena",
    godina_proizvodnje=2018,
    snaga_motora=SnagaMotora(kW=100, KS=136),
    cijena=Cijena(osnovna=25000, sa_pdv=30000)
)
# ili sa from typing import TypedDict

# from typing import TypedDict
# class SnagaMotora(TypedDict):
# kW: int
# KS: int

# class Cijena(TypedDict):
# osnovna: float
# sa_pdv: float

# class Automobil(BaseModel):
# id: int
# marka: str
# model: str
# boja: Literal["crvena", "plava", "zelena", "bijela", "crna"]
# Ovaj automobil instancirali bi na sljedeći način:
# godina_proizvodnje: Optional[int]
# snaga_motora: SnagaMotora
# cijena: Cijena


# automobil = Automobil(
# id=1,
# marka="Audi",
# model="A4",
# boja="crvena",
# godina_proizvodnje=2018,
# snaga_motora={"kW": 100, "KS": 136},
# cijena={"osnovna": 25000, "sa_pdv": 30000}
# )

#tijelo azhtjeva
@app.get("/proizvodi/{id}")
def get_proizvodi(id : int, min_cijena: float, novi_proizvod: dict):
    return {"proizvod": id}

@app.get("/")
def get_proizvod(broj: int):
    return{"proizvod": broj}

