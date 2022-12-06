import asyncio
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
from aiohttp import ClientSession


class TemeBot(commands.Bot):
    def __init__(self, *args, initial_extensions: "list[str]", testing_guild_id: int = None, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial_extensions = initial_extensions
        self.testing_guild_id = testing_guild_id

    async def setup_hook(self) -> None:
        print("Loading extensions")
        for extension in self.initial_extensions:
            await self.load_extension(extension)

        if self.testing_guild_id:
            print("Deploying commands to test guild")
            guild = discord.Object(self.testing_guild_id)
            self.tree.copy_global_to(guild = guild)
            await self.tree.sync(guild = guild)


async def main(test: bool =False):
    load_dotenv()

    intents = discord.Intents.default()

    async with ClientSession() as my_client:
        exts = ["command_test", "voice_commands"]
        testing_guild_id = os.getenv("TEST_SERVER") if test else None
        async with TemeBot(commands.when_mentioned, web_client=my_client, initial_extensions=exts, testing_guild_id=testing_guild_id, intents=intents) as bot:
            await bot.start(os.getenv('TOKEN', ''))


asyncio.run(main(test=True))