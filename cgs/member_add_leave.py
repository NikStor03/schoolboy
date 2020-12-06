import discord
import SchoolBoy
import config

from discord.ext import commands

class member_add_leave(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_member_join(self, member):
		if member.bot:
			return
		else:
			channel = self.bot.get_channel(785129670559531079) # получаем объект канала
			role = discord.utils.get(member.guild.roles, id=783669858838773781)
			await member.add_roles(role)
			await channel.send(f":partying_face: **Користувач приєднався до нас {member.mention}, так давайте привітаємо його!!!**")

def setup(bot):
	bot.add_cog(member_add_leave(bot))