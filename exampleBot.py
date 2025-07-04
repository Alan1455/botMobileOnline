import discord
from discord.ext import commands
from discord.gateway import DiscordWebSocket

from identify import identify

TOKEN = "token"
# remember put the right token

DiscordWebSocket.identify = identify
# use the one which is mobile online


intents = discord.Intents.default()
intents.message_content = True
intents.members = True


status = discord.Status.dnd
prefix = commands.when_mentioned_or(".")
activite = discord.Activity(type = discord.ActivityType.watching, name = "Example")
guildID = 1234567890987654321


class Example(commands.Bot):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(command_prefix = prefix, activity = activite, status = status, intents = intents)

    async def setup_hook(self):
        self.tree.copy_global_to(guild = discord.Object(id = guildID))
        await self.tree.sync()

bot = Example(intents = intents)


@bot.event
async def on_ready():
    await bot.wait_until_ready()
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print(f"Supporting {str(len(bot.guilds))} Servers")

# bot.remove_command("help")
# if you wanna remake a new one with nice visual


bot.run(TOKEN)

# also if you need to use cogs:
"""
import asyncio, os

async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")
            print(f'Loaded {filename[:-3]}.')
    print('Done.')

async def main():
    async with bot:
        await load_extensions()
        await bot.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
"""

