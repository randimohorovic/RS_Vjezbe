def ukloni_duplikate(lista):
 
    bez_duplikata = list(set(lista))
    return bez_duplikata


lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(ukloni_duplikate(lista))  

#set sadrzi samo ali samo unique elemente, usefull to know.