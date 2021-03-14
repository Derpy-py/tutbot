import discord
from discord.ext import commands
import random
import json
import traceback
import sys

intents = discord.Intents.all()

client = commands.Bot(command_prefix='$', intents=intents)
client.remove_command('help')

intial_extensions = ['cogs.help']

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


@client.event
async def on_member_join(member):
    print(f'{member} has joined a server!')
    with open('afk.json', 'r') as f:
        afk = json.load(f)

    await update_data(afk, member)

    with open('afk.json', 'w') as f:
        json.dump(afk, f)


async def update_data(afk, user):
    if not f'{user.id}' in afk:
        afk[f'{user.id}'] = {}
        afk[f'{user.id}']['AFK'] = 'False'


@client.event
async def on_message(message):
    with open('afk.json', 'r') as f:
        afk = json.load(f)

    for x in message.mentions:
        if afk[f'{x.id}']['AFK'] == 'True':
            if message.author.bot:
                return
            await message.channel.send(f'{x} is AFK!')

    if not message.author.bot:
        await update_data(afk, message.author)

        if afk[f'{message.author.id}']['AFK'] == 'True':
            await message.channel.send(f'{message.author.mention} is no longer afk!')
            afk[f'{message.author.id}']['AFK'] = 'False'
            with open('afk.json', 'w') as f:
                json.dump(afk, f)
			try:
				await message.author.edit(nick=f'{message.author.display_name[5:]}')
			except Exceptions as err:
				print(f'Something is wrong: {err}')
    with open('afk.json', 'w') as f:
        json.dump(afk, f)

    await client.process_commands(message)

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server!')


@client.command()
async def say(ctx, *, say):
    await ctx.send(say)

@client.command()
async def afk(ctx, reason=None):
    with open('afk.json', 'r') as f:
        afk = json.load(f)

    if not reason:
        reason = 'None'

    afk[f'{ctx.author.id}']['AFK'] = 'True'
    await ctx.send(f'You are now AFK! Reason: {reason}')

    with open('afk.json', 'w') as f:
        json.dump(afk, f)
	try:
		await ctx.author.edit(nick=f'[AFK]{ctx.author.display_name}')
	except Exceptions as err:
		print(f'Something is wrong: {err}')

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


client.run('a') # Token Here lol
