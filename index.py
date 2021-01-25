import asyncio
import json
import platform
import discord

import modules


client = modules.Mybot()
client.add_cog(modules.Commands(client))
client.add_cog(modules.Commands_fn(client))
client.add_cog(modules.Commands_ch(client))
client.add_cog(modules.Music(client))
client.add_cog(modules.Poll(client))
client.add_cog(modules.Commands_test(client))

print(f'python {platform.python_version()}')
print("discord.py " + discord.__version__)
loop = asyncio.get_event_loop()

#loop.run_until_complete(modules.setup())

loop.run_until_complete(client.run("NzQzNzc2ODI1MTMzNjI5NTQw.XzZmJQ.4Cer4_pQghZHCtDwqHjzu8nPrec"))
