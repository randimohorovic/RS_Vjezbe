from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Automobil(BaseModel):
    id: int
    marka: str
    model: str
    godina_proizvodnje: int
    cijena: float
    boja: str


auti = [
    Automobil(id=1, marka="Golf", model="4", godina_proizvodnje=2015, cijena=12000.0, boja="plava"),
    Automobil(id=2, marka="Golf", model="4", godina_proizvodnje=2018, cijena=12000.0, boja="plava"),
    Automobil(id=3, marka="Golf", model="4", godina_proizvodnje=2020, cijena=12000.0, boja="Plava")
]

@app.get("/auti/{id}", response_model=Automobil)
def get_car(id: int):
    # Search for the car by ID in the "database"
    for x in auti:
        if x.id == id:
            return x
    raise HTTPException(status_code=404, detail="Automobil nije pronađen")

@app.get("/auti", response_model=List[Automobil])
def get_all_cars():
    return auti