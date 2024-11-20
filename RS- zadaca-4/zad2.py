import asyncio

async def dohvati_podatke_korisnika():
    await asyncio.sleep(3)
    baza_korisnika = [
 {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
 {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
 {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
 {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]
    return baza_korisnika

async def dohvati_podatke_proizvoda():
    await asyncio.sleep(5)
    baza_proizvoda = [
 {'proizvod1': 'mirko123', 'email': 'mirko123@gmail.com'},
 {'proizvod2': 'ana_anic', 'email': 'aanic@gmail.com'}
]
    return baza_proizvoda

async def main():
    
    baza_korisnika, baza_proizvoda = await asyncio.gather(
        dohvati_podatke_korisnika(),
        dohvati_podatke_proizvoda()
    )

    print(baza_korisnika)
    print(baza_proizvoda)

asyncio.run(main())

