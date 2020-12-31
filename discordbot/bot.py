import discord
import sys
import platform
from flask import Flask, request
import json
from PIL import Image, ImageDraw
import datetime
import requests
import logging
from . import music

from discord.ext import commands
bot = commands.Bot(command_prefix='!')

json_open_confing = open('confing.json', 'r')
confing = json.load(json_open_confing)
json_open_message = open('message.json', 'r')
message_template = json.load(json_open_message)


formatter = '%(levelname)s : %(asctime)s : %(message)s'
logging.basicConfig(
    filename='logger.log', level=logging.INFO, format=formatter)


#discord
print("ログインしています……\n")

class Mybot(discord.client):
  async def on_ready(self):
    activity = discord.Activity(name=confing["activity"], type=discord.ActivityType.watching)
    await self.change_presence(activity=activity)
    print("-----------------------")
    print('ログインしました')
    print(f'ユーザー名:{self.user}')
    print(f'アクティビティ:{confing["activity"]}')
    print(f'python {platform.python_version()}')
    print("discord.py " + discord.__version__)
    print(f'\n')
  async def on_message(message):
    print(f'[{message.author}] [{message.channel}] | {message.content}')
    if message.content in "@":
      channel = self.get_channel(confing["server"]["622206625586872323"]["channel"]["log"])
      await message.delete()
    if message.content == "help":
			embed = discord.Embed(title="ボットコマンドの使い方", description="")
			embed.add_field(name="news", value="Fortnite News を表示します")
			embed.add_field(name="fn <ユーザー名>", value="成績を表示します by fortnite-api")
			embed.add_field(name="map", value="マップを表示します")
			embed.timestamp = datetime.datetime.now()
			await message.channel.send(embed=embed)
		if message.content == "confing":
			embed = discord.Embed(title="data", description="", color=0x0000ff)
			embed.add_field(name="config.json", value=confing)
			await message.channel.send(embed=embed)
		if message.content == "send_message":
		  await message.delete()
		  await message.channel.send("?")
		if message.content.startswith("editmessage"):
		  msg = message.content.split()
		  editmessage = await self.fetch_message(msg[1])
		  await editmessage.edit(content = msg[2])
		  print()
		if message.content == "test":
			await message.channel.send("!")
	  #Fortnite-----------------------
		if message.content == "news":
			res_lang = "ja"
			response = requests.get(
			    f'https://fortnite-api.com/v2/news/br?language={res_lang}')
			geted = response.json()
			if response.status_code == 200:
				text = "Fortnite News"
				image = geted['data']['image']
				embed = discord.Embed(title=text, color=0x00ff00)
				embed.set_image(url=image)
				await message.channel.send(embed=embed)
		if message.content.startswith("map"):
			text = "Fortnite map"
			embed = discord.Embed(title=text, color=0x00ff00)
			embed.set_image(url="https://media.fortniteapi.io/images/map.png")
			await message.channel.send(embed=embed)
		if message.content.startswith("fn"):
			edit = await message.channel.send("データを取得中……")
			async with message.channel.typing():
			  pass
			msg = message.content
			nameold = msg.split()
			name = msg.replace("fn ", "")
			res_lang = "ja"
			response = requests.get(
			    f'https://fortnite-api.com/v1/stats/br/v2?name={name}&image=all')
			geted = response.json()
			if response.status_code == 200:
				text = f'Fortnite Players Data : [{name}]'
				image = geted['data']['image']
				embed = discord.Embed(title=text, color=0x00ff00)
				embed.add_field(
				    name="link",
				    value=
				    f'[fortnitetracker](https://fortnitetracker.com/profile/all/{name})'
				)
				embed.set_image(url=image)
				await edit.edit(content="", embed=embed)
			if response.status_code == 404:
				text = f'Fortnite Player Data : [{name}]'
				embed = discord.Embed(title=text, color=0xff0000)
				embed.add_field(
				    name="読み込みに失敗しました(status_code 404)",
				    value=f'内容:{geted["error"]}')
				await edit.edit(content="", embed=embed)
		if message.content == "challenge":
			lang = "ja"
			headers = {"Authorization": confing["fortnite-api"]}
			response = requests.get(
			    f'https://fortniteapi.io/v1/challenges?season=current&lang={lang}',
			    headers=headers)
			geted = response.json()
		if message.content == "shop":
			lang = "ja"
			headers = {"Authorization": confing["fortnite-api"]}
			response = requests.get(
			    f'https://fortniteapi.io/v1/shop?lang={lang}', headers=headers)
			geted = response.json()
			print(geted)
		#-----------------------
		#voice
		if message.content == "!join":
			if message.author.voice is None:
				await message.channel.send("あなたはボイスチャンネルに接続していません。")
				return
			await message.author.voice.channel.connect()
			await message.channel.send("接続しました。")
		if message.content == "!leave":
			if message.guild.voice_self is None:
				await message.channel.send("接続していません。")
				return
			# 切断する
			await message.guild.voice_self.disconnect()
			await message.channel.send("切断しました。")
		if message.content == "!play":
			if message.guild.voice_self is None:
				await message.channel.send("接続していません。")
				return
			message.guild.voice_self.play(
			    discord.FFmpegPCMAudio("example.mp3", volume=0.5))
		#-----------------------
		#サーバー
		if message.content == "invite":
			invite = await message.guild.invites()
			await message.channel.send(f'{invite}')
		if message.content.startswith("nick "):
			name = message.content.replace("nick ", "")
			await message.edit(nick=name)
		if message.content.startswith("/"):
			await message.channel.send()
		#-----------------------
	
	
	
	async def on_member_join(member):
		channel = self.get_channel(
		    confing["server"]["622206625586872323"]["channel"]["Notice"])
		sendmessage = message_template["member_join"].format(member.display_name)
		await channel.send(sendmessage)
		role = guild.get_role("636456351375163402")
		await member.add_roles(role)
		await channel.send(sendmessage)
	
	async def on_member_update(before, after):
	  print(before, after)

client = Mybot()
client.run('NzQzNzc2ODI1MTMzNjI5NTQw.XzZmJQ.4Cer4_pQghZHCtDwqHjzu8nPrec"')