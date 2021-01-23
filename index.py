import modules
import asyncio
import json
import platform
import discord

json_open_config = open('config.json', 'r')
config = json.load(json_open_config)

client = modules.Mybot()
client.add_cog(modules.Commands(client))
client.add_cog(modules.Commands_fn(client))
client.add_cog(modules.Commands_ch(client))
client.add_cog(modules.Music(client))
client.add_cog(modules.Poll(client))
client.add_cog(modules.Commands_test(client))
client.add_cog(modules.Commands_chess(client))
print(f'python {platform.python_version()}')
print("discord.py " + discord.__version__)
loop = asyncio.get_event_loop()
loop.run_until_complete(client.run(config["TOKEN"]))
