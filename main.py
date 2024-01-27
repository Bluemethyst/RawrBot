import nextcord
import os
import dotenv
import colorama
from nextcord.ext import commands
from colorama import Fore as col

dotenv.load_dotenv()
colorama.init(autoreset=True)
TOKEN = os.getenv('BOT_TOKEN')
bot = commands.Bot()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


bot.run(TOKEN)
