# import asyncio

# asyncio.run(coroutine)


import asyncio
async def fetch_api_1():
    print('Dohvaćam podatke s API-ja 1...')
    await asyncio.sleep(2)
    print('Podaci s API-ja 1 dohvaćeni.')
    return {'api_1': 'uspješno'}



async def fetch_api_2():
    print('Dohvaćam podatke s API-ja 2...')
    await asyncio.sleep(4)
    print('Podaci s API-ja 2 dohvaćeni.')
    return {'api_2': 'uspješno'}

# async def main():
#     podaci_1 = await fetch_api_1()
#     podaci_2 = await fetch_api_2()
#     print(f'Podaci s API-ja 1: {podaci_1}')
#     print(f'Podaci s API-ja 2: {podaci_2}')

# async def main():
#     podaci_1, podaci_2 = await asyncio.gather(fetch_api_1(), fetch_api_2())
#     print(f'Podaci s API-ja 1: {podaci_1}')
#     print(f'Podaci s API-ja 2: {podaci_2}')

# async def main():
#     task_1 = asyncio.create_task(fetch_api_1())
#     task_2 = asyncio.create_task(fetch_api_2())
#     podaci_1 = await task_1
#     podaci_2 = await task_2
#     print(f'Podaci s API-ja 1: {podaci_1}')
#     print(f'Podaci s API-ja 2: {podaci_2}')


asyncio.run(main())


# asyncio.create_task()


