import discord
import os
import random
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True
intents.message_content = True

danger = ['градусник', 'медикаменты', 'лекарства', 'аэрозоль', 'целафан', 'электроника', 'лампы', 'бытовая химия']

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def Deco(ctx, a: str):
    if a == 'metall':
        await ctx.send('10 лет разложения металла')
    elif a == 'plastik':
        await ctx.send('450 лет миним. срок разложения пластика, 1000 лет макс. срок разложения')
    elif a == 'glass':
        await ctx.send('от 1000 лет и более разлагается стекло')
    elif a == 'food':
        await ctx.send('около месяца разлогается пища')
    elif a == 'bubble gum':
        await ctx.send('30 лет разлагается жвачка')
    else:
        await ctx.send('Напиши что нибудь другое! Например: metall, plastik, glass, food, bubble gum.')

@bot.command()
async def Sort(ctx, a: str):
    if a in danger:
        await ctx.send('На переработку! Не в коем случае не боасать в мусорный бак!')
    else:
        await ctx.send('Ну выкинь че.')

@bot.command()
async def meme(ctx):
    all_mems = os.listdir("images")
    rand_mem = random.choice(all_mems)
    with open(f"images/{rand_mem}", 'rb') as f:
        imagesd = discord.File(f)
    await ctx.send(file=imagesd)

bot.run('HERE IS THE TOKEN')