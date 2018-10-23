import discord
from discord.ext import commands

description = 'A nice little bot'
bot = commands.Bot(command_prefix='!', description=description)
TOKEN = ''

@bot.event
async def on_ready():
    print(bot.user.id)
    print(bot.user.name)
    print('---------------')
    print('This bot is up!')

@bot.command(pass_context=True)
async def ping(ctx):
    '''Returns pong when called'''
    author = ctx.message.author.name
    server = ctx.message.server.name
    await bot.say('Pong for {} from {}!'.format(author, server))

bot.run(TOKEN)