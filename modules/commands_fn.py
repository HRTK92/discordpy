import discord
import requests
from discord.ext import commands
import time

class Commands_fn(commands.Cog, name='fortnite'):
	def __init__(self, bot):
		self.bot = bot
	@commands.command()
	async def map(self, ctx):
		"""fortnite mapを表示する"""
		text = "Fortnite map"
		embed = discord.Embed(title=text, color=0x00ff00)
		embed.set_image(url="https://media.fortniteapi.io/images/map.png")
		await ctx.send(embed=embed)

	@commands.command()
	async def news(self, ctx):
		"""Fortnite Newsを表示する"""
		res_lang = "ja"
		response = requests.get(
		    f'https://fortnite-api.com/v2/news/br?language={res_lang}')
		geted = response.json()
		if response.status_code == 200:
			text = "Fortnite News"
			image = geted['data']['image']
			embed = discord.Embed(title=text, color=0x00ff00)
			embed.set_image(url=image)
			await ctx.send(embed=embed)

	@commands.command()
	async def fn(self, ctx, *args):
		"""Fortnite 成績を表示する fn <ユーザー名>"""
		await ctx.message.delete()
		joinedArgs = ('+'.join(args))
		edit = await ctx.send(f'{joinedArgs}のデータを取得中……')
		res_lang = "ja"
		response = requests.get(
		    f'https://fortnite-api.com/v1/stats/br/v2?name={joinedArgs}&image=all'
		)
		geted = response.json()
		if response.status_code == 200:
			text = f'Fortnite プレイヤー成績情報 : [{joinedArgs}]'
			image = geted['data']['image']
			embed = discord.Embed(title=text, color=0x00ff00)
			embed.add_field(
			    name="link",
			    value=
			    f'[fortnitetracker](https://fortnitetracker.com/profile/all/{joinedArgs})'
			)
			embed.set_image(url=image)
			embed.set_footer(text=f'送信者:{ctx.author.display_name}')
			await edit.edit(content="", embed=embed)
		if response.status_code == 404:
			text = f'Fortnite プレイヤー成績情報 : [{joinedArgs}]'
			embed = discord.Embed(title=text, color=0xff0000)
			embed.add_field(
			    name="読み込みに失敗しました(status_code 404)",
			    value=f'内容:{geted["error"]}')
			embed.set_footer(text=f'送信者:{ctx.author.display_name}')
			await edit.edit(content="", embed=embed)
		if ctx.channel.id == 794100709271535646:
		  send = True
		  if send :
		    time.sleep(2)
		    embed=discord.Embed(title="使い方", description="```.fn <ユーザー名>```Fortniteの成績を表示します", color=0x4273b5)
		    embed.set_footer(text=".helpでBOTのヘルプを表示")
		    await ctx.send(embed=embed)
		  time.sleep(20)
		  await edit.delete()