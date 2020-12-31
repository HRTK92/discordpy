import requests
from discord.ext import commands
import time
async def is_owner(ctx):
    return ctx.author.id == 618332297275375636
class Commands(commands.Cog, name='コマンド'):
	def __init__(self, bot):
		self.bot = bot
	@commands.command()
	@commands.check(is_owner)
	async def say(self, ctx,*args):
	  channel=self.bot.get_channel(int(args[0]))
	  await channel.send(args[1])