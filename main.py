import discord
from discord.ext import commands
import os

from Music import music_cog

bot = commands.Bot(command_prefix='.')

bot.remove_command('help')

bot.add_cog(music_cog(bot))

bot.run("OTg5MDQ4NzI1Nzk4MjU2NjQz.G835TS.j972Bo43pjITxbzy7LHPTJJtPvHC5bvXwYiMko")
