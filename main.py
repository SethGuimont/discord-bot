# bot.py
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import random

MULTIPLAYER_MODES = [
    'Frontline', 'Team Deathmatch', 'Search and Destroy', 'Domination', 'Free-For-All',
    'Kill Confirmed', 'Hardpoint', 'Gunfight',
]

load_dotenv()
TOKEN = os.getenv('TOKEN')
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.event
async def on_message(message):
    if message.channel.name == 'general':
        await bot.process_commands(message)


@bot.command()
async def ping(ctx):
    await ctx.channel.send("pong")


@bot.command(pass_context=True)
async def pick(ctx):
    play_this = random.choice(MULTIPLAYER_MODES)
    await ctx.channel.send(play_this)


bot.run(TOKEN)
# test