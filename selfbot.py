import discord
import asyncio
from discord.ext import commands

token = 'Njk2NTk4Njg1MDA1MzgxNjQz.XorEFA.aYbYh2XruBZ5HNbORegRp6h5NK8'

prefix = 'bhu+'
client = commands.Bot(
    description='Dropout',
    command_prefix=prefix,
    self_bot=True
)
client.remove_command('help') 

@client.event
async def on_ready():
    print('Online')
   

@client.command()
async def dmall(ctx, *, message):
    for user in ctx.guild.members:
        try:
            await user.send(message)
            print(f"Sent To {user}")
        except:
            pass

    
client.run(token, bot = False)
