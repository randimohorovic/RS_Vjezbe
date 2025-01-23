from fastapi import APIRouter
router = APIRouter()
router = APIRouter(prefix="/knjige")

@router.get("/")  #ustvari je /knjige
def get_knjige():
    return {"poruka": "Dohvaćene knjige"}