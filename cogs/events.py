import nextcord
from nextcord.ext import commands


class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Logged in as {self.client.user.name} (ID: {self.client.user.id})")

    @commands.Cog.listener()
    async def on_message(self, message):
        print("{0.guild} - {0.author}: {0.content}".format(message))


def setup(client):
    client.add_cog(Events(client))
