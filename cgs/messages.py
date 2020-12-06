import discord
import SchoolBoy
import config

from discord.ext import commands

class messages(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener("on_message")
	async def on_message(self, message):
		
		if "Direct" == str(message.channel).split()[0] and message.content.startswith("ПІБ"):
			guild = self.bot.get_guild(id=783286908910174219)
			member = discord.utils.get(guild.members, id=message.author.id)
			try:
				nick = f"{message.content.split()[1]} {message.content.split()[2]} {message.content.split()[3]}"
			except:
				try:
					nick = f"{message.content.split()[1]} {message.content.split()[2]}"
				except:
					try:
						nick = f"{message.content.split()[1]}"
					except:
						emb = discord.Embed(title="Помилка :exclamation:",
							description="Ви ввели не вiрне iм'я\nСпробуйте знову",
							color=0x1400ff)
						emb.set_footer(text="Цей бот є зараз на бета тестуванні, якщо помітите будь-якої неполадки, напишіть про це творцю NikStor")
						await member.send(embed=emb)
						return
			for guild_member in guild.members:
				if guild_member.nick == nick:
					emb = discord.Embed(title="Помилка :exclamation:",
						description="Я бачу у гільдії вже є така людина\nСпробуйте знову",
						color=0x1400ff)
					emb.set_footer(text="Цей бот є зараз на бета тестуванні, якщо помітите будь-якої неполадки, напишіть про це творцю NikStor")
					await member.send(embed=emb)
					return
			await member.edit(nick=nick)
			emb = discord.Embed(title="Кiнець",
				description="Вiтаю, ти завершив регестрацiю:yum:\n"
				"Тепер ти можеш пiти й прочитати правила у чатi #правила-учнiв\n\n"
				"||Якщо ти зробив помилку в написаннi свого iменi\nНапиши знову `ПІБ [призвище] [ім'я]`||",
				color=0x1400ff)
			emb.set_footer(text="Цей бот є зараз на бета тестуванні, якщо помітите будь-якої неполадки, напишіть про це творцю NikStor")
			await member.send(embed=emb)

def setup(bot):
	bot.add_cog(messages(bot))