import discord
import asyncio
from discord.ext import commands

token = 'LOL'
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = '++',intents = intents)
client.remove_command('help')


@client.event
async def on_ready():
    print('Online')
   

@client.command()
async def dmall(ctx, *, message):
    for user in list(ctx.guild.members):
        try:
            await asyncio.sleep(0.5)    
            await user.send(message)
            await ctx.send(f'Sent "{message}" To {user}')
        except:
            pass

    
client.run(token, bot = True)
