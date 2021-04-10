import asyncio
import json
import platform
import discord
from discord_slash import SlashCommand, SlashContext

import discordbot


    
def start(token):
  client = discordbot.Mybot(
    settings=discordbot.Settings(),
    )
  client.add_cog(discordbot.Commands(client))
  client.add_cog(discordbot.Commands_ch(client))
  client.add_cog(discordbot.Commands_fn(client))
  client.add_cog(discordbot.Music(client))
  client.add_cog(discordbot.Poll(client))
  client.add_cog(discordbot.Commands_test(client))
  print(f'python {platform.python_version()}')
  print("discord.py " + discord.__version__)
  print('discord.py Rapptz')
  loop = asyncio.get_event_loop()
  loop.run_until_complete(client.run(token))
  
class Settings:
  def __init__(self):
    self.debug_guild_id = 622206625586872323
    self.debug_channel_id = 830036485675155526
    self.fortnite_api = "6ef723f9-d83f254a-d4f28575-c34e5374"
    self.command_prefix = "."
    self.activity = "起　動　中"