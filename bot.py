import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time

client = discord.Client()
bot = commands.Bot(command_prefix = "z_")

@bot.listen()
async def on_ready():
    pass
    
@bot.command()
async def nothing(ctx, *args):
    pass

TOKEN = os.environ.get('BOT_TOKEN')
bot.run(TOKEN)
