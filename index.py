import modules
import asyncio
import json

json_open_config = open('config.json', 'r')
config = json.load(json_open_config)

client = modules.Mybot()
client.add_cog(modules.Commands(client))
client.add_cog(modules.Commands_fn(client))
client.add_cog(modules.Music(client))
client.add_cog(modules.Poll(client))
client.add_cog(modules.Commands_test(client))

loop = asyncio.get_event_loop()
loop.run_until_complete(client.run(config["TOKEN"]))
