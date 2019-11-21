import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os #!

discord.opus.load_opus() #!

client = discord.Client()
bot = commands.Bot(command_prefix = "p")

@bot.listen()
async def on_ready():
    print("bot on")
    
@bot.command()
async def ing(ctx, *args):
    await ctx.author.voice.channel.connect()




    
TOKEN = os.environ['BOT_TOKEN']
bot.run(TOKEN)
