from aiohttp import web


app = web.Application()

async def sum_handle(request):
    podaci = await request.json()
    brojevi = podaci.get("brojevi")
    zbroj = sum(brojevi)
    return web.json_response({"zbroj": zbroj})


app.router.add_post("/zbroj", sum_handle)

web.run_app(app, host="localhost", port=8080)