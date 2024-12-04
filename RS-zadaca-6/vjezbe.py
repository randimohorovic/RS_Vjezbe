import aiohttp
import asyncio
from aiohttp import web 


app = web.Application()

korisnici = [
    {'ime': 'Ivo', 'godine': 25},
    {'ime': 'Ana', 'godine': 17},
    {'ime': 'Marko', 'godine': 19},
    {'ime': 'Maja', 'godine': 16},
    {'ime': 'Iva', 'godine': 22}
]

async def handler_function(request): 
    
    punoljetni = [korisnik for korisnik in korisnici if korisnik["godine"] > 17]
    return web.json_response(punoljetni)



app.router.add_get("/punoljetni", handler_function)
web.run_app(app,host ="localhost", port= 8082 ) # pokretanje servea

#