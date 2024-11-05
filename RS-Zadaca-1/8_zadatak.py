def filtriraj_parne(lista):
    
    parni_brojevi = [x for x in lista if x % 2 == 0]
    return parni_brojevi

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filtriraj_parne(lista)) 


