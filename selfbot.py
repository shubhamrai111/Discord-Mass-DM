import discord
import asyncio
from discord.ext import commands

token = 'OTIxODI0MjU0Mzk4NDY0MDUx.Yb4hvA.kLeC1RBkoSMTayN-5f4HZ7uu7mw'

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
