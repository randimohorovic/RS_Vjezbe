# Zadatak 1: GET /proizvodi
# Definirajte aiohttp poslužitelj koji radi na portu 8081 koji na putanji /proizvodi vraća listu proizvoda u
# JSON formatu. Svaki proizvod je rječnik koji sadrži ključeve naziv , cijena i količina . Pošaljite zahtjev na
# adresu http://localhost:8080/proizvodi koristeći neki od HTTP klijenata ili curl i provjerite odgovor.

import aiohttp
from aiohttp import web 

app = web.Application()


def handler_function(request): 
    print("helloW")
    data = {'naziv' : 'p1', 'cjena' : 10, 'kolicina': 6}
    return web.json_response(data)

app.router.add_get("/proizvodi",handler_function)
web.run_app(app,host ="localhost", port= 8081 ) # pokretanje servea
















  
#     async with aiohttp.ClientSession() as session:
#      response = await session.get("https://jsonplaceholder.typicode.com/users")
#      response_json = await response.json()
#      print(response_json)


# asyncio.run(main())



