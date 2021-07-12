import sys,os
import traceback
import platform
import json
import datetime
import requests
import datetime
import discord
import asyncio
import sqlite3
from discord.ext import commands, tasks
from discord_slash import SlashCommand, SlashContext
from sanic import Sanic
from sanic.response import json as sanic_json
from .setup import Settings
from . import music




class Mybot(commands.Bot):
    def __init__(self, settings: Settings) -> None:
        self.message = f'[bot] [{datetime.datetime.now().strftime("%H:%M:%S")}] '
        self.settings = settings
        intents = discord.Intents.default()
        intents.members = True
        super().__init__(
            command_prefix=self.settings.command_prefix,
            case_insensitive=True,
            intents=discord.Intents.all(),
            owner_id=618332297275375636,
            activity=discord.Activity(
                name="読み込み中…", type=discord.ActivityType.watching
            ),
            help_command=JapaneseHelpCommand(),
        )

    async def on_ready(self):
        print("-----------------------")
        print("ログインしました")
        print(f"ユーザー名:{self.user}")
        print(f"アクティビティ:{self.activity}")
        slash = SlashCommand(self, override_type=True)
        await self.change_presence(
            activity=discord.Activity(name="Ready", type=discord.ActivityType.watching),
        )


    async def on_message(self, message):
        if message.author.bot:
            return
        print(f"{self.message}{message.author.name}｜{message.content}")
        if message.channel.id == 848091616299450403:
          await message.add_reaction('👍')
          await message.add_reaction('👎')
        await self.process_commands(message)

    async def on_message_delete(self, message):
        pass

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            channel = guild.get_channel(guild.system_channel.id)
            link = await channel.create_invite(max_age = 300)
            to_send = f"{member.mention}ようこそ サーバーへ\nボットの管理者 <@618332297275375636> \n{link}"
            await guild.system_channel.send(to_send)
        channel = discord.utils.get(member.guild.text_channels, name="👥メンバー数")
        await channel.edit(name=f"👥メンバー数:{guild.member_count}")

    async def on_member_remove(self, member):
        guild = member.guild
        channel = guild.get_channel(636457818110820362)
        await channel.edit(name=f"👥メンバー数:{guild.member_count}")

    async def on_member_update(self, before: str, after: str):
        user = self.get_user(before.id)

    # reaction
    async def on_raw_reaction_add(self, payload):
        # print(self.message, payload)
        guild = self.get_guild(payload.guild_id)
        channel = guild.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        user = self.get_user(payload.member.id)
        if payload.member.bot:
            return
        if payload.emoji.name == "🔵":
            await message.remove_reaction(payload.emoji, user)
            text = ""
            for reaction in message.reactions:
                text += f"\n{reaction.emoji}｜{reaction.count - 1}"
            embed = message.embeds[0]
            embed.add_field(name="集計結果", value=text, inline=False)
            await message.edit(embed=embed)

    async def on_raw_reaction_remove(self, payload):
        pass

    async def on_voice_state_update(self, member, before, after):
    	if before.channel is None: 
    		if member.id != self.user.id:
    			if member.guild.voice_client is None:
    				await asyncio.sleep(0.5)
    				await after.channel.connect()
    	elif after.channel is None:
    		if member.id != self.user.id:
    			if member.guild.voice_client.channel is before.channel:
    				if len(member.guild.voice_client.channel.members) == 1:
    					await asyncio.sleep(0.5)
    					await member.guild.voice_client.disconnect() #切断

    async def on_typing(self, channel, user, when):
        pass

    async def on_error(self, event, *args, **kwargs):
        channel = self.get_channel(self.settings.debug_channel_id)
        embed = discord.Embed(title=":x: Event Error", colour=0xE74C3C)  # Red
        embed.add_field(name="Event", value=event)
        embed.description = "```py\n%s\n```" % traceback.format_exc()
        embed.timestamp = datetime.datetime.utcnow()
        await channel.send(embed=embed)
        print(traceback.format_exc())


class JapaneseHelpCommand(commands.DefaultHelpCommand):
    def __init__(self):
        super().__init__()
        self.commands_heading = "コマンド:"
        self.no_category = "その他"
        self.command_attrs["help"] = "コマンド一覧と簡単な説明を表示"

    def get_ending_note(self):
        return (
            "プレフィックス {0}\n各コマンドの説明: {0}help <コマンド名>\n"
            "各カテゴリの説明: {0}help <カテゴリ名>\n\n\ndiscord.py: {1}"
        ).format(".", discord.__version__)