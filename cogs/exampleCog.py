from discord.ext import commands

class ExampleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")

def setup(bot):
    # bot.add_cog(ExampleCog(bot))
    # ^ add this when using cogs method
