import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import random

load_dotenv()

TOKEN = os.getenv("TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID"))
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Daftar ID stiker dari server kamu
STICKER_IDS = [
    123456789012345678,  # Ganti dengan ID stiker asli
    987654321098765432
]

# Tombol View
class HaloButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Kirim Stiker 🎉", style=discord.ButtonStyle.primary)
    async def send_sticker(self, interaction: discord.Interaction, button: discord.ui.Button):
        sticker_id = random.choice(STICKER_IDS)
        await interaction.channel.send(sticker=discord.Object(id=sticker_id))
        await interaction.response.defer()

@bot.event
async def on_ready():
    print(f"✅ Bot aktif sebagai {bot.user}")

    guild = bot.get_guild(GUILD_ID)
    channel = guild.get_channel(CHANNEL_ID)

    if channel:
        embed = discord.Embed(
            title="Selamat Datang!",
            description="Klik tombol di bawah untuk mengirim stiker 🎭",
            color=discord.Color.blurple()
        )
        await channel.send(embed=embed, view=HaloButton())
    else:
        print("❌ Channel tidak ditemukan!")

bot.run(TOKEN)
