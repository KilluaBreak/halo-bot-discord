import discord
from discord.ext import commands
import random
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")
WELCOME_CHANNEL_ID = int(os.getenv("WELCOME_CHANNEL_ID"))

intents = discord.Intents.default()
intents.members = True  # Penting untuk on_member_join
bot = commands.Bot(command_prefix="!", intents=intents)

# ID stiker-stiker kamu
STICKER_IDS = [
    1389838889564377188,
    1389841290795028551,
    1389839121773756416
]

# Tombol untuk mengirim stiker
class StickerButtonView(discord.ui.View):
    @discord.ui.button(label="Kirim Stiker 🎉", style=discord.ButtonStyle.primary)
    async def send_sticker(self, interaction: discord.Interaction, button: discord.ui.Button):
        sticker_id = random.choice(STICKER_IDS)
        try:
            await interaction.channel.send(sticker=discord.Object(id=sticker_id))
            await interaction.response.send_message("✅ Stiker dikirim!", ephemeral=True)
        except discord.HTTPException:
            await interaction.response.send_message("❌ Gagal kirim stiker.", ephemeral=True)

# Saat ada member baru
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(WELCOME_CHANNEL_ID)
    if channel:
        embed = discord.Embed(
            title="Selamat Datang!",
            description="Klik tombol di bawah untuk mengirim stiker 🎭",
            color=discord.Color.blurple()
        )
        await channel.send(embed=embed, view=StickerButtonView())

@bot.event
async def on_ready():
    print(f"✅ Bot aktif sebagai {bot.user}")

bot.run(TOKEN)
