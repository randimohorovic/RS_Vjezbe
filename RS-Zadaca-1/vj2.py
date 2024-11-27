#lamba funkcije

# rez2 = lambda x: x ** 2

# print(rez2)

# lista = [1,2,3,4,5,6,7,8,9,10]

#izvuci samo parne brojeve iz gornje liste

# def parni(lista)
#     nova_lista=[]
#     for x in lista:
#         if x %2 ==0:
#             nova_lista.append(x)
#     return nova_lista

# lista_2 = filter(lambda x: x %2 ==0, lista)

# print(lista_2(lista))


### rezultat lista rjecnika
# studenti = [{"ime": "ivan", "godina_starenja": 1999}]
# #1. kalsican nacin

# #def filtriraj_starije(studenti):


# #lambda nacin

# studenti_rodeni_prije_2000 = list(filter(lambda student: student["godina_starenja"]< 2000, studenti))

# print(studenti_rodeni_prije_2000)



#all i any, lambda, map pa all, prema vani gradis
# lista = [2,4,6,9]



# svi_parni= all(map(lambda broj: broj %2 ==0, lista))

# print(svi_parni)


###comprehension sintaksa

# kvadrati = list(map(lambda x:x**2, range(1,11)))

##comprehension -  puno krace , i**2 mjenjamo sta se dogada za svaki elemnt prije for petlje
# kvadrati= [i**2 for i in range(1,11)]

# print(kvadrati)

##vj1
# nizovi= ["jabuka", "kruska"]

# novi_niz=[ len(i)for i in nizovi] #ako tsavis uglate biti ce skup inace lista zbog []

# print(novi_niz)

##vj2

# brojevi = [1,2,34,76,52,872,3,32,23176,54,66,9]

##comprehension za svaki broj ako je paran napravi listu ili kvadriraj ga sta god sa pcoetnim npr i**2

# parni = [i**2 for i in brojevi if i %2 ==0]

# print(parni)


##if else na pcoetku se pisu ,  Samo if uvjet na kraju
# parni = [i**2 if i %2==0 else i**3 for i in brojevi]

# print(parni)

##dictionry comprehension ako je if else ide ljevo, if ide desno, to smo rekli, proc zadatke za vjezbu itd

## zadaci lambda izrazi

# a= (lambda x,y: (y*5)**x)

# print(a(2,3))

##Koristeći funkcije all i map, provjerite jesu li svi studenti punoljetni:

# studenti = [
#     {"ime": "Ivan", "prezime": "Ivić", "godine": 19},
#     {"ime": "Marko", "prezime": "Marković", "godine": 22},
#     {"ime": "Ana", "prezime": "Anić", "godine": 21},
#     {"ime": "Petra", "prezime": "Petrić", "godine": 13},
#     {"ime": "Iva", "prezime": "Ivić", "godine": 17},
#     {"ime": "Mate", "prezime": "Matić", "godine": 18}
# ]

# svi_punoljetni = all(map(lambda student: student["godine"]>18, studenti))


# print(svi_punoljetni) # False


