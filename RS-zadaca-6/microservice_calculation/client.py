import aiohttp
import asyncio

async def fetch_service_1():
    async with aiohttp.ClientSession() as session:
        podatak_koj_saljemo = {"brojevi": brojevi, "zbroj": zbroj}
        res = await session.post("http://localhost:8080/zbroj", json=podatak_koj_saljemo)
        return await res.json()
    
async def fetch_service_2():
    async with aiohttp.ClientSession() as session:
        podatak_koj_saljemo = {"brojevi": brojevi}
        res = await session.post("http://localhost:8081/ratio", json=podatak_koj_saljemo)
        return await res.json()


async def main():
    print("start")
    brojevi = [i for i in range(1,11)]
    print(brojevi)

    zbroj_dict = await fetch_service_1(brojevi)

 

    print(zbroj)

asyncio.run(main())