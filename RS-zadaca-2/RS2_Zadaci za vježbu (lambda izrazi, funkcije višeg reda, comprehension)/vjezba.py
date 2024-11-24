# #lambda funckije su anonimne funkcije koje se koriste ya jedno kratne male operacije,
# #anonimmne su jer im se ne dojdeljuju imena

# lambda argument : expression

# def kvadriraj(x):
#     return x **2

# print("rez",kvadriraj(5)) # rez 25

# # lambda zapis

# # lambda x: x**2

# print((lambda x: x**2)(5))


# kvadriraj= lambda x: x**2

# print(kvadriraj(5))

# tekst ="neki tekst"

# print((lambda x: x.upper())(tekst)) # mozemo koristi lambda f.

##lambdaf kao argumenti drugim f.



# def primjeni_na_sve(lista, funkcija):
#     rezultat =[]
#     for i in lista:
#         rezultat.append(funkcija(i))
#     return rezultat
# lam = lambda x: x**2
# print(primjeni_na_sve([1,2,5,4,8,6], lam))

##1.2.1 map()

# lista=[1,2,3,4,5,6]

# kvadriraj = lambda x: x**2

# kvadriraj_sve = list(map(kvadriraj, lista))

# print(kvadriraj_sve)

# studenti = [
#  {"ime": "Ivan", "prezime": "Ivić", "jmbag": "0303077889"},
#  {"ime": "Marko", "prezime": "Marković", "jmbag": "0303099878"},
#  {"ime": "Ana", "prezime": "Anić", "jmbag": "0303088777"}
# ]
# jmbagovi = list(map(lambda x: x["prezime"], studenti))

# print(jmbagovi)


## filter slicno sto i map prima funkciju iiterabilni objekt 
## ali f. vraca boolean vrijenost , true ili false

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# parni= list(filter(lambda x: x%2 ==0, lista))

# print(parni)

# studenti = [
#  {"ime": "Ivan", "prezime": "Ivić", "jmbag": "0303077889", "godina_rodenja" : 2000},
#  {"ime": "Marko", "prezime": "Marković", "jmbag": "0303099878", "godina_rodenja" :
# 1999},
#  {"ime": "Ana", "prezime": "Anić", "jmbag": "0303088777", "godina_rodenja" : 2003},
# ]

# rodeni_prije_2000 = list(filter(lambda x: x["godina_rodenja"] <2000, studenti))

# print(rodeni_prije_2000)

# lsita = []

# for i in range(1,11):
#     lsita.append(i**2)

# print(lsita)



# kvariraj = list(map(lambda x: x**2, range(1,11)))

# print(kvariraj)


## comprehension
#[expression for element in iterable]

# kvadrat = [x **2 for x in range(1,11)]

# print(kvadrat)

## [expression for element in iterable if condition] mozes nakon if condition dodat else condition

# niz = [1,2,3,4,5,6]
# duljie =[x**2 for x in niz if x%2 !=0]
# print(duljie)


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# list =[x[:3] for x in fruits]

# print(list)

##2.2 Dictionary comprehension

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]


# duljina = {x: len(x) for x in fruits}

# print(duljina)
## razlika dictionary i  comprehension liste 
# paran_neparan = {i: "paran" if i % 2 == 0 else "neparan" for i in range(1, 11)}