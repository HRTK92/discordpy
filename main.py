import discord
import json
import datetime
import requests

json_open_confing = open('confing.json', 'r')
confing = json.load(json_open_confing)
client = discord.Client()


@client.event
async def on_ready():
	print('ログインしました')
	print("discord.py" + discord.__version__)
	print("トークン:\n" + confing["TOKEN"])


@client.event
async def on_message(message):
	if message.author.bot:
		return
	print(message)
	if message.content == "help":
		embed = discord.Embed(title="ボットコマンドの使い方", description="説明")
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


@client.event
async def on_member_join(member):
	guildid = message.guild.id
	channel = client.get_channel(
	    confing["servers"]["622206625586872323"]["channel"]["Notice"])
	await channel.send("")


client.run(confing["TOKEN"])
