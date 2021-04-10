import requests
import discord
from discord.ext import commands
import time
import datetime, pytz
from discord_slash import cog_ext, SlashContext
async def is_owner(ctx):
    return ctx.author.id == 618332297275375636
class Poll(commands.Cog, name='投票'):
	def __init__(self, bot):
		self.bot = bot
	
		
	@commands.command()
	async def poll(self, ctx,question, *options: str):
	  if len(options) <= 1:
	    await ctx.send('投票を行うには、複数のオプションが必要です。')
	    return
	  if len(options) > 10:
	    await ctx.send('あなたは10以上のもののために投票をすることはできません！')
	    return
	  if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
	    reactions = ['✅', '❌']
	  else:
	    reactions = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣', '🔟']
	  description = []
	  for x, option in enumerate(options):
	    description += '\n {} {}'.format(reactions[x], option)
	  embed = discord.Embed(color=0x4a4aff)
	  embed.add_field(name="🔎質問🔎", value=question, inline=False)
	  embed.add_field(name="🗒️選択肢🗒️", value=''.join(description), inline=False)
	  dt_now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))#datetime.datetime.now()
	  embed.add_field(name="🕰️受け付けた時間🕰️", value=dt_now.strftime('%Y年%m月%d日 %H:%M:%S'), inline=True)
	  embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
	  embed.set_footer(text="投票｜集計するには「🔵」を追加してください")
	  react_message = await ctx.send(embed=embed)
	  for reaction in reactions[:len(options)]:
	    await react_message.add_reaction(reaction)
	  #await react_message.add_reaction('🔵')