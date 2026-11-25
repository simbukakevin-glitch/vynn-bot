import discord
from discord.ext import commands
import os
import json
import asyncio

TOKEN = os.getenv("TOKEN") or os.getenv("DISCORD_TOKEN") or os.getenv("BOT_TOKEN")
DATA_FILE = "data.json"

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"stock": {}}
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except:
        return {"stock": {}}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

@bot.event
async def on_ready():
    print(f"Bot {bot.user} ONLINE!")
    print(f"Login sebagai {bot.user}")

@bot.command(name="panelvynn")
async def panelvynn(ctx):
    embed = discord.Embed(
        title="🛒 VYNN SHOP - PANEL ORDER",
        description="Selamat datang di Vynn Shop!\n\nPilih produk di bawah untuk order.\n\n**Cara Order:**\n1. Klik tombol produk\n2. Isi format order\n3. Bayar & tunggu proses",
        color=0x2b2d31
    )
    embed.add_field(name="📦 Produk Tersedia", value="• Netflix\n• Spotify\n• CapCut Pro\n• Canva Pro\n• Alight Motion", inline=False)
    embed.add_field(name="💳 Payment", value="DANA / OVO / GOPAY / QRIS", inline=False)
    embed.set_footer(text="Vynn Shop • Fast & Trusted")
    await ctx.send(embed=embed)

@bot.command(name="replace")
async def replace(ctx):
    await ctx.send("Perintah replace siap! Ketik format yang mau diganti.")

@bot.command()
async def setupvynn(ctx):
    await ctx.send("⏳ Lagi ngerapihin server, tunggu bentar...")
    guild = ctx.guild
    # Hapus semua channel lama
    for channel in list(guild.channels):
        try:
            await channel.delete()
        except:
            pass
    await asyncio.sleep(1)
    # Struktur baru
    struktur = {
        "🔥・VYNN SHOP": ["👋・welcome", "📜・rules", "📢・announcement"],
        "ℹ️・INFORMASI": ["📦・stock", "⭐・testimoni", "💸・payment"],
        "🛒・TRANSAKSI": ["🛍️・order", "📝・chat", "🎫・ticket"],
        "💬・SUPPORT": ["❓・help", "📩・complaint"],
    }
    for cat_name, channels in struktur.items():
        cat = await guild.create_category(cat_name)
        for ch_name in channels:
            await guild.create_text_channel(ch_name, category=cat)
    await ctx.send("✅ Server udah dirapihin sama Vynn!")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    print(f"Error: {error}")

bot.run(TOKEN)
