import discord
from discord.ext import commands
import os

# Ambil token dari variabel lingkungan (Railway)
TOKEN = os.environ.get("DISCORD_TOKEN")

# Intents yang dibutuhkan
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# View berisi tombol emoji
class WelcomeView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="👋 Kirim Emoji", style=discord.ButtonStyle.primary)
    async def send_emoji(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("👋", ephemeral=False)

# Saat bot siap digunakan
@bot.event
async def on_ready():
    print(f"✅ Bot aktif sebagai {bot.user} (ID: {bot.user.id})")

# Saat ada member baru yang join server
@bot.event
async def on_member_join(member):
    # Cari channel dengan nama 'general'
    for channel in member.guild.text_channels:
        if channel.name == "general":
            embed = discord.Embed(
                title="👋 Selamat Datang!",
                description=f"Welcome {member.mention}! Ayo sapa dia dengan klik tombol di bawah.",
                color=discord.Color.blurple()
            )
            await channel.send(embed=embed, view=WelcomeView())
            break  # Hanya kirim ke satu channel 'general'

bot.run(TOKEN)
