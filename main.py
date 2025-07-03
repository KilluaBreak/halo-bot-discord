import discord
from discord.ext import commands
import os
import random

TOKEN = os.environ.get("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# List teks yang akan dikirim (bukan emoji object)
TEXT_RESPONSES = [
    "<:dengakan_notifnya:1390327274158686280>",
    "<:halo_bang:1390327311915548712>"
]

# Tombol interaktif
class WelcomeView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Sapa!", style=discord.ButtonStyle.primary, custom_id="welcome_button")
    async def greet_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        chosen_text = random.choice(TEXT_RESPONSES)

        try:
            await interaction.channel.send(f"{interaction.user.mention}{chosen_text}")
            await interaction.response.send_message("✅ Pesan berhasil dikirim!", ephemeral=True)
        except Exception as e:
            print(f"❌ ERROR saat kirim: {e}")
            await interaction.response.send_message(f"❌ Gagal kirim teks: {e}", ephemeral=True)

# Bot siap
@bot.event
async def on_ready():
    print(f"✅ Bot aktif sebagai {bot.user} (ID: {bot.user.id})")

# Saat member baru join
@bot.event
async def on_member_join(member):
    # Cari channel dengan nama tepat
    channel = discord.utils.get(member.guild.text_channels, name="💬┃main・hall")
    if not channel:
        print("⚠️ Channel 💬┃main・hall tidak ditemukan.")
        return

    embed = discord.Embed(
        title="👋 Selamat Datang!",
        description=f"Welcome {member.mention}! Ayo sapa dia",
        color=discord.Color.blurple()
    )

    view = WelcomeView()
    await channel.send(embed=embed, view=view)

# Jalankan bot
bot.run(TOKEN)
