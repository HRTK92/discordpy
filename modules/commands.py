import requests
import discord
from discord.ext import commands
import time
from gtts import gTTS
import urllib3
import datetime
import re
import json
import pytz


async def is_owner(ctx):
	return ctx.author.id == 618332297275375636


class Commands(commands.Cog, name='コマンド'):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	@commands.check(is_owner)
	async def say(self, ctx, *args):
	  num = re.sub("\\D", "", args[0])
	  channel = self.bot.get_channel(int(num))
	  await channel.send(args[1])

	@commands.command()
	@commands.check(is_owner)
	async def set_fn(self, ctx, *args):
		embed = discord.Embed(
		    title="使い方",
		    description="```.fn <ユーザー名>```  Fortniteの成績を表示します",
		    color=0x4273b5)
		embed.set_footer(text=".helpでBOTのヘルプを表示")
		await ctx.send(embed=embed)

	@commands.command()
	@commands.check(is_owner)
	async def speak(self, ctx, *args):
		tts_ja = gTTS(text=args[0], lang='ja', slow=False)
		tts_ja.save("text.mp3")

	@commands.command()
	@commands.check(is_owner)
	async def count(self, ctx, *args):
		guild = ctx.message.guild
		channel = guild.get_channel(636457818110820362)
		await channel.edit(name=f"メンバー数:{guild.member_count}")

	@commands.command()
	async def create_invite(self, ctx):
		"""- Create instant invite"""
		link = await discord.abc.GuildChannel.create_invite(
		    self, max_age='300')
		await ctx.send("Here is an instant invite to your server: " + link)

	@commands.command()
	async def addch(self, ctx, *args):
		category_id = ctx.message.channel.category_id
		category = ctx.message.guild.get_channel(744753562499678329)
		guild = self.bot.get_guild(ctx.guild.id)
		role = await guild.create_role(name=args[0]+"に参加権限")
		overwrites = {
		    #guild.default_role:discord.PermissionOverWrite(send_messages=False),
		    #guild.me: discord.PermissionOverWrite(send_messages=True)
		}
		dt_now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
		new_channel = await category.create_text_channel(name=args[0], overwrites=overwrites, topic=f"{dt_now.strftime('%m月%d日 %H:%M:%S')}\n{ctx.author.display_name}によって作成されました")
		await new_channel.set_permissions(role,read_messages=True,send_messages=True)
		new_voice_channel=await category.create_voice_channel(name=args[0])
		await new_voice_channel.set_permissions(role,read_messages=True,send_messages=True)
		delete_time = int(args[1])
		text = f'{new_channel.mention} を作成しました\nこのチャンネルは{delete_time}秒後に削除されます'
		await new_channel.send(f'ここだよ{ctx.author.mention}')
		await ctx.channel.send(text)
		data = {args[0]:{"author":str(ctx.author.id),"text":str(new_channel.id),"voice":str(new_voice_channel)}}
		
		with open("config/data.json", 'w') as outfile:
		  json.dump(data, outfile)
		  
		time.sleep(delete_time)
		await new_channel.delete()
		await new_voice_channel.delete()
		await role.delete()

	@commands.command()
	async def removech(self, ctx, *args):
	  guild = self.bot.get_guild(ctx.guild.id)
	  channel = discord.utils.get(guild.text_channels, name=args[0])
	  await ctx.send(channel)