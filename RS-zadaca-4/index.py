import aiohttp
import asyncio
import requests
import time



#zelimo u main() koristiti asyncio.gather() i pozivat vanjske korutine


async def get_cat_fact(session):# prosljedujemo session u korutinu
     print("saljem zahtjev")
     response = await session.get("https://catfact.ninja/fact")
     response_json = await response.json()
     print(response_json["fact"]) #["fact"]
     return response_json


async def main():
    start_time = time.time()
    #konekciju otvaram 1. 
    async with aiohttp.ClientSession() as session:

        liste_korutina =[get_cat_fact(session) for i in range(5)]

        rezultati = await asyncio.gather(*liste_korutina)
        print(type(rezultati))
        end_time = time.time()
    print(f"vrijem itzvodenja {end_time - start_time:.2f}")


# #rezultat mozemo vidjeti brze izvodenje
# saljem zahtjev
# saljem zahtjev
# saljem zahtjev
# saljem zahtjev
# A cat cannot see directly under its nose.
# A cat can jump 5 times as high as it is tall.
# The average cat food meal is the equivalent to about five mice.
# Cats and kittens should be acquired in pairs whenever possible as cat families interact best in pairs.
# The first formal cat show was held in England in 1871; in America, in 1895.
# <class 'list'>
#vrijem itzvodenja 0.25 --> brze izvodenje

asyncio.run(main())





