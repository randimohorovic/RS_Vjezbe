from fastapi import FastAPI
from models import Proizvod
from models import CreateProizvod
# @app.get(path) - definira GET rutu
# @app.post(path) - definira POST rutu
# @app.put(path) - definira PUT rutu
# @app.delete(path) - definira DELETE rutu
# @app.patch(path) - definira PATCH rutu
# @app.options(path) - definira OPTIONS rutu
# @app.head(path) - definira HEAD rutu

# Generirana FastAPI Swagger dokumentacija, dostupna na http://localhost:8000/docs
# Vidimo da generirana dokumentacija nudi pregled svih podataka koje očekuje i vraća naša ruta,
# odnosno sve podatke o HTTP zahtjevu koji se očekuje te o odgovoru koji će se vratiti.

app = FastAPI()

proizvodi = [
 {"id": 1, "naziv": "majica", "boja": "plava", "cijena": 50},
 {"id": 2, "naziv": "hlače", "boja": "crna", "cijena": 100},
 {"id": 3, "naziv": "tenisice", "boja": "bijela", "cijena": 150},
 {"id": 4, "naziv": "kapa", "boja": "smeđa", "cijena": 20}
]

@app.get("/") # dekorator za GET metodu na korijenskoj ruti("/"), dekoratori su funckije  ili klase koje prosiruju funkcionalnost druge funkcije ili klase
def read_root(): # funkcija koja se poziva kada se posjeti korijenska ruta, funkciju koja se mora izvršiti pišemo neposredno ispod dekoratora
    return {"message": "Hello, world!"} # vraća JSON odgovor u tijelu HTTP odgovora

#@app.get("/proizvodi/{proizvod_id}")
def get_proizvod(proizvod_id: int): # nismo definirali tip parametra pa ga on vraca kao string inace dodaj :int
    return {"proizvod_id": proizvod_id}

# pretrazivanje proizvoda po nazivu
@app.get("/proizvodi/{naziv}") # route parametar "naziv"
def get_proizvod_by_name(naziv: str): # očekujemo string kao naziv proizvoda
    # pronalazimo proizvod gdje se njegov naziv poklapa s nazivom iz parametra rute "naziv"
    pronadeni_proizvod = next((x for x in proizvodi if x["naziv"] == naziv ), None)
    return pronadeni_proizvod # pronalazimo proizvod gdje se njegov naziv poklapa s nazivom iz parametra rute "naziv"

#dodavanje proizvoda
# @app.post("/proizvodi")
# #def add_proizvod(proizvod: dict): #cak nije potrebno navest da je dict jer ako upotrjebio {} prepoznaje fastapi da se radi o objektu
# def add_proizvod(proizvod: CreateProizvod): 
#     new_id = len(proizvodi) +1 #{ "naziv": "šal", "boja": "plava", "cijena": 30 } id nismo poslali pa je dodao u objekt
#     proizvodi.append(proizvod)
#     return proizvod

@app.post("/proizvodi", response_model=Proizvod) # naglašavamo da je povratna vrijednost tipa Proizvod
def add_proizvod(proizvod: CreateProizvod):
    new_id = len(proizvodi) + 1
    proizvod_s_id = Proizvod(id=new_id, **proizvod.model_dump())
    return proizvod_s_id

#lista proizvoda
@app.get("/proizvodi")
def get_proizvodi():
    return proizvodi


#rad sa query parametrima
@app.get("/products")   #ne navodi querry parametre u URL putanji
def get_proizvodi_by_querry(boja: str = None, max_cijena: int= 100): #oekuej querry parametar boja, slicno ko sa parametriam u url-u, sa default vrijednostima
     #list comprehension , ne koristimo next(()) jer moze biti vise proizvoda sa istom bojom, next cim nade prvog u listi prekine search
     pronadeni_proizvod =[x for x in proizvodi if (x["boja"]== boja or boja is None) and (x["cijena"]<= max_cijena or max_cijena is None)]
     return pronadeni_proizvod



#uvicorn main:app --reload ili
# fastapi dev main.py



