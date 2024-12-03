import aiohttp
import asyncio
from aiohttp import web # server api- za definirat posluzitelja
# ako saljemo za kljentske strane na posluzitelja, server treba bit prvi pokrenut,

app = web.Application()

def handler_function(request): 
    print("helloW")
    #return web.Response(text="pozdrav rs sustavi ")
    data = {'ime' : 'ivo', 'prezime' : 'ivic'}
    return web.json_response(data)

async def post_handler(request): 
    data = await request.json() # deserijalizacija json podataka
    print(data) #ispis podataka u terminal
    return web.json_response(data)


app.router.add_get("/",handler_function)
app.router.add_post("/",post_handler)
web.run_app(app,host ="localhost", port= 8080 ) # pokretanje servera, + isntaliraj nodemon za lakse porketanje koda


# ovo je sad simulacija kljenta, znaci bez da koristis postman itd..,
#sljedece zelimo pokrenut kljent a i posluzitelja u isto vrijeme ? AppRunner klasa za vise kontrole nad serverom

async def main():
    async with aiohttp.ClientSession() as session:
     response = await session.get("http://localhost:8080")
     response_json = await response.json()
     print(response_json)


asyncio.run(main())

# primejr app runera tj. kao pkrenut server i zatim kljentsku sesiju, u main() korutini pokrecemo start_server() korutinu

from aiohttp import web
from aiohttp.web import AppRunner
import asyncio, aiohttp

app= web.Application()



def handle_change(request):
    print("hello")
    return web.json_response({"korisnici": ["ivo", "Ana", "Marko"]})


app.router.add_get("/", handle_change)



async def start_server():
    runner= AppRunner(app)  # 1. Definiraj AppRunner instancu
    await runner.setup()
    site= web.TCPSite(runner, "localhost", 8080)
    await site.start()
    print("Server up and running")




async def main():
    await start_server() # Prvo pokreni poslužitelj
    async with aiohttp.ClientSession() as session: # Zatim otvori klijentsku sesiju
        rezultat = await session.get('http://localhost:8080/') # Pošalji GET zahtjev na lokalni poslužitelj
        print(await rezultat.text()) # Ispis odgovora
    
    
asyncio.run(main())

#3.2 GET ruta s URL parametrima


from aiohttp import web
from aiohttp.web import AppRunner
import asyncio, aiohttp

app= web.Application()



def handle_change(request):
    print("hello")
    return web.json_response({"korisnici": ["ivo", "Ana", "Marko"]})

async def get_users(request):
    user_id = request.match_info.get("id")  # Koristimo get() metodu kako bismo izbjegli key error

    korisnici = [
    {"id": 1, "ime": "Ivo", "godine": 25},
    {"id": 2, "ime": "Ana", "godine": 22},
    {"id": 3, "ime": "Marko", "godine": 19},
    {"id": 4, "ime": "Maja", "godine": 21},
    {"id": 5, "ime": "Iva", "godine": 40}
    ]


    if user_id is None:
        return web.json_response(korisnici, status=200)
    for korisnik in korisnici:
         if korisnik['id'] == int(user_id):
             return web.json_response(korisnik, status=200)
    return web.json_response({'error': 'Korisnik s traženim ID-em ne postoji'}, status=404)


app.router.add_get("/", handle_change)
app.router.add_get("/users/{id}", get_users) # Sada očekujemo route parametar 'id'



async def start_server():
    runner= AppRunner(app)  # 1. Definiraj AppRunner instancu
    await runner.setup()
    site= web.TCPSite(runner, "localhost", 8080)
    await site.start()
    print("Server up and running")




async def main():
    await start_server() # Prvo pokreni poslužitelj
    async with aiohttp.ClientSession() as session: # Zatim otvori klijentsku sesiju
        rezultat = await session.get('http://localhost:8080/users/1') # Pošalji GET zahtjev na lokalni poslužitelj
        rezultat_text = await rezultat.text()
        print(rezultat_text) # Ispis odgovora

        rezultat_dict = await rezultat.json() #dekodiraj JSON odgovor u rječnik
        print(rezultat_dict) # {'error': 'Korisnik s traženim ID-em ne postoji'}
    
    
asyncio.run(main())

