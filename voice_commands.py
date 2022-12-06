import discord
import os
import youtube_handler as yt
from discord import app_commands
from discord.ext import commands

class Voice_Cog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name = "join")
    async def join_voice_channel(self, interaction: discord.Interaction) -> None:
        """ Joins the voice channel you are in """
        channel = interaction.user.voice.channel
        if channel:
            print(f"Connecting to voice channel of {interaction.user}")
            await channel.connect()
            await interaction.response.send_message("Connected!")
    
    @app_commands.command(name = "leave")
    async def leave_voice_channel(self, interaction: discord.Interaction) -> None:
        """ Leaves voice channel """
        user_guild = interaction.user.guild
        voice_client = None
        for voice_client in self.bot.voice_clients:
            if voice_client.guild == user_guild:
                break
        else:
            await interaction.response.send_message("Not connected to voice!")
            return
        await voice_client.disconnect()
        print(f"Left voice channel in {user_guild}")
        await interaction.response.send_message("Left voice!")

    @app_commands.command(name = "play")
    async def play_from_url(self, interaction: discord.Interaction, url: str) -> None:
        """ Plays a youtube url in voice """
        await interaction.response.send_message("Downloading...")
        yt.download_from_url(url)
        voice_client = await self.find_user_voice_channel(interaction)
        await voice_client.play(discord.FFmpegOpusAudio(os.path.join("audio", "audio.mp3")))

    @app_commands.command(name = "test_play")
    async def test_play(self, interaction: discord.Interaction) -> None:
        """ Plays the test audio """
        await interaction.response.send_message("Trying to play")
        voice_client = await self.find_user_voice_channel(interaction)
        await voice_client.play(discord.FFmpegOpusAudio(os.path.join("audio", "audio.mp3")))

    async def find_user_voice_channel(self, interaction: discord.Interaction) -> discord.VoiceClient:
        user_guild = interaction.user.guild
        for voice_client in self.bot.voice_clients:
            if isinstance(voice_client, discord.VoiceClient) and voice_client.guild == user_guild:
                return voice_client
        return None

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Voice_Cog(bot))
    print("Voice commands loaded")

