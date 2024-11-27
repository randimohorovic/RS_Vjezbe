import aiohttp
import asyncio
from aiohttp import web # server api- za definirat posluzitelja

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
#sljedece zelimo pokrenut kljent ai posluzitelja u isto vrijeme ?
async def main():
    async with aiohttp.ClientSession() as session:
     response = await session.get("http://localhost:8080")
     response_json = await response.json()
     print(response_json)


asyncio.run(main())



