import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
        print("Grimoire varification")
        print (bot.user.id)
