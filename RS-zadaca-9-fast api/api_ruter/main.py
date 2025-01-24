from fastapi import FastAPI
from api_router.korisnici import router as korisnici_router # uključujemo router iz datoteke korisnici.py

from api_router.knjige import router as knjige_router # uključujemo router iz datoteke knjige.py

app = FastAPI()
app.include_router(korisnici_router) # uključujemo rute za korisnike
app.include_router(knjige_router) # uključujemo rute za knjige
# nastavljamo dalje s definicijom rute na "main" razini



#mapa sa routerima mora biti zasebno, main.py je izvan isto kao i models

@app.get("/")
def home():
    return {"poruka": "Dobrodošli na FastAPI poslužitelj"}
