# 📱 botMobileOnline

A simple Discord bot that shows your presence as "Online on Mobile" (e.g., iOS) instead of the standard desktop status by overriding the WebSocket identify payload.

## 🚀 Features

- ✅ Spoofs presence as **Discord iOS**
- ✅ Custom status (e.g., DND, Watching, etc.)
- ✅ Supports command extensions via Cogs
- ✅ Based on [`discord.py`](https://discordpy.readthedocs.io/en/stable/)

## 🛠 Installation & Setup

### 1. Install Requirements

Requires Python 3.8 or later.

```bash
pip install -U discord.py
```

### 2. Configure the Bot

Open `exampleBot.py` and update the following:

```python
TOKEN = "your_token_here"
guildID = 123456789012345678  # Replace with your actual Discord server ID
```

### 3. Run the Bot

To run normally:

```bash
python exampleBot.py
```

To run with Cogs support:

```bash
python exampleBot.py
```

Make sure you have a `./cogs` directory and your cog files inside it.

## 📁 Project Structure

```
.
├── exampleBot.py     # Main bot script with modified identify
├── identify.py   # Custom identify() to fake mobile presence
└── cogs/         # Optional folder for command modules (extensions)
```

## 🧩 Example Cogs Setup (Optional)

You can extend the bot with modular commands using Cogs.

Example: `./cogs/exampleCog.py`

```python
from discord.ext import commands

class ExampleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")

def setup(bot):
    bot.add_cog(ExampleCog(bot))
```

## 🧠 Tips

- To customize the status message:

```python
activite = discord.Activity(type=discord.ActivityType.watching, name="Example")
```

- You can also set the bot’s prefix using:

```python
prefix = commands.when_mentioned_or(".")
```

## ⚠️ Disclaimer

- This project modifies the WebSocket `identify` payload to spoof platform presence.  
- Use responsibly. Do **not** violate [Discord's Terms of Service](https://discord.com/terms).  
- Intended for educational and personal use only.

## 📄 License

MIT License

---

Created with ❤️ by [Alan1455](https://github.com/Alan1455)
