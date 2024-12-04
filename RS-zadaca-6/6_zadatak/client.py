# client.py
import aiohttp
import asyncio
import time
#import microservice_1 # NE
#import microservice_2 # NE

async def fetch_service1(url, port):
    async with aiohttp.ClientSession() as session:
        response = await session.get(f'http://{url}:{port}/pozdrav')
        return await response.json()


async def fetch_service2(url, port):
    async with aiohttp.ClientSession() as session:
        response = await session.get(f'http://{url}:{port}/pozdrav')
        return await response.json()


async def konkurentno():
    print("Pokrećem main korutinu")
    results = await asyncio.gather(fetch_service1('localhost', 8081), fetch_service2('localhost', 8082)) # konkurentno slanje zahtjeva, vraća listu rječnika
    print(results)

async def sek():
    
    result1 = await fetch_service1('localhost', 8081) 
    result2 = await fetch_service2('localhost', 8082) 
    print(result1)
    print(result2)

async def main():
    await konkurentno()
    await sek()


asyncio.run(main())