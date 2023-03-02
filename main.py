import discord
from commands.bot_intents import intents
from commands.commands import *
from config.openai import openai_config
from env.env import *

client = intents()




@client.event
async def on_ready():

    print(f'Servidores {format(client.user)} conectados com sucesso!')
    print('Bem vindo novamente senhor!')
    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.listening, name="Immortals - Fall Out Boy"))


@client.event
async def on_message(message):

    channel = message.channel
    content = message.content.lower()
    dc_id = str(message.author.id)

    if '..' in content:

        with open('cogs/users.txt', 'r', encoding='utf-8') as user:
            users = user.read()
            if dc_id in users:

                fra = content.split('..')

                if fra[0] == '':
                    content2 = fra[1]
                elif fra[1] == '':
                    content2 = fra[0]

                print(f'[USUARIO AUTORIZADO]{message.author.name}:{content2}')

                response = openai_config(content2)

                print(response)

                await channel.send(f"{response}")
            else:
                print(f'[USUARIO SEM PERMISSÃO]{message.author.name}:{content}')
                p = 'faça uma carta xingando o usuario por nao ter acesso ao bot assinando no final com amor Tarzinho'
                response = openai_config(p)
                await channel.send(f"{response}")

    await client.process_commands(message)



client.run(BOT_DISCORD_KEY)

