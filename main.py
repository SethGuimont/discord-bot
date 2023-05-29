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
async def on_message_join(member):
    channel = bot.get_channel(1109948451577401347)
    embed = discord.Embed(title=f"Welcome {member.name}",
                          description=f"Thanks for joining {member.guild.name}!")  # F-Strings!
    embed.set_thumbnail(url=member.avatar_url)  # Set the embed's thumbnail to the member's avatar image!
    await channel.send(embed=embed)


@bot.event
async def on_message(message):
    if message.channel.name == 'general':
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


@bot.command(pass_context=True)
async def pick(ctx):
    play_this = random.choice(MULTIPLAYER_MODES)
    await ctx.channel.send(play_this)


bot.run(TOKEN)
# test
