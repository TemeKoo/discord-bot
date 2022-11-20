import discord
from discord import app_commands
from discord.ext import commands

class Test_Cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name = "test")
    async def test_command(self, interaction: discord.Interaction) -> None:
        """ /test command """
        await interaction.response.send_message(f"fuck you")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Test_Cog(bot))
    print("Test loaded")
