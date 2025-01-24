from pydantic import BaseModel
from typing import TypedDict, Literal, Optional

class BaseMovieCreate(BaseModel):
    title: str
    year: str=Field(description="godina filma", ge=1900)
    rated: str
    released: str
    runtime: str
    genre: str
    director: str
    writer: str
    actors: str
    plot: str
    language: str
    country: str
    awards: str
    poster: str
    metascore: str
    imdb_rating: str 
    imdb_votes: str 
    imdb_id: str 
    type: Literal["movie","series"]
    response: str
    images: list[str]


class Actor(BaseModel):
    name:str
    surname: str

class Writer(BaseModel):
    name:str
    surname: str