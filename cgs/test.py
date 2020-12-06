import discord
import SchoolBoy
import config

from discord.ext import commands

class test(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	@commands.has_permissions(administrator=True)
	async def test(self, ctx):
		print("Работает")

def setup(bot):
	bot.add_cog(test(bot))