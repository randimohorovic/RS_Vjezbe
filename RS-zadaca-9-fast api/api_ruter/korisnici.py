from fastapi import APIRouter

router = APIRouter()
router = APIRouter(prefix="/korisnici")


@router.get("/") #ustvari je /korisnici, di god imas /korisnic/nesto, taj/korisnici je vec dodatno kao preifx router
def get_all():
    return {"korisnici": "hello"}

