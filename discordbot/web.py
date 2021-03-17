from aiohttp import web


async def handle(request):
	name = request.match_info.get('name', "Anonymous")
	text = "Hello, " + name
	return web.Response(text=text)

async def setup():
  app = web.Application()
  app.add_routes([web.get('/', handle), web.get('/{name}', handle)])
  await web.run_app(app)
