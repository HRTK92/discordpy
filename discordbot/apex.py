class Commands_fn(commands.Cog, name="Apex β版"):
    def __init__(self, bot):
        self.bot = bot

        @commands.command()
        async def map(self, ctx):
            """Apex"""
            text = "Fortnite map"
            embed = discord.Embed(title=text, color=0x00FF00)
            embed.set_image(url="https://media.fortniteapi.io/images/map.png")
            await ctx.send(embed=embed)
