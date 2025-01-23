from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel,Field


app = FastAPI()

class KnjigaRequest(BaseModel):
    naslov: str
    autor: str
    broj_stranica: int = Field(description="broj stranica", ge=1)
    godina_izdavanja: int = Field(ge=0, le=2024)

class KnjigaResponse(KnjigaRequest):
    id: int

knjige = [
 {"id": 1, "naslov": "Ana Karenjina", "autor": "Lav Nikolajevič Tolstoj",
"broj_stranica": 864, "godina_izdavanja": 1877},
 {"id": 2, "naslov": "Kiklop", "autor": "Ranko Marinković", "broj_stranica": 488,
"godina_izdavanja": 1965},
 {"id": 3, "naslov": "Proces", "autor": "Franz Kafka", "broj_stranica": 208,
"godina_izdavanja": 1925}
]

@app.get("/knjige/{naslov}", response_model=Knjiga)
def dohvati_knjigu(naslov: str):
    for knjiga in knjige:
        if knjiga["naslov"] == naslov:
            return knjiga # vraćamo knjigu ako je pronađena
    raise HTTPException(status_code=404, detail="Knjiga nije pronađena") # podižemo iznimku
    #ako knjiga nije pronađena s odgovarajućom porukom i statusnim kodom

    #ili

@app.get("/knjige/{naslov}", response_model=Knjiga)
def dohvati_knjigu2(naslov: str):
    for knjiga in knjige:
        if knjiga["naslov"] == naslov:
            return knjiga # vraćamo knjigu ako je pronađena
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Knjiga s id-em {id} 
                        nije pronađena") 
#ako knjiga nije pronađena s odgovarajućom porukom i statusnim kodom


from fastapi import Path
#kad zelis validirat da id koj korisnik unese mora bit ge=1, ili ge,gt,le,lt
@app.get("/knjige/{id}", response_model=KnjigaResponse)
def dohvati_knjigu(id: int = Path(title="ID knjige", ge=1)): # koristimo isti "ge"
    #parametar kao u Field polju
        for knjiga in knjige:
            if knjiga["id"] == id:
                return knjiga # vraćamo knjigu ako je pronađena
        raise HTTPException(status_code=404, detail=f"Knjiga s id-em {id} nije pronađena") #
# podižemo iznimku ako knjiga nije pronađena s odgovarajućom porukom i statusnim kodom