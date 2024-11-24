##Lambda izrazi za dole navedene funkcije

##1. Kvadriranje broja:
# def kvadriraj(x):
#     return x ** 2
i=5
print((lambda x: x**2)(i))

##2. Zbroji pa kvadriraj:

# def zbroji_pa_kvadriraj(a, b):
# return (a + b) ** 2

a=5
b=5

print((lambda x,y: (x+y)**2 )(a,b))

##3. Kvadriraj duljinu niza:

# def kvadriraj_duljinu(niz):
# return len(niz) ** 2

print((lambda x: len(x)**2)([1,2,3,4]))

##4. Pomnoži vrijednost s 5 pa potenciraj na x:

# def pomnozi_i_potenciraj(x, y):
# return (y * 5) ** x

print((lambda x,y: (y*5) **x )(1,2))

##5. Vrati True ako je broj paran, inače vrati None:
# def paran_broj(x):
#     if x % 2 == 0:
# return True
#     else:
#         return None

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

paran_broj=  list(filter(lambda x : x%2 ==0, lista))

print(paran_broj)

##ili bez liste

je_paran = lambda x : x%2 ==0

unesi= int(input("unesi neki broj"))

rezultat = je_paran(unesi)

if rezultat:
    print("True")
else:
    print("False")
