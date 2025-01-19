from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


#route parametar
#min_cijena querry
#tijelo azhtjeva
@app.get("/proizvodi/{id}")
def get_proizvodi(id : int, min_cijena: float, novi_proizvod: dict):
    return {"proizvod": id}