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

    if anlys == 1:
        await message.delete()
        await message.channel.send(message.author.mention + '　テーマ　：　' + tema_gacha.gacha())

#client.run(os.environ.get('discord_token'))
client.run('ODM3OTM1MTYxNTYzNDE0NTI4.YIzx7g.0m6jVoK3ugUftMlw5YBCVJgB0Y4')