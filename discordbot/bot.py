import discord
import sys
import platform
import json
import datetime
import requests
import logging
from . import music
import asyncio
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from sanic import Sanic
from sanic.response import json as sanic_json

app = Sanic(__name__)
@app.route('/')
async def test(request):
    return sanic_json({'hello': 'world'})
    
json_open_config = open('config/config.json', 'r')
config = json.load(json_open_config)

logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)

loop = asyncio.get_event_loop()



class Mybot(commands.Bot):
	def __init__(self) -> None:
		self.config = config,
		intents = discord.Intents.default()
		intents.members = True
		super().__init__(
		    command_prefix=config["command_prefix"],
		    loop=loop,
		    intents=discord.Intents.all(),
		    owner_id=618332297275375636,
		    activity=discord.Activity(
		        name=config["activity"], type=discord.ActivityType.watching),
		    help_command=JapaneseHelpCommand())

	async def on_ready(self):
		print("-----------------------")
		print('ログインしました')
		print(f'ユーザー名:{self.user}')
		print(f'アクティビティ:{config["activity"]}')
		print(f'\n')
		#await app.create_server(host='0.0.0.0', return_asyncio_server=True)
		
	async def on_message(self, message):
		print(f"{message.author.name}｜{message.content}")
		await self.process_commands(message)
		
	async def on_member_join(self, member):
		guild = member.guild
		if guild.system_channel is not None:
			to_send = f'{member.mention}ようこそ サーバーへ\nサーバー管理者 <@618332297275375636> \nhttps://discord.gg/vXgDnP7'
			await guild.system_channel.send(to_send)
		channel = guild.get_channel(636457818110820362)
		await channel.edit(name=f"👥メンバー数:{guild.member_count}")
		#await app.create_server(host="0.0.0.0", port=8000, return_asyncio_server=True)

	async def on_member_remove(self, member):
		guild = member.guild
		channel = guild.get_channel(636457818110820362)
		await channel.edit(name=f"👥メンバー数:{guild.member_count}")

	async def on_member_update(self, before, after):
		pass

	#reaction
	async def on_raw_reaction_add(self, payload):
		print("、")


class JapaneseHelpCommand(commands.DefaultHelpCommand):
	def __init__(self):
		super().__init__()
		self.commands_heading = "コマンド:"
		self.no_category = "その他"
		self.command_attrs["help"] = "コマンド一覧と簡単な説明を表示"

	def get_ending_note(self):
		return (
		    "プレフィックス {0}\n各コマンドの説明: {0}help <コマンド名>\n"
		    "各カテゴリの説明: {0}help <カテゴリ名>\n\n\ndiscord.py: {1}"
		).format(config["command_prefix"], discord.__version__)

