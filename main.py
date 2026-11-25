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
import discord
from discord.ext import commands
import os

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

REGIONS = ["Hongkong [HK_HK_01]", "Hongkong 2 [HKXG_IDC_01]", "Singapore [SG_SG_01]", "Thailand [TH_IDC_01]", "Taiwan [TW_IDC_01]", "United States [US_IDC_01]"]

class RegionView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(RegionSelect())

class RegionSelect(discord.ui.Select):
    def __init__(self):
        options = [discord.SelectOption(label=r) for r in REGIONS]
        super().__init__(placeholder="Pilih Region Server Tujuan", options=options, custom_id="region")
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"✅ Region dipilih: **{self.values[0]}**\nLangkah 2: Pilih Android (10/12)\n\nKetik di ticket: `!order {self.values[0]}`", ephemeral=True)

class TicketView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.button(label="🎫 Klik menuju Ticket", style=discord.ButtonStyle.secondary)
    async def ticket(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        overwrites = {guild.default_role: discord.PermissionOverwrite(read_messages=False), interaction.user: discord.PermissionOverwrite(read_messages=True, send_messages=True)}
        ch = await guild.create_text_channel(f"ticket-{interaction.user.name}", overwrites=overwrites)
        await interaction.response.send_message(f"✅ Ticket dibuat: {ch.mention}", ephemeral=True)
        await ch.send(f"👋 {interaction.user.mention} Mau order apa? Tulis: Redeem / Renew / Upgrade / Replace + Region + Android")

class MainView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.button(label="🎮 Redeem Code", style=discord.ButtonStyle.primary)
    async def redeem(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("✅ **Redeem Code [ Device Baru ]**\nHarga: **Rp 0**\nSilahkan /login dulu, lalu pilih region.", ephemeral=True, view=RegionView())
    @discord.ui.button(label="♻️ Renew Cloud", style=discord.ButtonStyle.success)
    async def renew(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("♻️ **Renew Cloud [ Perpanjang Device ]**\nHarga: **Rp 0**\nPilih region tujuan:", ephemeral=True, view=RegionView())
    @discord.ui.button(label="⬆️ Upgrade Device", style=discord.ButtonStyle.secondary)
    async def upgrade(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("⬆️ **Upgrade Device**\nHarga: **Rp 0**\nPilih region:", ephemeral=True, view=RegionView())
    @discord.ui.button(label="🔄 Replace Cloud", style=discord.ButtonStyle.secondary)
    async def replace(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(title="Replace Cloud Server", description="Pindahkan device Anda ke region server yang berbeda.\n\n**Harga: Rp 0**\n\n**Catatan:**\n• Setelah login, pilih device dari dropdown\n• Waktu aktif device tetap sama\n\n**Langkah 1:** pilih **region** tujuan.\n**Langkah 2:** pilih **Android (10/12)**.\n\nPilih region tujuan dari dropdown di bawah.", color=0x2b2d31)
        await interaction.response.send_message(embed=embed, ephemeral=True, view=RegionView())

@bot.event
async def on_ready():
    print(f"Bot {bot.user} ONLINE!")

@bot.command()
async def ping(ctx): await ctx.send(f"Pong! {round(bot.latency*1000)}ms - Vynn SHOP Online!")
@bot.command()
async def help(ctx): await ctx.send("Perintah: !ping - !shop - !panelrf - !help")

@bot.command()
async def panelrf(ctx):
    embed = discord.Embed(title="⚙️ REDFINGER SERVICE", description="Ketik `/login` untuk daftar\nLalu Tekan Joki untuk memulai layanan.\n\n🟢 **STATUS BOT**\nSystem: Online\nQueue: 0/50\n\n📋 **SERVICE COST**\n— Redeem : Rp 0 (Gratis)\n— Replace : Rp 0 (Gratis)\n— Renew : Rp 0 (Gratis)\n— Upgrade : Rp 0 (Gratis)\n\n🌍 **Support Region**\nHongkong [ HK_HK_01 ]\nHongkong 2 [ HKXG_IDC_01 ]\nSingapore [ SG_SG_01 ]\nThailand [ TH_IDC_01 ]\nTaiwan [ TW_IDC_01 ]\nUnited States [ US_IDC_01 ]\n\n📱 **Android System**\nAndroid 8, 10, 12, 15\n( tergantung region )\n\n🔵 **BACA SEBELUM MEMAKAI LAYANAN**\n• Settingan Akun Mengikuti\n• #cara-setting-akun\n• Disarankan Ganti Password setelah Menggunakan Layanan", color=0x2b2d31)
    embed.set_footer(text="Vynn | Powered by Vynn • Replace")
    await ctx.send(embed=embed)

    embed2 = discord.Embed(title="🛠️ Pilih Layanan", description="Silakan pilih **layanan** yang ingin Anda gunakan:\n\n✅ — **Redeem Code [ Device Baru ]**\n🕐 — **Renew Cloud [ Perpanjang Device ]**\n🚀 — **Upgrade Device**\n🔄 — **Replace Cloud [ Ganti Cloud ]**\n\nPilih salah satu tombol di bawah.\n\nPastikan saldo Anda cukup sebelum menggunakan layanan berbayar.\n\nBot Redeem RedFinger | Fast Process", color=0x2b2d31)
    embed2.set_footer(text="Vynn | Powered by Vynn • Replace")
    await ctx.send(embed=embed2, view=MainView())

@bot.command()
async def shop(ctx): await panelrf(ctx)

TOKEN = os.getenv("TOKEN") or os.getenv("DISCORD_TOKEN") or "MASUKIN_TOKEN_LU_DISINI"
bot.run(TOKEN)
