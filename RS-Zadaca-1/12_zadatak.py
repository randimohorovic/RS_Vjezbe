def obrni_rjecnik(rjecnik):
    
    obrnuti_rjecnik={}
    for key, value in rjecnik.items():
         obrnuti_rjecnik.update({value: key})
    return obrnuti_rjecnik

rjecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}
print(obrni_rjecnik(rjecnik))


# {'Ivan': 'ime', 'Ivić': 'prezime', 25: 'dob'} 
