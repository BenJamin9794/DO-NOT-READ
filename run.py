
import discord
import asyncio

client = discord.Client(358363273663610882)

@client.event
async def on_ready():
    print('DanTDM#1087')
    print(client.user.name)
    print(client.user.id)
    print('358363273663610882')

@client.event
async def on_message(message):
    if message.content.startswith('!ping'):
        await client.send_message(message.channel, 'pong')

client.run('MzU4MzYzMjczNjYzNjEwODgy.DMOO4A.ArwYgGK5jMSKyAwCVMoI_eZT2EU', bot=True)
