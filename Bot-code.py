import discord
import time
import random
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
async def online(ctx):
    await ctx.send('The bot is online and working!')

@bot.command()
async def helpme(ctx):
    await ctx.send('''
Help is here! Heres a list of commands below:
1. /online 
2. /helpme
3. /coinflip #flips a coin and gives a heads or tails response to decide things                  
4. /rockpaperscissors #play rock, paper, scissors - it's not fully done yet
5. /
''')

@bot.command()
async def coinflip(ctx):
    coin = random.randint(1, 2)
    if coin == 1:
        await ctx.send("Tails")
    if coin == 2:
        await ctx.send("Heads")


@bot.command()
async def rockpaperscissors(ctx):
    rock = random.randint(1, 2, 3)
    if rock == 1:
        await ctx.send("Rock")

    if rock == 2:
        await ctx.send("Paper")

    if rock == 3:
        await ctx.send("Scissors")

bot.run('123')
