import discord
import config
import os
import re
import sqlite3

from discord.ext import commands

intents = discord.Intents.all() # надо добавить эту строку 
# И в client дополительно записать intents=intents
bot = commands.Bot(command_prefix=".", intents=intents)

#Загружаю коги
@bot.command()
async def load(ctx, extensions):
	bot.load_extensions(f'cgs.{extensions}')#Загрузка дополнений
	await ctx.send('loaded')

#Разгрузка
@bot.command()
async def reload(ctx, extensions):
	bot.unload_extension(f'cgs.{extensions}')#Розгрузка дополнений
	await ctx.send('unloaded')

@bot.command()
async def unload(ctx, extensions):
	bot.unload_extension(f'cgs.{extensions}')#Розгрузка дополнений
	bot.load_extensions(f'cgs.{extensions}')#Загрузка дополнений
	await bot.send('unload')

for filename in os.listdir('./cgs'): # Цикл перебирающий файлы в cogs
	if filename.endswith('.py'): # если файл кончается на .py, то это наш ког
		bot.load_extension(f'cgs.{filename[:-3]}') # командуем боту 
		#загрузитьвсе расширения. Это нужно для того, чтобы вы перезапуская 
		#бота неписали команды загрузки. При наличии этого цикла бот 
		#стартует сразус полной загрузкой когов
# Connect
bot.run(config.TOKEN)