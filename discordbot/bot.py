import discord
import sys
import platform
from flask import Flask, request
import json
from PIL import Image, ImageDraw
import datetime
import requests
import logging
from . import music

from discord.ext import commands

json_open_confing = open('confing.json', 'r')
confing = json.load(json_open_confing)
json_open_message = open('message.json', 'r')
message_template = json.load(json_open_message)


formatter = '%(levelname)s : %(asctime)s : %(message)s'
logging.basicConfig(
    filename='logger.log', level=logging.INFO, format=formatter)
prefix = '.'

#discord
print("ログインしています……\n")

class Mybot(commands.Bot):
  def __init__(self) -> None:
    super().__init__(
      command_prefix=".",
      owner_id=618332297275375636,
      activity=discord.Activity(name=confing["activity"], type=discord.ActivityType.watching),
      help_command=JapaneseHelpCommand()
      )
  async def on_ready(self):
    print("-----------------------")
    print('ログインしました')
    print(f'ユーザー名:{self.user}')
    print(f'アクティビティ:{confing["activity"]}')
    print(f'python {platform.python_version()}')
    print("discord.py " + discord.__version__)
    print(f'\n')
    

class JapaneseHelpCommand(commands.DefaultHelpCommand):
    def __init__(self):
        super().__init__()
        self.commands_heading = "コマンド:"
        self.no_category = "その他"
        self.command_attrs["help"] = "コマンド一覧と簡単な説明を表示"

    def get_ending_note(self):
        return (f"プレフィックス {prefix}\n各コマンドの説明: {prefix}help <コマンド名>\n"
                f"各カテゴリの説明: {prefix}help <カテゴリ名>\n")


def setup():
  client = Mybot()
  client.run('NzQzNzc2ODI1MTMzNjI5NTQw.XzZmJQ.4Cer4_pQghZHCtDwqHjzu8nPrec')