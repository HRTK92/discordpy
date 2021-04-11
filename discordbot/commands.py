import requests
import discord
from discord.ext import commands
import time
from gtts import gTTS
import urllib3
import datetime
import re
import json
import pytz
import feedparser
import asyncio
import subprocess
import aiohttp, requests


async def is_owner(ctx):
    return ctx.author.id == 618332297275375636


class Commands(commands.Cog, name="コマンド"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.check(is_owner)
    async def say(self, ctx, *args):
        num = re.sub("\\D", "", args[0])
        channel = self.bot.get_channel(int(num))
        await channel.send(args[1])

    @commands.command()
    async def speak(self, ctx, *args):
        tts_ja = gTTS(text=args[0], lang="ja", slow=False)
        tts_ja.save("text.mp3")

    @commands.command()
    @commands.check(is_owner)
    async def count(self, ctx, *args):
        guild = ctx.message.guild
        channel = guild.get_channel(636457818110820362)
        await channel.edit(name=f"👥メンバー数:{guild.member_count}")

    @commands.command()
    async def removech(self, ctx, *args):
        guild = self.bot.get_guild(ctx.guild.id)
        channel = discord.utils.get(guild.text_channels, name=args[0])
        await ctx.send()

    @commands.command()
    async def ynews(self, ctx, *args):
        """Yahooニュースを表示します"""
        RSS_URL = "https://news.yahoo.co.jp/rss/topics/top-picks.xml"
        d = feedparser.parse(RSS_URL)
        data = ""
        for entry in d.entries:
            data = data + f"{entry.title}\n"
            await asyncio.sleep(1)
            embed = discord.Embed(title=f"{entry.title}", color=0x00FF00)
            embed.add_field(
                name="description", value=f"{entry.description}\n\n[リンク]({entry.link})"
            )
            embed.set_footer(text=f"送信者:{ctx.author.display_name}")
            message = await ctx.send(embed=embed)
        # await ctx.send(data)

    @commands.command()
    async def role_members(self, ctx, *args):
        guild = self.bot.get_guild(ctx.guild.id)
        role = guild.get_role(int(args[0]))
        embed = discord.Embed(
            title=f"ロール:{role.name}", description=f"{role.id}", color=0x00FF00
        )
        members = ""
        for data in role.members:
            members = members + f"{data.name}\n"
        embed.add_field(name="人数", value=f"{len(role.members)}", inline=False)
        embed.add_field(name="リスト", value=f"{members}", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def role_add(self, ctx, *args):
        pass

    @commands.command(name="マイクラルール")
    async def mc_rule(self, ctx, *args):
        url = "https://raw.githubusercontent.com/HRTK92/HR.Snow-World/main/rule.md"
        response = requests.get(url)
        embed = discord.Embed(
            title="HR.Snowの世界-ルール",
            url=url,
            description=response.text,
            timestamp=datetime.datetime.utcnow(),
            color=0x00FFFF,
        )
        # embed.add_field(name="undefined", value=response.text, inline=False)
        embed.set_author(
            name="HRTK92",
            url="https://github.com/HRTK92",
            icon_url="https://avatars.githubusercontent.com/u/70054655?s=64&v=4",
        )
        embed.set_footer(text="最終更新時間")
        await ctx.message.delete()
        await ctx.send(embed=embed)

    @commands.command(name="やる事リスト")
    async def todo(self, ctx, *args):
        url = "https://api.github.com/repos/HRTK92/HR.Snow-World/projects?"
        response = requests.get(
            url, headers={"Accept": "application/vnd.github.inertia-preview+json"}
        )
        embed = discord.Embed(
            title="HR.Snowの世界-やる事リスト",
            description=response.text,
            timestamp=datetime.datetime.utcnow(),
            color=0x00FFFF,
        )
        # embed.add_field(name="undefined", value=response.text, inline=False)
        embed.set_author(
            name="HRTK92",
            url="https://github.com/HRTK92",
            icon_url="https://avatars.githubusercontent.com/u/70054655?s=64&v=4",
        )
        embed.set_footer(text="最終更新時間")
        await ctx.message.delete()
        await ctx.send(embed=embed)

    @commands.command()
    async def nick(self, ctx, member: discord.Member, nick):
        await member.edit(nick=nick)
        await ctx.send(f"Nickname was changed for {member.mention} ")
