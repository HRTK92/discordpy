import sanic
from sanic import Sanic
from sanic.response import json
import asyncio
app = Sanic()

@app.route('/')
async def test(request):
    return json({'hello': 'world'})

def setup():
    #app.run(host='0.0.0.0', port=8000, loop = asyncio.get_event_loop())
    pass