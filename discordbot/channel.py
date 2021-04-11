from discord.ext import commands
import time
import json
import discord
import datetime
import pytz
import asyncio
import re


class Commands_ch(commands.Cog, name="チャンネル"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def addch(self, ctx, *args):
        category_id = ctx.message.channel.category_id
        category = ctx.message.guild.get_channel(744753562499678329)
        guild = self.bot.get_guild(ctx.guild.id)
        role = await guild.create_role(
            name=args[0] + "に参加できる権限", colour=discord.Colour.blue()
        )
        member = guild.get_member(ctx.author.id)
        await member.add_roles(role)
        guild = ctx.guild
        role_everyone = discord.utils.get(guild.roles, name="@everyone")
        dt_now = datetime.datetime.now(pytz.timezone("Asia/Tokyo"))
        new_channel = await category.create_text_channel(
            name=args[0],
            topic=f"{dt_now.strftime('%m月%d日 %H:%M:%S')}\n{ctx.author.display_name}によって作成されました",
        )
        await new_channel.set_permissions(role, read_messages=True, send_messages=True)
        await new_channel.set_permissions(role_everyone, view_channel=False)
        new_voice_channel = await category.create_voice_channel(name=args[0])
        await new_voice_channel.set_permissions(
            role, read_messages=True, send_messages=True
        )
        await new_voice_channel.set_permissions(role_everyone, view_channel=False)
        try:
            delete_time = int(args[1])
        except:
            delete_time = 10
        await new_channel.send(f"ここだよ{ctx.author.mention}\nロール:{role.mention}\n")
        message = await ctx.channel.send(
            f"☑チャンネルを作成しました\nテキストチャンネル:{new_channel.mention}\nボイスチャンネル:{new_voice_channel.mention}\nこのチャンネルは{delete_time}秒後に削除されます"
        )

        data = {
            args[0]: {
                "author": str(ctx.author.id),
                "text": str(new_channel.id),
                "voice": str(new_voice_channel),
            }
        }

        with open("config/data.json", "w") as outfile:
            json.dump(data, outfile)

        await asyncio.sleep(delete_time)
        await new_channel.delete()
        await new_voice_channel.delete()
        await role.delete()

    @commands.command()
    async def addch_role(self, ctx, *args):
        guild = self.bot.get_guild(ctx.guild.id)
        member = guild.get_member(args[0])
        role = discord.utils.get(guild.roles, name=f"@{ctx.channel.name}に参加できる権限")
        await member.add_roles(role)

    @commands.command()
    async def clear(ctx, number: int):
        pass
