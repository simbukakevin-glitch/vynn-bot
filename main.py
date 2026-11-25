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
@bot.command()
async def setupvynn(ctx):
    guild = ctx.guild
    # Hapus dulu biar gak dobel kalo ke-pencet 2x - optional
    struktur = {
        "---- ✦ ORDER ✦ ----": ["📓│redfinger-order-tutorial", "💰│bulk-order-code", "🎫│order-automatis-redfinger", "🎫│order-manual-redfinger", "🌐│order-via-website"],
        "---- ✦ REDFINGER SERVICE ✦ ----": ["📣│announcement-autoredeem", "📚│cara-setting-akun", "📱│panel-autoredeem-rf", "💬│tanya-reedem", "🟩│succes-log", "💵│refund-log"],
        "---- ✦ JUAL BELI ✦ ----": ["📝│rules-jubel", "🌳│jb-robux", "🌳│jb-growblox", "🌿│jb-gag", "🐬│jb-fishit"]
    }
    for nama_kategori, list_channel in struktur.items():
        kategori = discord.utils.get(guild.categories, name=nama_kategori)
        if not kategori:
            kategori = await guild.create_category(nama_kategori)
        for nama_channel in list_channel:
            channel_lama = discord.utils.get(guild.channels, name=nama_channel)
            if not channel_lama:
                await guild.create_text_channel(nama_channel, category=kategori)
    await ctx.send("✅ Server udah dirapihin kayak Ferz!")
@bot.command()
async def setupvynn(ctx):
    guild = ctx.guild
    everyone = guild.default_role

    # Channel yang dikunci, member cuma bisa baca
    dikunci = ["📣│announcement-autoredeem", "📚│cara-setting-akun", "📱│panel-autoredeem-rf", "🟩│succes-log", "💵│refund-log", "📝│rules-jubel", "📓│redfinger-order-tutorial"]

    struktur = {
        "---- ✦ ORDER ✦ ----": ["📓│redfinger-order-tutorial", "💰│bulk-order-code", "🎫│order-automatis-redfinger", "🎫│order-manual-redfinger", "🌐│order-via-website"],
        "---- ✦ REDFINGER SERVICE ✦ ----": ["📣│announcement-autoredeem", "📚│cara-setting-akun", "📱│panel-autoredeem-rf", "💬│tanya-reedem", "🟩│succes-log", "💵│refund-log"],
        "---- ✦ JUAL BELI ✦ ----": ["📝│rules-jubel", "🌳│jb-robux", "🌳│jb-growblox", "🌿│jb-gag", "🐬│jb-fishit"]
    }

    await ctx.send("⏳ Lagi ngerapihin server, tunggu 10 detik...")
    for nama_kategori, list_channel in struktur.items():
        kategori = discord.utils.get(guild.categories, name=nama_kategori)
        if not kategori:
            kategori = await guild.create_category(nama_kategori)
        for nama_channel in list_channel:
            channel_lama = discord.utils.get(guild.channels, name=nama_channel)
            if channel_lama:
                continue
            if nama_channel in dikunci:
                # Kunci: @everyone gak bisa kirim pesan
                overwrites = {everyone: discord.PermissionOverwrite(send_messages=False)}
                await guild.create_text_channel(nama_channel, category=kategori, overwrites=overwrites)
            else:
                await guild.create_text_channel(nama_channel, category=kategori)
    await ctx.send("✅ BERES! Server udah rapi kayak Ferz, channel log udah dikunci!")
