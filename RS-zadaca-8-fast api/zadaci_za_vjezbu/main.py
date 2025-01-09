from fastapi import FastAPI
from models import Film
from models import CreateFilm

app= FastAPI()

filmovi = [
 {"id": 1, "naziv": "Titanic", "genre": "drama", "godina": 1997},
 {"id": 2, "naziv": "Inception", "genre": "akcija", "godina": 2010},
 {"id": 3, "naziv": "The Shawshank Redemption", "genre": "drama", "godina": 1994},
 {"id": 4, "naziv": "The Dark Knight", "genre": "akcija", "godina": 2008}
]
#ruta koja vraca filmove
@app.get("/filmovi", response_model= list[Film]) # akostavis = Film onda to vraca jedan objekt tipa Film pa ti treba logika po id-u ili po cemu bis vratio
def get_filmovi():
    return filmovi

@app.get("/filmovi/{id}", response_model=Film)
def get_film_by_id(id: int):
    for x in filmovi:
        if x["id"]== id:
            return x
        
@app.post("/filmovi", response_model = Film)
def create_film(film: CreateFilm):
    new_id = len(filmovi) + 1 
    new_film = Film( id=new_id, **film.model_dump())#naziv=film.naziv, genre= film.genre, godina= film.godina
    return new_film


@app.get("/filmovi")
def get_movie_by_querry(genre: str = None, min_godina: int = 2000):
    searched_movie = [ x for x in filmovi if (genre is None or x["genre"]== genre) and (min_godina is None or x["godina"]>= min_godina )]
    return searched_movie 

