import discord
import random
import os
import music
from discord.ext import commands
from keep_alive import keep_alive

cogs = [music]

client = commands.Bot(command_prefix='$', intents=discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)

palabras_tristes = [
    'matar', 'suicidar', 'matenme', 'acaben con mi vida', 'atropelle',
    'despierte vivo', 'morir', 'Me siento mal', 'Me siento de la verga'
]
safe_words = [
    'Todo va a estar bien :D', 'Recuerda que al final siempre sale el sol ^^',
    'TKM, no lo olvides <3',
    'Recuerda que hay muchar gente a la que le importas c:'
]

dos = ['dos/dosuv.jpg', 'dos/dosuve2.jpg', 'dos/dosuv3.jpg', 'dos/dosuv4.jpg']

bebas = ['Sebas di lo tuyo', 'sebas di lo tuyo', 'Di lo tuyo', 'di lo tuyo']
bebas2 = ['Peso 100 kilos aaaaaaaah']

alcohol = ['Kosako', 'kosako', 'Whiskey', 'whiskey', 'Vodka', 'vodka']
gpi = ['gpi', 'Nati pon casa', 'Blue pon casa']


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Code lines'))
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
    if msg.startswith('CHINOS'.lower()):
        await message.reply('Hola chinos')

    if any(word in msg for word in palabras_tristes):
        await message.reply(random.choice(safe_words))

    if any(word in msg for word in bebas):
        await message.reply(random.choice(bebas2))

    if any(word in msg for word in alcohol):
        await message.reply(random.choice(gpi))

    if client.user in message.mentions:
        await message.reply('Hola {} ^^'.format(message.author.mention))

    if msg.startswith('lets fucking go'):
        await message.channel.send(file=discord.File('imagenes/letsgo.jpg'))

    if msg.find('el clash') != -1:
        await message.channel.send(file=discord.File('imagenes/a.png'))

    if msg.find('me siento mal') != -1:
        await message.channel.send(file=discord.File('imagenes/bno.jpg'))

    if msg.find(':v') != -1:
        await message.channel.send(file=discord.File(random.choice(dos)))

    await client.process_commands(message)


keep_alive()
client.run(os.environ['TOKEN'])
