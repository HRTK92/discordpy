import requests
from discord.ext import commands
import time
import json
import discord

class Commands_test(commands.Cog, name='テスト'):
	def __init__(self, bot):
		self.bot = bot
	@commands.command()
	async def test(self, ctx):
	  guild = ctx.guild
	  role = discord.utils.get(guild.roles, name="@everyone")
	  print(role.id)