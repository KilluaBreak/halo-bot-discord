import discord
from discord.ext import commands
import os
import random

# Ambil token dari environment variable (Railway)
TOKEN = os.environ.get("DISCORD_TOKEN")

# Aktifkan intents penting
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# Inisialisasi bot
bot = commands.Bot(command_prefix="!", intents=intents)

# Tombol custom welcome
class WelcomeView(discord.ui.View):
    def __init__(self, emoji: discord.Emoji | str):
        super().__init__(timeout=None)
        self.add_item(discord.ui.Button(
            label="Sapa!",
            style=discord.ButtonStyle.primary,
            emoji=emoji,
            custom_id="welcome_button"
        ))

# Bot aktif
@bot.event
async def on_ready():
    print(f"✅ Bot aktif sebagai {bot.user} (ID: {bot.user.id})")

# Saat member baru join
@bot.event
async def on_member_join(member):
    # Cari channel dengan nama tepat "💬┃main・hall"
    channel = discord.utils.get(member.guild.text_channels, name="💬┃main・hall")
    if not channel:
        print("⚠️ Channel 💬┃main・hall tidak ditemukan.")
        return

    # Ambil list emoji berdasarkan ID
    emoji_ids = [1390327274158686280, 1390327311915548712]
    selected_id = random.choice(emoji_ids)
    selected_emoji = discord.utils.get(member.guild.emojis, id=selected_id)

    # Fallback kalau emoji tidak ditemukan
    if selected_emoji is None:
        selected_emoji = "👋"

    # Buat embed welcome
    embed = discord.Embed(
        title="👋 Selamat Datang!",
        description=f"Welcome {member.mention}! Ayo sapa dia.",
        color=discord.Color.blurple()
    )

    await channel.send(embed=embed, view=WelcomeView(selected_emoji))

# Jalankan bot
bot.run(TOKEN)
