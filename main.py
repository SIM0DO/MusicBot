import discord
from discord.ext import commands
import os

from Music import music_cog

bot = commands.Bot(command_prefix='.')
bot.remove_command('help')

bot.add_cog(music_cog(bot))

access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)
