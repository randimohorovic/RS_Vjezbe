# ##Asinkroni Python: Slanje konkurentnih HTTP zahtjeva

import aiohttp
import asyncio
import requests
import time


#deserijalizacija , serijalizacija obrnuti proces, iz dict u json string
print(type(response1))
# {'fact': 'A cats field of vision is about 185 degrees.', 'length': 44}



def send_request():
    response = requests.get("https://catfact.ninja/fact")
    fact = response.json()["fact"]
    print(fact)


#primjer2:
# slozenost je o(n), vise zahtjeva vise vremena za izvodenje
#kako to rjesit na konkurentni nacin? u nastavku prikaz
start_time = time.time()
for i in range(1,16):
  print(f"saljem {i}. zahtjev")
  send_request()

end_time = time.time()

print(f"ukupno vrijem izvodenja { end_time - start_time:.2f} sec" )




##primjer3:

import aiohttp
import asyncio
import requests
import time

##konkurentni nacin priaza prijasnjeg zadatka kao primjer
## koristimo aiohttp 
#prijasni primejr koristio requests ali ona ponavlja sesiju u svakom zahtjevu, mi zelimo zdrzati
# sesiju otvorenu pomocu aiohttp


# Koncept kontekstnog menadžera (eng. Context Manager) u Pythonu omogućavaju nam alokaciju i
# dealokaciju resursa, odnosno upravljanje resursima koji se koriste u bloku koda.
# Najčešće korišteni primjer context managera u Pythonu je naredba with koju koristimo kako bismo
# definirali blok koda za rad s resursima koje treba eksplicitno (1) otvoriti, (2) koristiti i (3) zatvoriti.
# Primjerice:
# datoteke (otvaranje →čitanje/pisanje → zatvaranje)
# mrežne veze (otvaranje → slanje zahtjeva → zatvaranje)
# baze podataka (otvaranje → izvršavanje upita → zatvaranje)
# Naredba with omogućava automatsko upravljanje resursima, osiguravajući da će se resursi pravilno
# # osloboditi i zatvoriti čak i ako dođe do greške u bloku koda. Na taj način, kod postaje čišći i sigurniji.


# with neki_resurs as alias:
# # rad s resursom koristeći "alias"
# def send_request():
    # response = requests.get("https://catfact.ninja/fact")
    # fact = response.json()["fact"]
    # print(fact)

 #async with nemozes koristi izvan korutine, definiras main() korutinu i stavis unutar
 

 ### Ovo je asinkroni kod ali nije konkurentan , nema raspodjelu resursa, jer se idalje izvodi sekvencijalno
async def main():
    #konekciju otvaram 1. 
    async with aiohttp.ClientSession() as session:
        start_time = time.time()
        #for petlja za zahtjeve
        for _ in range(5):
            response = await session.get("https://catfact.ninja/fact") #sacekaj da response dode pa isprintaj, moras awaitat funkciju
            response_json = await response.json()
            print(response_json["fact"]) #["fact"]
            end_time= time.time()
        print("finished")
        print(f"vrijem itzvodenja {end_time - start_time:.2f}")


asyncio.run(main())







