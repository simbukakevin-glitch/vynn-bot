import discord
from discord.ext import commands
import os

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f"Bot {bot.user} ONLINE!")

# INI FIX NYA: Bot baca chat langsung, gak ke-block lagi
@bot.event
async def on_message(message):
    if message.author.bot:
        return

    msg = message.content.strip().lower()

    # Terima !setup, !setupvynn, !ping - semua jalan
    if "!setup" in msg or "!setupvynn" in msg or "!ping" in msg:
        if msg == "!ping":
            await message.channel.send("Pong! Bot nyala ✅")
            return

        # SETUP MULAI
        await message.channel.send("⏳ Lagi ngerapihin server Vynn...")
        guild = message.guild

        try:
            # 1. Bikin Role
            role_member = discord.utils.get(guild.roles, name="Vynn Member")
            if not role_member:
                role_member = await guild.create_role(name="Vynn Member", colour=discord.Colour.blue())
            
            role_admin = discord.utils.get(guild.roles, name="Vynn Admin")
            if not role_admin:
                role_admin = await guild.create_role(name="Vynn Admin", colour=discord.Colour.red())

            # 2. Bikin Kategori
            category = discord.utils.get(guild.categories, name="VYNN SHOP")
            if not category:
                category = await guild.create_category("VYNN SHOP")

            # 3. Bikin Channel
            channels = ["vynn-shop", "order", "testimoni", "stock"]
            for ch_name in channels:
                if not discord.utils.get(guild.channels, name=ch_name):
                    await guild.create_text_channel(ch_name, category=category)

            await message.channel.send("✅ **BERES!** Server udah di-setup Vynn!\nCek kategori `VYNN SHOP` di atas!")
        except Exception as e:
            await message.channel.send(f"❌ Error: {e}\nCoba kasih bot role paling atas / Administrator dulu.")
        return

    await bot.process_commands(message)

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! Bot nyala ✅")

TOKEN = os.getenv("TOKEN") or os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
