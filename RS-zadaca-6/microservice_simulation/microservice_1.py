# microservice_1.py

from aiohttp import web
async def handle_service1(request):
    
    return web.json_response({"message": "Hello from Microservice 1"})


app = web.Application()
app.router.add_get('/', handle_service1)

if __name__ == "__main__":
    web.run_app(app, port=8081)
