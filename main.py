import discord
from discord.ext import commands
import os

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot {bot.user} ONLINE!")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! Bot nyala ✅")

@bot.command()
async def setupvynn(ctx):
    await ctx.send("⏳ Lagi ngerapihin server...")
    guild = ctx.guild
    # Bikin kategori
    cat = await guild.create_category("VYNN SHOP")
    await guild.create_text_channel("order", category=cat)
    await guild.create_text_channel("testimoni", category=cat)
    await guild.create_text_channel("general", category=cat)
    await ctx.send("✅ Server Vynn udah dirapihin!")

@bot.command()
async def setup(ctx):
    await setupvynn(ctx)

TOKEN = os.getenv("TOKEN") or os.getenv("DISCORD_TOKEN") or "MASUKIN_TOKEN_LU_DISINI"
bot.run(TOKEN)
