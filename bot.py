import os
import threading
import discord
from discord.ext import commands
from dotenv import load_dotenv
from flask import Flask, jsonify

load_dotenv()
TOKEN = os.getenv("TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
PORT = int(os.environ.get("PORT", 5000))

# Flask web server
app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Bot is alive!"})

def run_flask():
    app.run(host="0.0.0.0", port=PORT)

# Start Flask in a background thread
threading.Thread(target=run_flask).start()

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
    channel = bot.get_channel(channel_id)
    
    if channel:
        await channel.send("Ayo I'm online now! 🔥 Wassup everyone!")
        await channel.send("use !ping, !userinfo, !serverinfo")
    else:
        print("⚠️ Channel not found. Check the ID or bot permissions.")

    for cog in COGS:
        await bot.load_extension(cog)

bot.run(TOKEN)
