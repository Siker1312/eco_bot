import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def eco(ctx):
    await ctx.send("Хочешь почувствовать себя на месте директора экологии и ресурсов и принимать решения которые могут повлиять на мир и его состояния. Если да то напиши $eco_yes, если нет напиши $eco_no")

@bot.command()
async def eco_yes(ctx):
    await ctx.send("https://dialogs.yandex.ru/store/skills/d4d7dec6-sohrani-ekologiyu")

@bot.command()
async def eco_no(ctx):
    await ctx.send("Ну как хотите")





bot.run("MTA5MjQ2MTU5NDcyNzk2MDY2Nw.G-GVaM.pVCJaekCApxqOpQckYEN10gEXzEaNN6t9LoIQY")