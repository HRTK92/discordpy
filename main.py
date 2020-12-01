import discord
import json
import datetime
import requests
from discord.ext import commands
bot = commands.Bot(command_prefix='>')

json_open_confing = open('confing.json', 'r')
confing = json.load(json_open_confing)
client = discord.Client()


@client.event
async def on_ready():
	print('ログインしました')
	print("discord.py" + discord.__version__)
	print()


@client.event
async def on_message(message):
	if message.author.bot:
		return
	print(f'[{message.author}] [{message.channel}]| {message.content}')
	if message.content == "help":
		embed = discord.Embed(title="ボットコマンドの使い方", description="説明")
		embed.add_field(name="news",value="Fortnite News を表示します")
		embed.timestamp = datetime.datetime.now()
		await message.channel.send(embed=embed)
	if message.content == "confing":
		guildid = message.guild.id
		await message.channel.send(guildid)
		await message.channel.send(
		    confing["server"]["622206625586872323"])
	if message.content == "test":
		data = requests.get("https://fortnite-api.com/v1/map")
		await message.channel.send(data['data']['images']['blank'])
	if message.content == "news":
	  res_lang = "ja"
	  response = requests.get(f'https://fortnite-api.com/v2/news/br?language={res_lang}')
	  geted = response.json()
	  if response.status_code == 200:
	    text = "Fortnite News"
	    image = geted['data']['image']
	    embed = discord.Embed(title=text)
	    embed.set_image(url=image)
	    await message.channel.send(embed=embed)
	if message.content == "map":
	  res_lang = "ja"
	  response = requests.get(f'https://fortnite-api.com/v1/news/map?language={res_lang}')
	  geted = response.json()
	  if response.status_code == 200:
	    text = "Fortnite map"
	    image = geted['data']['images']['pois']
	    embed = discord.Embed(title=text)
	    embed.set_image(url=image)
	    await message.channel.send(embed=embed)
	if message.content == "item":
	  joinedArgs = "ブラック"
	  response_lang = "ja"
	  response = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/search/all?name={joinedArgs}&matchMethod=starts&language={response_lang}&searchLanguage={request_lang}')
	  geted = response.json()
	  print(geted)
	  if response.status_code == 200:
	    mbed_count=0
	    item_left_count=0
	    for item in geted['data']:
	      if embed_count !=200:
	        embed_count+=1
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
	      embed = discord.Embed(title=f'{item_name}', color=color(item['rarity']['value']))
	      embed.add_field(name=desc, value=f'`{item_description}`')
	      embed.add_field(name=txt_id, value=f'`{item_id}`')
	      embed.add_field(name=intro, value=f'`{item_introduction}`')
	      embed.add_field(name=of_set, value=f'`{item_set}`')
	      embed.add_field(name=rarity, value=f'`{item_rarity}`')
	      embed.set_thumbnail(url=item_icon)
	      await message.channel.send(embed=embed)

   
@client.event
async def on_member_join(member):
	guildid = message.guild.id
	channel = client.get_channel(
	    confing["servers"]["622206625586872323"]["channel"]["Notice"])
	await channel.send(f'ようこそサーバーへ {member}\nサーバー管理者:<@618332297275375636>\nhttps://discord.gg/vXgDnP7')


client.run(confing["TOKEN"])






@bot.command()
async def ping(ctx):
    await ctx.send('pong')