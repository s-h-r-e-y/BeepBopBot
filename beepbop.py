import discord
from discord.ext import commands
import json
import random
# read token from config file
config_file = 'config.json'
with open(config_file, 'r') as c_file:
    config = json.load(c_file)

description = 'A nice little bot'
bot = commands.Bot(command_prefix='!', description=description)
TOKEN = config['token']

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

@bot.command(pass_context=True)
async def toss(ctx):
    outcome = ['Heads','Tails']
    await bot.say('It\'s {}'.format(random.choice(outcome)))

bot.run(TOKEN)