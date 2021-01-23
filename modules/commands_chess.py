import requests
from discord.ext import commands
import time
import json
import discord
import chess

board = None

class Commands_chess(commands.Cog, name='チェス'):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def start(self ,ctx):
		global board
		board = chess.Board()
		await ctx.send("ボードを作成しました")
		await ctx.send("```" + str(board) + "```")

	@commands.command()
	async def move(self, ctx, movePos):
		global board
		if board == None:
			await ctx.send("ボードが作成されていません")
			return
		try:
			board.push_san(movePos)
			await ctx.send("```" + str(board) + "```")
		except:
			await ctx.send(movePos + "は有効な値ではありません")
			a = ""
			for i in board.legal_moves:
				a += str(i) + ","
			await ctx.send("> " + a)
		if board.is_game_over():
			await ctx.send("game over")
			board = None
