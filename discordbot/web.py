import asyncio
import aiohttp
import threading

def start_web():
	loop = asyncio.new_event_loop()
	asyncio.set_event_loop(loop)
	web = aiohttp.web.Application()
	aiohttp.web.run_app(app, loop=lop)