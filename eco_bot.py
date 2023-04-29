import discord
from discord.ext import commands
import random
from eco_bot_logic import *
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def eco(ctx, eco_1="ff"):
    if eco_1=="ff":
        emb = discord.Embed(
            description=f"Хочешь почувствовать себя на месте директора экологии и ресурсов и принимать решения которые могут повлиять на мир и его состояния. Если да то напиши **$eco yes**, если нет напиши **$eco no**"
        )
        await ctx.send(embed=emb)
    if eco_1=="yes":
        emb = discord.Embed(
            description="**https://dialogs.yandex.ru/store/skills/d4d7dec6-sohrani-ekologiyu**"
        )
        await ctx.send(embed=emb)
    if eco_1=="no":
        emb = discord.Embed(
            description="Ну как хотите"
        )
        await ctx.send(embed=emb)

@bot.command()
async def how_eco(ctx):
    emb = discord.Embed(
        title="Как спасти природу: 8 шагов, которые может сделать каждый",
        description="\nЭКОНОМЬТЕ РЕСУРСЫ\nРАЗДЕЛЯЙТЕ МУСОР\nСДАВАЙТЕ ВТОРСЫРЬЁ\nВЫБИРАЙТЕ ЭКОЛОГИЧНЫЙ ТРАНСПОРТ\nИСПОЛЬЗУЙТЕ ПОВТОРНО И НЕ БЕРИТЕ ЛИШНЕЕ\nВНЕДРЯЙТЕ ЭКО-ПРИВЫЧКИ НА РАБОТЕ\nОБРАТИТЕ ВНИМАНИЕ НА ПИТАНИЕ\nПОСТАРАЙТЕСЬ ОТВЫКНУТЬ ОТ ПЛАСТИКА"
    )
    await ctx.send(embed=emb)
@bot.command()
async def fact_eco(ctx):
    await ctx.send(f"{gen_eco}")
@bot.command()
async def how_eco_plastic(ctx):
    emb=discord.Embed(
        title="7 способов уменьшить потребление пластика",
        description="\nОткажитесь от пластиковых пакетов\nНе покупайте воду каждый раз\nИспользуйте собственную кружку\nЕсли пластик, то многоразовый\nПокупайте еду правильно\nВыбирайте неупакованные чистящие средства\nОткажитесь от пластиковой посуды"
    )
    await ctx.send(embed=emb)
@bot.command()
async def how_eco_water(ctx):
    emb=discord.Embed(
        title="9 эффективных решений по борьбе с загрязнением воды для защиты окружающей среды",
        description="\nОчистка сточных вод\nСокращение пластиковых отходов\nЭкономия воды\nУстановите водосберегающий туалет в своем доме\nСептики\nНе используйте туалет в качестве мусорной корзины\nУправление ливневыми стоками\nЗеленое сельское хозяйство\nДенитрификация"
    )
    await ctx.send(embed=emb)
@bot.command()
async def help_1(ctx):
    emb=discord.Embed(
        title="Команды которые умеет этот бот",
        description="\n$eco\n$how_eco\n$fact_eco\n$how_eco_plastic\n$how_eco_water"
    )
    await ctx.send(embed=emb)
bot.run("токен")