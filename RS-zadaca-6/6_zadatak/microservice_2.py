from aiohttp import web
import time

async def handle_service1(request):
    time.sleep(4)
    return web.json_response({"message": "pozdrav nakon 4 sekudne"})


app = web.Application()
app.router.add_get('/pozdrav', handle_service1)

if __name__ == "__main__":
    web.run_app(app, port=8082)
