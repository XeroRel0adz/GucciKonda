import discord
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

bot.command90
async def someone(ctx):
    await ctx.send('')

bot.run('123')
