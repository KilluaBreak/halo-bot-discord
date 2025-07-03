import discord
from discord.ext import commands
import os

TOKEN = os.environ.get("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# View dengan tombol
class WelcomeView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="👋 Kirim Emoji", style=discord.ButtonStyle.primary)
    async def send_emoji(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("👋", ephemeral=False)

# Bot siap digunakan
@bot.event
async def on_ready():
    print(f"✅ Bot aktif sebagai {bot.user} (ID: {bot.user.id})")

# Saat ada member join
@bot.event
async def on_member_join(member):
    # Ganti 'general' ke nama channel kamu
    channel = discord.utils.get(member.guild.text_channels, name="general")
    if channel:
        embed = discord.Embed(
            title="👋 Selamat Datang!",
            description=f"Welcome {member.mention}! Ayo sapa dia dengan klik tombol di bawah.",
            color=discord.Color.blurple()
        )
        await channel.send(embed=embed, view=WelcomeView())

bot.run(TOKEN)
