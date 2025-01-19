from typing import Optional, Literal

class Automobil(BaseModel):
    id: int
    marka: str
    model: str
    boja: Literal["crvena", "plava", "zelena", "bijela", "crna"]
    godina_proizvodnje: Optional[int]
    snaga_motora: dict[str, int] 
    cijena: dict[str, float]


# class snagmotora(basemodel):
#     kw:int
#     ks:int

# class Automobil2(BaseModel):
#     id: int
#     marka: str
#     model: str
#     boja: Literal["crvena", "plava", "zelena", "bijela", "crna"]
#     godina_proizvodnje: Optional[int]
#     snaga_motora: snagamotora
#     cijena: dict[str, float]

automobil = Automobil(
id=1,
marka="Audi",
model="A4",
boja="crvena",
godina_proizvodnje=2018,
snaga_motora={"kW": 100, "KS": 136},
cijena={"osnovna": 25000, "sa_pdv": 30000}
)