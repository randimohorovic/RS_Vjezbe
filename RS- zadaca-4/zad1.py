# import asyncio

# lista = [1,2,3,4,5,6,7,8,9,10]

# async def korutina(delay):
#     print("Dohvacanje podataka")
#     for i in lista:
#         print(f"Elemtent liste {i} ")
#         await asyncio.sleep(delay)
    
#     print("podaci dohvaceni")


# async def main():
#     await korutina(1)

# asyncio.run(main())


import asyncio

async def dohvati_podatke():

    await asyncio.sleep(3)
    podaci = [i for i in range(1, 10)]
    print("Podaci dohvaćeni.")
    return podaci


async def main():
    podaci = await dohvati_podatke()
    print(f"Dohvaćeni podaci: {podaci}")

asyncio.run(main())
