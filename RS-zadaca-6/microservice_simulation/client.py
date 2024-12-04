# client.py
import aiohttp
import asyncio
import time
#import microservice_1 # NE
#import microservice_2 # NE

async def fetch_service1():
    async with aiohttp.ClientSession() as session:
        response = await session.get('http://localhost:8081/')
        return await response.json()

async def fetch_service2():
    async with aiohttp.ClientSession() as session:
        response = await session.get('http://localhost:8082/')
        return await response.json()




async def main():
    print("Pokrećem main korutinu")
    results = await asyncio.gather(fetch_service1(), fetch_service2()) # konkurentno slanje zahtjeva, vraća listu rječnika
    print(results)



asyncio.run(main())