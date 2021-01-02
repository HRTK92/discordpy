import discordbot
import json

json_open_config = open('config.json', 'r')
config = json.load(json_open_config)

client = discordbot.Mybot()
client.add_cog(discordbot.Commands(client))
client.add_cog(discordbot.Commands_fn(client))
client.add_cog(discordbot.Music(client))
client.add_cog(discordbot.Poll(client))
client.add_cog(discordbot.Commands_test(client))
client.run(config["TOKEN"])
