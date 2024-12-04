from aiohttp import web


app = web.Application()

async def ratio_list(request):
    podaci = await request.json()
    brojevi = podaci.get("brojevi")
    zbroj = podaci.get("zbroj")

    ratio_list = [rouund(broj/zbroj, 2) for broj in brojevi]
    print(ratio_list)
    return web.json_response({"zbroj": ratio_list})


app.router.add_post("/ration", ratio_list)

web.run_app(app, host="localhost", port=8081)