# 2.4 Zadaci za vježbu: Definiranje jednostavnih aiohttp
# poslužitelja

# Zadatak 2: POST /proizvodi
# Nadogradite poslužitelj iz prethodnog zadatka na način da na istoj putanji /proizvodi prima POST zahtjeve
# s podacima o proizvodu. Podaci se šalju u JSON formatu i sadrže ključeve naziv , cijena i količina .
# Handler funkcija treba ispisati primljene podatke u terminalu, dodati novi proizvod u listu proizvoda i vratiti
# odgovor s novom listom proizvoda u JSON formatu.
import aiohttp
from aiohttp import web 

app = web.Application()

def handler_function(request): 
    print("helloW")
    data = {'naziv' : 'p1', 'cjena' : 10, 'kolicina': 6}
    return web.json_response(data)

app.router.add_get("/proizvodi",handler_function)
web.run_app(app,host ="localhost", port= 8081 ) # pokretanje servea

