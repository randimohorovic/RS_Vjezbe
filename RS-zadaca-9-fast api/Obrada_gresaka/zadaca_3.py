from fastapi import FastAPI, HTTPException, status,Path, Query
from pydantic import BaseModel,Field
from typing import TypedDict


app = FastAPI()

class Basecar(BaseModel):
    marka: str = Field(description="opis field polja")
    model: str
    godina_proizvodnje: int
    cijena: float
    boja: str

class AutomobilCreate(Basecar):
    pass

class AutomobilResponse(Basecar):
    sa_pdv: float
    id: int
   


auti = []

@app.get("/auti/{id}", response_model= Automobil)
def get_auti(id: int,  min_cijena: int = Query(1, ge=1) , max_cijena: int= Query(1000, ge=1)  , min_godina: int = Query(2025, ge= 1960, le=2025) , 
             max_godina: int = Query(2025, ge= 1960, le=2025)):
    if min_cijena >= max_cijena or min_godina >= max_godina:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="min cijena je veca od max/ min godina veca od max")
    for x in auti:
        if x["cijena"] >= min_cijena and x["cijena"] <= max_cijena and x["godina_proizvodnje"] >= min_godina and x["godina_proizvodnje"] <= max_godina:
            return x
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "auto nije naden")


@app.post("/auti/dodaj")
def post_auti(id: int):
    pass