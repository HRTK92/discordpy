import discord
import sys
import platform
import json
import datetime
import requests
import logging
from . import music

from discord.ext import commands

json_open_config = open('config/config.json', 'r')
config = json.load(json_open_config)

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(
    filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(
    logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

prefix = '.'

#discord
print("ログインしています……\n")


class Mybot(commands.Bot):
	def __init__(self) -> None:
		intents = discord.Intents.default()
		intents.members = True
		super().__init__(
		    command_prefix=".",
		    intents=discord.Intents.all(),
		    #intents=intents,
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
	async def on_member_join(self, member):
		guild = member.guild
		if guild.system_channel is not None:
			to_send = f'{member.mention}ようこそ サーバーへ\nサーバー管理者 <@618332297275375636> \nhttps://discord.gg/vXgDnP7'
			await guild.system_channel.send(to_send)
		channel = guild.get_channel(636457818110820362)
		await channel.edit(name=f"メンバー数:{guild.member_count}")
	async def on_member_remove(self, member):
		guild = member.guild
		channel = guild.get_channel(636457818110820362)
		await channel.edit(name=f"メンバー数:{guild.member_count}")
	async def on_member_update(self, before, after):
	  pass


class JapaneseHelpCommand(commands.DefaultHelpCommand):
	def __init__(self):
		super().__init__()
		self.commands_heading = "コマンド:"
		self.no_category = "その他"
		self.command_attrs["help"] = "コマンド一覧と簡単な説明を表示"

	def get_ending_note(self):
		return (f"プレフィックス {prefix}\n各コマンドの説明: {prefix}help <コマンド名>\n"
		        f"各カテゴリの説明: {prefix}help <カテゴリ名>\n")


def setup():
	client = Mybot()
	client.run('NzQzNzc2ODI1MTMzNjI5NTQw.XzZmJQ.4Cer4_pQghZHCtDwqHjzu8nPrec')
