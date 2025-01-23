from fastapi import FastAPI, HTTPException, Query, Path, status, Depends
from pydantic import BaseModel, Field


app= FastAPI()



class Admin(BaseModel):
    korisnicko_ime: str
    token: str

administratori = [
 {"korisnicko_ime": "secret_admin_007", "token": "super_secret_admin_token007"},
 {"korisnicko_ime": "secret_admin_123", "token": "admin_token123"},
 {"korisnicko_ime": "secret_admin_456", "token": "admin_token456"}
]

def provjeri_token(token: str):
    for x in administratori:
        if x["token"] == token:
            return Admin(**x)
    raise HTTPException(status_code=404, detail="nemoze")
    
@app.get("/tajni_podaci")
def get_tajni_podaci(admin: Admin = Depends(provjeri_token)): # koristimo Depends funkciju za "ubrizgavanje ovisnosti"
    return {"tajni_podaci": "šifra za sef je 1234"}

@app.get("/")
def tokeni(admin: Admin = Depends(provjeri))