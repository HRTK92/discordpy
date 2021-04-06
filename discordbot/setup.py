import asyncio
import json
import platform
import discord
from discord_slash import SlashCommand, SlashContext

import discordbot


    
def start(token):
  client = discordbot.Mybot()
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