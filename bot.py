import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# Load all cogs
COGS = [
    "cogs.utils",
    # "cogs.moderation",
    # "cogs.fun",
    # "cogs.utility",
    # "cogs.music",
    # "cogs.ai"
]

# @bot.event
# async def on_ready():
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    
    channel_id = int(CHANNEL_ID)
    print(channel_id)
    channel = bot.get_channel(channel_id)
    
    if channel:
        await channel.send("Ayo I'm online now! 🔥 Wassup everyone!")
    else:
        print("⚠️ Channel not found. Check the ID or bot permissions.")

    for cog in COGS:
        await bot.load_extension(cog)

bot.run(TOKEN)
