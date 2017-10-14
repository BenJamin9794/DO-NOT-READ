
import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!ping'):
        await client.send_message(message.channel, 'pong')

client.run('MzU4MzYzMjczNjYzNjEwODgy.DMOO4A.ArwYgGK5jMSKyAwCVMoI_eZT2EU', bot=True)
