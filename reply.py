import discord
import os

import tema_gacha
import command

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    anlys: int = command.anlys(message.content)

    if anlys == 0:
        await message.channel.send(message.author.mention + '　テーマ　：　')

client.run(os.environ.get('discord_token'))
