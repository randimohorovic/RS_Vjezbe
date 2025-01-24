from fastapi import APIRouter, HTTPException, Query
router = APIRouter()
router = APIRouter(prefix="/filmovi")


data = [
    {
        "title": "Avatar",
        "year": 2009,
        "rated": "PG-13",
        "runtime": "162 min",
        "genre": "Action, Adventure, Fantasy",
        "language": "English, Spanish",
        "country": "USA, UK",
        "actors": [{"name": "Sam", "surname": "Worthington"}, {"name": "Zoe", "surname": "Saldana"}],
        "plot": "A paraplegic marine dispatched to the moon Pandora...",
        "writer": {"name": "James", "surname": "Cameron"},
        "images": ["https://example.com/image1.jpg"],
        "type": "movie",
        "imdb_rating": 7.9,
        "imdb_votes": 890617,
        "imdbID": "tt0499549"
    },
    {
        "title": "The Dark Knight",
        "year": 2008,
        "rated": "PG-13",
        "runtime": "152 min",
        "genre": "Action, Crime, Drama",
        "language": "English, Mandarin",
        "country": "USA, UK",
        "actors": [{"name": "Christian", "surname": "Bale"}, {"name": "Heath", "surname": "Ledger"}],
        "plot": "When the menace known as the Joker emerges from his mysterious past...",
        "writer": {"name": "Jonathan", "surname": "Nolan"},
        "images": ["https://example.com/image2.jpg"],
        "type": "movie",
        "imdb_rating": 9.0,
        "imdb_votes": 2000000,
        "imdbID": "tt0468569"
    }
]



@router.get("/")  #ustvari je /filmovi
def get_movies():
    return data

