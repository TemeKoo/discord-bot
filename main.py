import os

import discord
from dotenv import load_dotenv


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

intents = discord.Intents.default()
client = MyClient(intents=intents)

load_dotenv()
TOKEN = os.getenv("TOKEN")

client.run(TOKEN)
