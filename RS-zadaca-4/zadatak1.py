# 1. Definirajte korutinu fetch_users koja će slati GET zahtjev na JSONPlaceholder API na URL-u:
# https://jsonplaceholder.typicode.com/users . Morate simulirate slanje 5 zahtjeva konkurentno
# unutar main korutine. Unutar main korutine izmjerite vrijeme izvođenja programa, a rezultate
# pohranite u listu odjedanput koristeći asyncio.gather funkciju. Nakon toga koristeći map funkcije ili
# list comprehension izdvojite u zasebne 3 liste: samo imena korisnika, samo email adrese korisnika i
# samo username korisnika. Na kraju main korutine ispišite sve 3 liste i vrijeme izvođenja programa.


import aiohttp
import asyncio
import time


async def fetch_users(session):# prosljedujemo session u korutinu
     print("saljem zahtjev")
     response = await session.get("https://jsonplaceholder.typicode.com/users")
     response_json = await response.json()
     #print(response_json) #["fact"]
     return response_json


async def main():
    start_time = time.time()
    #konekciju otvaram 1. 
    async with aiohttp.ClientSession() as session:

        taskovi =[ fetch_users(session) for i in range(5)]

        rezultati = await asyncio.gather(*taskovi)
        sum= rezultati[0]
        
        #print(type(rezultati))
        imena_korisnika = list(map(lambda x: x["name"],sum))
        email_korisnika = list(map(lambda x: x["email"],sum))
        username_korisnika = list(map(lambda x: x["username"],sum))
        print(imena_korisnika)
        print(email_korisnika)
        print(username_korisnika)
        end_time = time.time()
    print(f"vrijem itzvodenja {end_time - start_time:.2f}")


asyncio.run(main())


