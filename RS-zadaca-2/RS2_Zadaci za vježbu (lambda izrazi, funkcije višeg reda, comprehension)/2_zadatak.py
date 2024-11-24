## Funkcije viseg reda

##Definirajte sljedeće izraze korištenjem funkcija višeg reda i lambda izraza:


##1. Koristeći funkciju map , kvadrirajte duljine svih nizova u listi:

nizovi = ["jabuka", "kruška", "banana", "naranča"]
# kvadrirane_duljine = ...
# print(kvadrirane_duljine) # [36, 36, 36, 49]

# def kvadriraj(funkcija,lista):
#     rezultat =[]
#     for i in lista:
#         rezultat.append(funkcija(i))
#     return rezultat

lam = list(map(lambda x: len(x)**2, nizovi))

print(lam)