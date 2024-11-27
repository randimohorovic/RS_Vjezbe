#korutine -  asinkrone funkcije async, await
# asyncio.run(corutine)

import asyncio

# async def main():
#     print("hello")
#     await asyncio.sleep(1)
#     print("Hello")

# asyncio.run(main())


## timer, ali tu sad imas gatherio za spojit itd..
# async def timer(delay):
#     print("tajmer starts..")
#     for i in range (delay, 0, -1):
#         print(f"timer {i} sec.")
#         await asyncio.sleep(1)
#     print("kraj timera")


# async def main():
#     await timer(5)

# asyncio.run(main())


## asyncio taskovi,

# async def main():
#     task1 = asyncio.create_task(fetch_api_1())
#     task2 = asyncio.create_task(fetch_api_2())

#     podaci1 =await task1
#     podaci2 =await task1

    
# asyncio.run(main())

##def korutina mi treba sa skripte

async def korutina(n):
    await async

# async def main():
#     tasks = []
#     tasks_comp= [await asyncio.create_task(korutina(i)) for i in range (1,6)]
    
#     print(tasks_comp)

# asyncio.run(main())

##

import asyncio


async def dohvati_podatke():

    await asyncio.sleep(3)
    podaci = [broj for broj in range(1, 11)]
    print("Podaci dohvaćeni.")
    return podaci


async def main():
    podaci = await dohvati_podatke()
    print(f"Dohvaćeni podaci: {podaci}")

asyncio.run(main())
