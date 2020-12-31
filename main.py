import discordbot

client = discordbot.Mybot()
client.add_cog(discordbot.Commands(client))
client.add_cog(discordbot.Commands_fn(client))
client.add_cog(discordbot.Music(client))
client.add_cog(discordbot.Commands_test(client))
client.run("NzQzNzc2ODI1MTMzNjI5NTQw.XzZmJQ.4Cer4_pQghZHCtDwqHjzu8nPrec")