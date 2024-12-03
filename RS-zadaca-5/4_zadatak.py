# Zadatak 4: Dohvaćanje proizvoda

# Definirajte aiohttp poslužitelj koji radi na portu 8081 . Poslužitelj mora imati dvije rute: /proizvodi i
# /proizvodi/{id} . Prva ruta vraća listu proizvoda u JSON formatu, a druga rutu vraća točno jedan proizvod
# prema ID-u. Ako proizvod s traženim ID-em ne postoji, vratite odgovor s statusom 404 i porukom
# {'error': 'Proizvod s traženim ID-em ne postoji'} .
# Proizvode pohranite u listu rječnika:


# proizvodi = [
#  {"id": 1, "naziv": "Laptop", "cijena": 5000},
#  {"id": 2, "naziv": "Miš", "cijena": 100},
#  {"id": 3, "naziv": "Tipkovnica", "cijena": 200},
#  {"id": 4, "naziv": "Monitor", "cijena": 1000},
#  {"id": 5, "naziv": "Slušalice", "cijena": 50}
# ]


from aiohttp import web
from aiohttp.web import AppRunner
import asyncio, aiohttp

app= web.Application()



def handle_change(request):
    proizvodi = [
 {"id": 1, "naziv": "Laptop", "cijena": 5000},
 {"id": 2, "naziv": "Miš", "cijena": 100},
 {"id": 3, "naziv": "Tipkovnica", "cijena": 200},
 {"id": 4, "naziv": "Monitor", "cijena": 1000},
 {"id": 5, "naziv": "Slušalice", "cijena": 50}
]
    return web.json_response(proizvodi, status=200)

async def get_product(request):
    product_id = request.match_info.get("id")  # Koristimo get() metodu kako bismo izbjegli key error

    proizvodi = [
 {"id": 1, "naziv": "Laptop", "cijena": 5000},
 {"id": 2, "naziv": "Miš", "cijena": 100},
 {"id": 3, "naziv": "Tipkovnica", "cijena": 200},
 {"id": 4, "naziv": "Monitor", "cijena": 1000},
 {"id": 5, "naziv": "Slušalice", "cijena": 50}
]


    if product_id is None:
        return web.json_response(proizvodi, status=200)
    for proizvod in proizvodi:
         if proizvod['id'] == int(product_id):
             return web.json_response(proizvod, status=200)
    return web.json_response({'error': 'Proizvod s traženim ID-em ne postoji'}, status=404)


app.router.add_get("/proizvodi", handle_change)
app.router.add_get("/proizvodi/{id}", get_product) 



async def start_server():
    runner= AppRunner(app)  # definira apprunner instancu
    await runner.setup()
    site= web.TCPSite(runner, "localhost", 8081)
    await site.start()
    print("Server up and running")




async def main():
    await start_server()  # pokreni poslužitelj
    async with aiohttp.ClientSession() as session: #  otvori klijentsku sesiju
        rezultat = await session.get('http://localhost:8081/proizvodi/6') # Pošalji GET zahtjev na lokalni poslužitelj
        

        rezultat_dict = await rezultat.json() #dekodiraj JSON odgovor u rječnik
        print(rezultat_dict) 
    
    
asyncio.run(main())

