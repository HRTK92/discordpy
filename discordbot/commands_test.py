import requests
from discord.ext import commands
import time
import json
json_open_config = open('config.json', 'r')
config = json.load(json_open_config)
class Commands_test(commands.Cog, name='テスト'):
	def __init__(self, bot):
		self.bot = bot
	@commands.command()
	async def test(self, ctx):
	  channel_id = config["servers"][str(ctx.guild.id)]["channels"]["Notice"]
	  channel = self.bot.get_channel(channel_id)
	  await channel.send('!')