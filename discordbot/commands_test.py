import requests
from discord.ext import commands
import time

class Commands_test(commands.Cog, name='テスト'):
	def __init__(self, bot):
		self.bot = bot
	@commands.command()
	async def test(self, ctx):
		pass