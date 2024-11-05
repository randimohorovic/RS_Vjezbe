a= float(input("unesi vrijednost broja a= "))
b= float(input("unesi vrijednost broja b= "))
c= str(input("unesi operator + , -, *, / "))

dozvoljeni_operatori= ("+","-")


if operator not in dozvoljeni_operatori:
    print("Greska operatora")

if operator is "+":
    print(f"Rezultat operacije  {a } + { b} iznosi { a+b}") #

#print("Vrijednost: = ",a b)


