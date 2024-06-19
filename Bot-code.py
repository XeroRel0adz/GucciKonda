import discord
import time
from discord import app_commands
from discord.ext import commands


intents = discord.Intents.all()
intents.messages = True
intents.guilds = True


bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('-----')

@bot.command()
async def hello(ctx):
    await ctx.send('hello')

@bot.command()
async def ping(ctx):
    await ctx.send('@everyone')

@bot.command()
async def someone(ctx):
    await ctx.send('your mother')

@bot.command()
async def simplydont(ctx):
    await ctx.send('@everyone')

@bot.command()
async def test(ctx):
    await ctx.send('test complete')

bot.run('123')
