import requests
import discord
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
	  
	@commands.command()
	@commands.check(is_owner)
	async def set_fn(self, ctx,*args):
	  embed=discord.Embed(title="使い方", description="```.fn <ユーザー名>```  Fortniteの成績を表示します", color=0x4273b5)
	  embed.set_footer(text=".helpでBOTのヘルプを表示")
	  await ctx.send(embed=embed)