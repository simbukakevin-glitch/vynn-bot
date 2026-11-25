import discord
from discord.ext import commands
import os
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents,help_command=None)
@bot.event
async def on_ready():
    print(f"Bot {bot.user} ONLINE!")
    await bot.change_presence(activity=discord.Game(name="Vynn SHOP | !help"))
@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency*1000)}ms - Vynn SHOP Online!")
@bot.command()
async def shop(ctx):
    embed = discord.Embed(title="🛒 VYNN SHOP", description="Selamat datang di Vynn SHOP!", color=0x00ff00)
    await ctx.send(embed=embed)
@bot.command()
async def help(ctx):
    await ctx.send("Perintah: !ping - !shop - !help")
TOKEN = os.getenv("TOKEN")
bot.run(TOKEN)
