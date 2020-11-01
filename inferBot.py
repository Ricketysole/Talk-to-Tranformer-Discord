import discord
import text_generation as generate
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix = '!')

@bot.event
async def on_ready():
	print("up")

@bot.command()
async def infer(ctx, param):
	await ctx.send(generate.generate_text(param))

bot.run("NzcxNzY0NDk4NTc0OTk5NjMy.X5w3sw.vugl3K6oIG7myQMrI-gkiReYa7s")
