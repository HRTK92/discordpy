import requests
import discord
from discord.ext import commands
import time
async def is_owner(ctx):
    return ctx.author.id == 618332297275375636
class Poll(commands.Cog, name='投票'):
	def __init__(self, bot):
		self.bot = bot
	@commands.command()
	async def poll(self, ctx,*args):
	  poll_list = ""
	  poll_number = 0
	  for i in args:
	    poll_number + 1
	    poll_list += f'{poll_number}、{i}  '
	  embed=discord.Embed(title=f'投票 : {args[0]}', description="説明", color=0xe600ff)
	  embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
	  await ctx.send(embed=embed)
	  