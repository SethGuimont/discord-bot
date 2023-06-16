# bot.py
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import random

from constants import *

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1109948451577401347)
    await channel.send(f"Welcome to {member.guild.name}!")


@bot.event
async def on_message(message):
    if message.channel.id == 1109948451577401347:
        for i in BANNED_WORDS:  # Go through the list of bad words;
            if i in message.content:
                await message.delete()
                await message.channel.send(f"{message.author.mention} Don't use that word here!")
                bot.dispatch('profanity', message, i)
                return  # So that it doesn't try to delete the message again.
        await bot.process_commands(message)


@bot.event
async def on_profanity(message, word):
    channel = bot.get_channel(1112860393874923591)
    embed = discord.Embed(title="Profanity Alert!", description=f"{message.author.name} just said ||{word}||",
                          color=discord.Color.blurple())  # Let's make an embed!
    await channel.send(embed=embed)


@bot.command()
async def ping(ctx):
    await ctx.channel.send("pong")


# Retrieve information on a member, will return error if member does not exist.
# This will go into its own class later on
@bot.command()
async def info(ctx, *, member: discord.Member):
    """Tells you some info about the member."""
    msg = f'{member} joined on {member.joined_at} and has {len(member.roles)} roles.'
    await ctx.send(msg)


@info.error
async def info_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('I could not find that member...')


# Beginning of methods that are not part of Discords commands, but one's wrote by dev
@bot.command(pass_context=True)
async def pick(ctx):
    play_this = random.choice(MULTIPLAYER_MODES)
    await ctx.channel.send(play_this)


bot.run(TOKEN)
# test
