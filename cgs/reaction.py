import discord
import SchoolBoy
import config

from discord.ext import commands

class member_add_leave(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_raw_reaction_add(self, payload):
		channel = self.bot.get_channel(payload.channel_id) # получаем объект канала
		message = await channel.fetch_message(payload.message_id) # получаем объект сообщения
		if "Direct" == str(message.channel).split()[0]:
			guild = self.bot.get_guild(id=783286908910174219)
			member = discord.utils.get(guild.members, id=payload.user_id) 
			emoji = str(payload.emoji)
			if emoji == "👩‍🏫" and member.bot == False:
				role_add = discord.utils.get(guild.roles, id=783669858838773781)
				await member.remove_roles(role_add)
				role_teacher = discord.utils.get(guild.roles, id=783668543597445140)
				await member.add_roles(role_teacher)
				emb = discord.Embed(title="Вчитель 👩‍🏫",
					description="Супер, вiтаю Вас.\n\n"
								"Тепер Вам треба обрати свiй предмет:\n"
								"Я кщо вашого предмету тут нема, нажмiть ➡\n\n"
								"```\n"
								"0 - Математика\n"
								"1 - Українська мова\n"
								"2 - Труд. навч. дівчат\n"
								"3 - Труд. навч. хлопці\n"
								"4 - Фізика\n"
								"5 - Історія\n"
								"6 - Німецька мова \n"
								"7 - Англійська_мова│основна\n"
								"8 - Англійська_мова│друга\n"
								"9 - Географія\n"
								"10 - Зарубіжна література\n"
								"🟥 - Інформатика\n"
								"🟧 - Фіз. вих.\n"
								"🟨 - Фінансова грамотність\n"
								"🟩 - Біологія\n"
								"🟦 - Хімія\n"
								"🟪 - Мистетство\n"
								"🟫 - Основи здоров‘я```",
					colour=0x00ffe0)
				emb_reaction = await member.send(embed=emb)
				await emb_reaction.add_reaction(str("0⃣"))
				await emb_reaction.add_reaction(str("1⃣"))
				await emb_reaction.add_reaction(str("2⃣"))
				await emb_reaction.add_reaction(str("3⃣"))
				await emb_reaction.add_reaction(str("3⃣"))
				await emb_reaction.add_reaction(str("4⃣"))
				await emb_reaction.add_reaction(str("5⃣"))
				await emb_reaction.add_reaction(str("6⃣"))
				await emb_reaction.add_reaction(str("7⃣"))
				await emb_reaction.add_reaction(str("8⃣"))
				await emb_reaction.add_reaction(str("9⃣"))
				await emb_reaction.add_reaction(str("🔟"))
				await emb_reaction.add_reaction(str("🟥"))
				await emb_reaction.add_reaction(str("🟧"))
				await emb_reaction.add_reaction(str("🟨"))
				await emb_reaction.add_reaction(str("🟩"))
				await emb_reaction.add_reaction(str("🟦"))
				await emb_reaction.add_reaction(str("🟪"))
				await emb_reaction.add_reaction(str("🟫"))
			elif emoji == "👤" and member.bot == False:
				role_add = discord.utils.get(guild.roles, id=783669858838773781)
				await member.remove_roles(role_add)
				role_teacher = discord.utils.get(guild.roles, id=783668339180175370)
				await member.add_roles(role_teacher)
				emb = discord.Embed(title="Учень 👤",
					description="Супер, вiтаю тебе.\n\n"
								"Далi оберiть свою стать:\n"
								"Хлопець - ♂\n"
								"Дiвчина - ♀\n\n"
								"**УВАГА!!!** Це потрiбно для того, що б правильно роздiлити вас на трудовому навчанi.\n",
					colour=0x00ffe0)
				emb.set_footer(text="Цей бот е зараз на бета тестуванні, якщо помітите будь-якої неполадки, напишіть про це творцю NikStor")
				emb_reaction = await member.send(embed=emb)
				await emb_reaction.add_reaction(str("♂"))
				await emb_reaction.add_reaction(str("♀"))

			if emoji == "♂" or emoji == "♀" and member.bot == False:
				role_man = discord.utils.get(guild.roles, id=784335526735642706)
				role_woman = discord.utils.get(guild.roles, id=784336327344521266)
				for member_roles in member.roles:
					if str(role_man) == str(member_roles) or str(role_woman) == str(member_roles):
						emb = discord.Embed(title="Помилка ❗",
							description=f"В вас вже є ця роль _**{member_roles.name}**_",
							colour=0x00b8ff)
						await member.send(embed=emb)
						return
				emb = discord.Embed(title="Обри свою группу",
					description="Прекрасно, тепер менi треба знати в якiй ви групi:\n\n"
								"🎲 - Основна англійська\n"
								"🎱 - Основна нiмецька\n",
					colour=0x00b8ff)
				if emoji == "♂" and member.bot == False:
					await member.add_roles(role_man)
				elif emoji == "♀" and member.bot == False:
					await member.add_roles(role_woman)

				message = await member.send(embed=emb)
				await message.add_reaction(str("🎲"))
				await message.add_reaction(str("🎱"))
			if emoji == "🎲" and member.bot == False:
				role_main_1 = discord.utils.get(guild.roles, id=784338113626505218)
				role_enother_1 = discord.utils.get(guild.roles, id=784338778805370891)
				role_main_2 = discord.utils.get(guild.roles, id=784338449887920138)
				role_enother_2 = discord.utils.get(guild.roles, id=784338340333879306)

				for member_roles in member.roles:
					if str(role_enother_1) == str(member_roles) or str(role_main_1) == str(member_roles) or str(role_main_2) == str(member_roles) or str(role_enother_2) == str(member_roles):
						emb = discord.Embed(title="Помилка ❗",
							description=f"В вас вже є ця роль _**{member_roles.name}**_",
							colour=0x0047ff)
						await member.send(embed=emb)
						return
				emb = discord.Embed(title="Им'я та Призвище",
					description="Майже все, тепер вам потрібно написати своє ім'я, щоб вчителі знали до кого звертатися 😜.\n\n"
								"Напиши менi таке повiдомлення `ПІБ [призвище] [ім'я]`",
					colour=0x0047ff)
				emb_reaction = await member.send(embed=emb)
				await member.add_roles(role_main_1)
				await member.add_roles(role_enother_1)
			elif emoji == "🎱" and member.bot == False:
				role_main_1 = discord.utils.get(guild.roles, id=784338113626505218)
				role_enother_1 = discord.utils.get(guild.roles, id=784338778805370891)
				role_main_2 = discord.utils.get(guild.roles, id=784338449887920138)
				role_enother_2 = discord.utils.get(guild.roles, id=784338340333879306)

				for member_roles in member.roles:
					if str(role_enother_1) == str(member_roles) or str(role_main_1) == str(member_roles) or str(role_main_2) == str(member_roles) or str(role_enother_2) == str(member_roles):
						emb = discord.Embed(title="Помилка ❗",
							description=f"В вас вже є ця роль _**{member_roles.name}**_",
							colour=0x0047ff)
						await member.send(embed=emb)
						return
				emb = discord.Embed(title="Им'я та Призвище",
					description="Майже все, тепер вам потрібно написати своє ім'я, щоб вчителі знали до кого звертатися 😜.\n\n"
								"Напиши менi таке повiдомлення `ПІБ [призвище] [ім'я]`",
					colour=0x0047ff)
				emb_reaction = await member.send(embed=emb)
				await member.add_roles(role_main_2)
				await member.add_roles(role_enother_2)

			if emoji == "0⃣" and member.bot == False:
				role = discord.utils.get(guild.roles, id=784321822933778452)
				for member_roles in member.roles:
					if str(role) == str(member_roles):	
						emb = discord.Embed(title="Помилка ❗",
							description=f"В вас вже є ця роль _**{role.name}**_",
							colour=0x00b8ff)
						await member.send(embed=emb)
						return
				emb = discord.Embed(title="Им'я та Призвище",
					description="Майже все, тепер вам потрібно написати своє ім'я, щоб дiти знали до кого звертатися :stuck_out_tongue_winking_eye:.\n"
								"Напиши менi таке повiдомлення `ПІБ [призвище] [ім'я]`",
					colour=0x00b8ff)
				await member.send(embed=emb)
				await member.add_roles(role)
			elif emoji == "1⃣" and member.bot == False:
				role = discord.utils.get(guild.roles, id=784321481328164916)
				for member_roles in member.roles:
					if str(role) == str(member_roles):	
						emb = discord.Embed(title="Помилка ❗",
							description=f"В вас вже є ця роль _**{role.name}**_",
							colour=0x00b8ff)
						await member.send(embed=emb)
						return
				emb = discord.Embed(title="Им'я та Призвище",
					description="Майже все, тепер вам потрібно написати своє ім'я, щоб дiти знали до кого звертатися :stuck_out_tongue_winking_eye:.\n"
								"Напиши менi таке повiдомлення `ПІБ [призвище] [ім'я]`",
					colour=0x00b8ff)
				await member.send(embed=emb)
				await member.add_roles(role)
			elif emoji == "2⃣" and member.bot == False:
				role = discord.utils.get(guild.roles, id=784324863720292352)
				for member_roles in member.roles:
					if str(role) == str(member_roles):	
						emb = discord.Embed(title="Помилка ❗",
							description=f"В вас вже є ця роль _**{role.name}**_",
							colour=0x00b8ff)
						await member.send(embed=emb)
						return
				emb = discord.Embed(title="Им'я та Призвище",
					description="Майже все, тепер вам потрібно написати своє ім'я, щоб дiти знали до кого звертатися :stuck_out_tongue_winking_eye:.\n"
								"Напиши менi таке повiдомлення `ПІБ [призвище] [ім'я]`",
					colour=0x00b8ff)
				await member.send(embed=emb)
				await member.add_roles(role)
			elif emoji == "3⃣" and member.bot == False:
				role = discord.utils.get(guild.roles, id=784326130999754822)
				for member_roles in member.roles:
					if str(role) == str(member_roles):	
						emb = discord.Embed(title="Помилка ❗",
							description=f"В вас вже є ця роль _**{role.name}**_",
							colour=0x00b8ff)
						await member.send(embed=emb)
						return
				emb = discord.Embed(title="Им'я та Призвище",
					description="Майже все, тепер вам потрібно написати своє ім'я, щоб дiти знали до кого звертатися :stuck_out_tongue_winking_eye:.\n"
								"Напиши менi таке повiдомлення `ПІБ [призвище] [ім'я]`",
					colour=0x00b8ff)
				await member.send(embed=emb)
				await member.add_roles(role)
			elif emoji == "4⃣" and member.bot == False:
				role = discord.utils.get(guild.roles, id=784322767645966336)
				for member_roles in member.roles:
					if str(role) == str(member_roles):	
						emb = discord.Embed(title="Помилка ❗",
							description=f"В вас вже є ця роль _**{role.name}**_",
							colour=0x00b8ff)
						await member.send(embed=emb)
						return
				emb = discord.Embed(title="Им'я та Призвище",
					description="Майже все, тепер вам потрібно написати своє ім'я, щоб дiти знали до кого звертатися :stuck_out_tongue_winking_eye:.\n"
								"Напиши менi таке повiдомлення `ПІБ [призвище] [ім'я]`",
					colour=0x00b8ff)
				await member.send(embed=emb)
				await member.add_roles(role)
			elif emoji == "5⃣" and member.bot == False:
				role = discord.utils.get(guild.roles, id=784324549806129163)
				for member_roles in member.roles:
					if str(role) == str(member_roles):	
						emb = discord.Embed(title="Помилка ❗",
							description=f"В вас вже є ця роль _**{role.name}**_",
							colour=0x00b8ff)
						await member.send(embed=emb)
						return
				emb = discord.Embed(title="Им'я та Призвище",
					description="Майже все, тепер вам потрібно написати своє ім'я, щоб дiти знали до кого звертатися :stuck_out_tongue_winking_eye:.\n"
								"Напиши менi таке повiдомлення `ПІБ [призвище] [ім'я]`",
					colour=0x00b8ff)
				await member.send(embed=emb)
				await member.add_roles(role)
			elif emoji == "6⃣" and member.bot == False:
				role = discord.utils.get(guild.roles, id=784322036277313556)
				for member_roles in member.roles:
					if str(role) == str(member_roles):	
						emb = discord.Embed(title="Помилка ❗",
							description=f"В вас вже є ця роль _**{role.name}**_",
							colour=0x00b8ff)
						await member.send(embed=emb)
						return
				emb = discord.Embed(title="Им'я та Призвище",
					description="Майже все, тепер вам потрібно написати своє ім'я, щоб дiти знали до кого звертатися :stuck_out_tongue_winking_eye:.\n"
								"Напиши менi таке повiдомлення `ПІБ [призвище] [ім'я]`",
					colour=0x00b8ff)
				await member.send(embed=emb)
				await member.add_roles(role)
			elif emoji == "7⃣" and member.bot == False:
				role = discord.utils.get(guild.roles, id=784331869864067124)
				for member_roles in member.roles:
					if str(role) == str(member_roles):	
						emb = discord.Embed(title="Помилка ❗",
							description=f"В вас вже є ця роль _**{role.name}**_",
							colour=0x00b8ff)
						await member.send(embed=emb)
						return
				emb = discord.Embed(title="Им'я та Призвище",
					description="Майже все, тепер вам потрібно написати своє ім'я, щоб дiти знали до кого звертатися :stuck_out_tongue_winking_eye:.\n"
								"Напиши менi таке повiдомлення `ПІБ [призвище] [ім'я]`",
					colour=0x00b8ff)
				await member.send(embed=emb)
				await member.add_roles(role)
			elif emoji == "8⃣" and member.bot == False:
				role = discord.utils.get(guild.roles, id=784330496821297152)
				for member_roles in member.roles:
					if str(role) == str(member_roles):	
						emb = discord.Embed(title="Помилка ❗",
							description=f"В вас вже є ця роль _**{role.name}**_",
							colour=0x00b8ff)
						await member.send(embed=emb)
						return
				emb = discord.Embed(title="Им'я та Призвище",
					description="Майже все, тепер вам потрібно написати своє ім'я, щоб дiти знали до кого звертатися :stuck_out_tongue_winking_eye:.\n"
								"Напиши менi таке повiдомлення `ПІБ [призвище] [ім'я]`",
					colour=0x00b8ff)
				await member.send(embed=emb)
				await member.add_roles(role)
			elif emoji == "9⃣" and member.bot == False:
				role = discord.utils.get(guild.roles, id=784324698384891924)
				for member_roles in member.roles:
					if str(role) == str(member_roles):	
						emb = discord.Embed(title="Помилка ❗",
							description=f"В вас вже є ця роль _**{role.name}**_",
							colour=0x00b8ff)
						await member.send(embed=emb)
						return
				emb = discord.Embed(title="Им'я та Призвище",
					description="Майже все, тепер вам потрібно написати своє ім'я, щоб дiти знали до кого звертатися :stuck_out_tongue_winking_eye:.\n"
								"Напиши менi таке повiдомлення `ПІБ [призвище] [ім'я]`",
					colour=0x00b8ff)
				await member.send(embed=emb)
				await member.add_roles(role)
			elif emoji == "🔟" and member.bot == False:
				role = discord.utils.get(guild.roles, id=784324230094520320)
				for member_roles in member.roles:
					if str(role) == str(member_roles):	
						emb = discord.Embed(title="Помилка ❗",
							description=f"В вас вже є ця роль _**{role.name}**_",
							colour=0x00b8ff)
						await member.send(embed=emb)
						return
				emb = discord.Embed(title="Им'я та Призвище",
					description="Майже все, тепер вам потрібно написати своє ім'я, щоб дiти знали до кого звертатися :stuck_out_tongue_winking_eye:.\n"
								"Напиши менi таке повiдомлення `ПІБ [призвище] [ім'я]`",
					colour=0x00b8ff)
				await member.send(embed=emb)
				await member.add_roles(role)
			elif emoji == "🟥" and member.bot == False:
				role = discord.utils.get(guild.roles, id=784322532853415957)
				for member_roles in member.roles:
					if str(role) == str(member_roles):	
						emb = discord.Embed(title="Помилка ❗",
							description=f"В вас вже є ця роль _**{role.name}**_",
							colour=0x00b8ff)
						await member.send(embed=emb)
						return
				emb = discord.Embed(title="Им'я та Призвище",
					description="Майже все, тепер вам потрібно написати своє ім'я, щоб дiти знали до кого звертатися :stuck_out_tongue_winking_eye:.\n"
								"Напиши менi таке повiдомлення `ПІБ [призвище] [ім'я]`",
					colour=0x00b8ff)
				await member.send(embed=emb)
				await member.add_roles(role)
			elif emoji == "🟧" and member.bot == False:
				role = discord.utils.get(guild.roles, id=784326297143738379)
				for member_roles in member.roles:
					if str(role) == str(member_roles):	
						emb = discord.Embed(title="Помилка ❗",
							description=f"В вас вже є ця роль _**{role.name}**_",
							colour=0x00b8ff)
						await member.send(embed=emb)
						return
				emb = discord.Embed(title="Им'я та Призвище",
					description="Майже все, тепер вам потрібно написати своє ім'я, щоб дiти знали до кого звертатися :stuck_out_tongue_winking_eye:.\n"
								"Напиши менi таке повiдомлення `ПІБ [призвище] [ім'я]`",
					colour=0x00b8ff)
				await member.send(embed=emb)
				await member.add_roles(role)
			elif emoji == "🟨" and member.bot == False:
				role = discord.utils.get(guild.roles, id=784327077977260082)
				for member_roles in member.roles:
					if str(role) == str(member_roles):	
						emb = discord.Embed(title="Помилка ❗",
							description=f"В вас вже є ця роль _**{role.name}**_",
							colour=0x00b8ff)
						await member.send(embed=emb)
						return
				emb = discord.Embed(title="Им'я та Призвище",
					description="Майже все, тепер вам потрібно написати своє ім'я, щоб дiти знали до кого звертатися :stuck_out_tongue_winking_eye:.\n"
								"Напиши менi таке повiдомлення `ПІБ [призвище] [ім'я]`",
					colour=0x00b8ff)
				await member.send(embed=emb)
				await member.add_roles(role)
			elif emoji == "🟩" and member.bot == False:
				role = discord.utils.get(guild.roles, id=784323214016512042)
				for member_roles in member.roles:
					if str(role) == str(member_roles):	
						emb = discord.Embed(title="Помилка ❗",
							description=f"В вас вже є ця роль _**{role.name}**_",
							colour=0x00b8ff)
						await member.send(embed=emb)
						return
				emb = discord.Embed(title="Им'я та Призвище",
					description="Майже все, тепер вам потрібно написати своє ім'я, щоб дiти знали до кого звертатися :stuck_out_tongue_winking_eye:.\n"
								"Напиши менi таке повiдомлення `ПІБ [призвище] [ім'я]`",
					colour=0x00b8ff)
				await member.send(embed=emb)
				await member.add_roles(role)
			elif emoji == "🟦" and member.bot == False:
				role = discord.utils.get(guild.roles, id=784323345466130433)
				for member_roles in member.roles:
					if str(role) == str(member_roles):	
						emb = discord.Embed(title="Помилка ❗",
							description=f"В вас вже є ця роль _**{role.name}**_",
							colour=0x00b8ff)
						await member.send(embed=emb)
						return
				emb = discord.Embed(title="Им'я та Призвище",
					description="Майже все, тепер вам потрібно написати своє ім'я, щоб дiти знали до кого звертатися :stuck_out_tongue_winking_eye:.\n"
								"Напиши менi таке повiдомлення `ПІБ [призвище] [ім'я]`",
					colour=0x00b8ff)
				await member.send(embed=emb)
				await member.add_roles(role)
			elif emoji == "🟪" and member.bot == False:
				role = discord.utils.get(guild.roles, id=784326132308770848)
				for member_roles in member.roles:
					if str(role) == str(member_roles):	
						emb = discord.Embed(title="Помилка ❗",
							description=f"В вас вже є ця роль _**{role.name}**_",
							colour=0x00b8ff)
						await member.send(embed=emb)
						return
				emb = discord.Embed(title="Им'я та Призвище",
					description="Майже все, тепер вам потрібно написати своє ім'я, щоб дiти знали до кого звертатися :stuck_out_tongue_winking_eye:.\n"
								"Напиши менi таке повiдомлення `ПІБ [призвище] [ім'я]`",
					colour=0x00b8ff)
				await member.send(embed=emb)
				await member.add_roles(role)
			elif emoji == "🟫" and member.bot == False:
				role = discord.utils.get(guild.roles, id=784327079411843072)
				for member_roles in member.roles:
					if str(role) == str(member_roles):	
						emb = discord.Embed(title="Помилка ❗",
							description=f"В вас вже є ця роль _**{role.name}**_",
							colour=0x00b8ff)
						await member.send(embed=emb)
						return
				emb = discord.Embed(title="Им'я та Призвище",
					description="Майже все, тепер вам потрібно написати своє ім'я, щоб дiти знали до кого звертатися :stuck_out_tongue_winking_eye:.\n"
								"Напиши менi таке повiдомлення `ПІБ [призвище] [ім'я]`",
					colour=0x00b8ff)
				await member.send(embed=emb)
				await member.add_roles(role)

		else:
			member = discord.utils.get(message.guild.members, id=payload.user_id) # получаем объект пользователя который поставил реакцию
			emoji = str(payload.emoji)
			if message.id == 784714870258925588 and emoji == "✅" and member.bot == False:
				emb = discord.Embed(title="Обери свою роль 🎭", 
					description="Отже, тепер Вам потрiбно обрати - Ви вчитель чи учень\n\n"
								"Вчитель => 👩‍🏫\n"
								"Учень => 👤\n\n"
								"Після цього дійте за інструкцією 😋",
					colour=0x00ffa3)
				emb.set_footer(text="Цей бот е зараз на бета тестуванні, якщо помітите будь-якої неполадки, напишіть про це творцю NikStor")
				emb_reaction = await member.send(embed=emb)
				await emb_reaction.add_reaction(str("👩‍🏫"))
				await emb_reaction.add_reaction(str("👤"))



def setup(bot):
	bot.add_cog(member_add_leave(bot))