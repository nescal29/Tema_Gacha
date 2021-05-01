import discord
import os

import tema_gacha

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    anlys: int = 0

    if anlys == 0:
        await message.channel.send(message.author.mention + '　テーマ　：　' + tema_gacha.gacha())

client.run(os.environ.get('discord_token'))
