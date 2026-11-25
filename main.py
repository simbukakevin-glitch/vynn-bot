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
# === PANEL VYNN SHOP ===
@bot.command(name='panelvynn')
@commands.has_permissions(administrator=True)
async def panelvynn(ctx):
    embed = discord.Embed(title='Vynn SHOP - BOT REDEEM REDFINGER', description='**Status Bot: 🟢 Online**\n**Queue: 0/50**\n**Status: 🔄 Auto Processing**\n\n**❕ Login Terlebih Dahulu Di Bawah Ini ⬇️**\nGunakan `/login` untuk memulai layanan redeem dan layanan lainnya.\n\n**🛒 Service**\n**Redeem Code - Rp 0 (Gratis)**\n**Replace - Rp 0 (Gratis)**\n**Renew Cloud - Rp 0 (Gratis)**\n**Upgrade Device - Rp 0 (Gratis)**', color=0x2b2d31)
    embed.set_footer(text='Vynn SHOP • 2026')
    view = discord.ui.View(timeout=None)
    view.add_item(discord.ui.Button(label='Klik menuju Ticket', style=discord.ButtonStyle.primary, emoji='🎫', custom_id='ferzz_ticket'))
    await ctx.send(embed=embed, view=view)
    await ctx.message.delete()

@bot.command(name='replace')
async def replace_cmd(ctx):
    await ctx.send(f'{ctx.author.mention} silahkan isi format replace:\n**Email:** \n**Device:** \n**Region:** \n**Alasan:**')

bot.run(TOKEN)
