import discord
import sys
import platform
from flask import Flask, request
import json
from PIL import Image, ImageDraw
import datetime
import requests
import logging
from discord.ext import commands
bot = commands.Bot(command_prefix='>')

json_open_confing = open('confing.json', 'r')
confing = json.load(json_open_confing)
client = discord.Client()

formatter = '%(levelname)s : %(asctime)s : %(message)s'
logging.basicConfig(
    filename='logger.log', level=logging.INFO, format=formatter)
app = Flask(__name__)


#Flask
@app.route("/")
def hello_world():
	return "起動中"


@app.route("/webhook", methods=['POST'])
def callback():
	signature = request.headers['X-Line-Signature']
	body = request.get_data(as_text=True)
	app.logger.info("Request body: " + body)
	try:
		handler.handle(body, signature)
	except InvalidSignatureError:
		abort(400)
	return 'OK'


#discord
print("ログインしています……\n")


@client.event
async def on_ready():
  activity = discord.Activity(name=confing["activity"], type=discord.ActivityType.watching)
  await client.change_presence(activity=activity)
  print("-----------------------")
  print('ログインしました')
  print(f'ユーザー名:{client.user}')
  print(f'アクティビティ:{confing["activity"]}')
  print(f'python {platform.python_version()}')
  print("discord.py " + discord.__version__)
  print(f'\n')

@client.event
async def on_message(message):
	if message.author.bot:
		return
	logging.info(f'[{message.author}] [{message.channel}] | {message.content}')
	print(f'[{message.author}] [{message.channel}] | {message.content}')
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
	if message.content == "test":
		await message.channel.send("!")
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
			embed.add_field(name="読み込みに失敗しました", value=f'内容:{geted["error"]}')
			await edit.edit(content="", embed=embed)
	if message.content == "item":
		joinedArgs = "ブラック"
		response_lang = "ja"
		response = requests.get(
		    f'https://fortnite-api.com/v2/cosmetics/br/search/all?name={joinedArgs}&matchMethod=starts&language={response_lang}&searchLanguage={request_lang}'
		)
		geted = response.json()
		print(geted)
		if response.status_code == 200:
			mbed_count = 0
			item_left_count = 0
			for item in geted['data']:
				if embed_count != 200:
					embed_count += 1
					item_id = item['id']
					item_name = item['name']
					item_description = item['description']
					item_icon = item['images']['icon']
					item_introduction = item['introduction']['text']
					item_rarity = item['rarity']['displayValue']
					if item['set'] == None:
						item_set = text()['none']
					else:
						item_set = "アイテム"
						name = "名前"
						desc = ""
						intro = ""
						of_set = ""
						txt_id = ""
						rarity = ""
				embed = discord.Embed(
				    title=f'{item_name}', color=color(item['rarity']['value']))
				embed.add_field(name=desc, value=f'`{item_description}`')
				embed.add_field(name=txt_id, value=f'`{item_id}`')
				embed.add_field(name=intro, value=f'`{item_introduction}`')
				embed.add_field(name=of_set, value=f'`{item_set}`')
				embed.add_field(name=rarity, value=f'`{item_rarity}`')
				embed.set_thumbnail(url=item_icon)
				await message.channel.send(embed=embed)
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
	if message.content =="invite":
	  invite = await message.guild.invites()
	  await message.channel.send(f'{invite}')
	if message.content.startswith("nick "):
	  name = message.content.replace("nick ", "")


@client.event
async def on_member_join(member):
	channel = client.get_channel(
	    confing["server"]["622206625586872323"]["channel"]["Notice"])
	await channel.send(
	    f'ようこそサーバーへ {member.display_name}\nサーバー管理者:<@618332297275375636>\nhttps://discord.gg/vXgDnP7'
	)


client.run(confing["TOKEN"])


@bot.command()
async def ping(ctx):
	await ctx.send('pong')
