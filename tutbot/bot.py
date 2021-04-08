import discord
from discord.ext import commands
import random
import json
import traceback
import sys

intents = discord.Intents.all()

client = commands.Bot(command_prefix='$', intents=discord.Intents.all())
client.remove_command('help')

intial_extensions = [
    'cogs.help',
    'cogs.afk'
    ]

if __name__ == '__main__':
    for extension in intial_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            print(f'Failed to load {extension}', file=sys.stderr)
            traceback.print_exc()

@client.event
async def on_ready():
    print('Logged In!')

@client.command()
async def randomword(ctx):
    ranword = ['quizzical', 'needless', 'sloppy', 'comfortable', 'front', 'wealthy', 'modify', 'faint', 'jump',
               'holiday']

    await ctx.send(random.choice(ranword))


@client.command()
async def testembed(ctx):
    embed = discord.Embed(colour=ctx.author.color, timestamp=ctx.message.created_at)
    embed.set_author(name='Test')
    embed.set_footer(text=f'Called by {ctx.author}', icon_url=ctx.author.avatar_url)
    embed.add_field(name='Test', value='Test Done')

    await ctx.send(embed=embed)


client.run('NzY0MTc1ODY0NzI0MTkzMjkw.X4CcOw.AVSfraF_Y8VBoJEFprPD2aj-qLU')
