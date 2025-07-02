import discord
from discord.ext import commands
from discord.ui import Button, View
from dotenv import load_dotenv
import os
import random

# Load .env
load_dotenv()
TOKEN = os.getenv("TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID"))

# Inisialisasi bot
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Ganti dengan ID stiker server kamu
STICKER_IDS = [
  1389838889564377188,
  1389839121773756416,
  1389841290795028551
]

@bot.event
async def on_ready():
    print(f"✅ Bot aktif sebagai {bot.user}")

@bot.event
async def on_member_join(member):
    # Ganti dengan channel welcome kamu (atau pakai system_channel)
    channel = member.guild.system_channel or discord.utils.get(member.guild.text_channels, name="general")
    if not channel:
        return

    button = Button(label="Klik untuk menyapa👋", style=discord.ButtonStyle.primary, custom_id="send_sticker")
    view = View()
    view.add_item(button)

    await channel.send(
        content=f"Halo {member.mention}, selamat datang di **{member.guild.name}**!",
        view=view
    )

@bot.event
async def on_interaction(interaction: discord.Interaction):
    if interaction.type == discord.InteractionType.component and interaction.data.get("custom_id") == "send_sticker":
        try:
            await interaction.response.send_message(sticker=discord.Object(STICKER_ID))
        except Exception as e:
            await interaction.response.send_message("❌ Gagal mengirim stiker. Pastikan bot punya izin!", ephemeral=True)

bot.run(TOKEN)
