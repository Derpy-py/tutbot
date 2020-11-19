import discord
from discord.ext import commands

class Help(commands.Cog):
    """Commands involving Help."""

    def __init__(self,client,*args,**kwargs):
        self.client = client

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        embed = discord.Embed(title='Help!', colour=ctx.author.color)
        embed.add_field(name='Commands:', value='Help | Displays this message.\nSay | Make the bot say what you want!\nTestEmbed | Shows a test embed!')

        await ctx.send(embed=embed)

    @help.command()
    async def say(self, ctx):
        await ctx.send('```$say <say>```')

    @help.command()
    async def testembed(self, ctx):
        await ctx.send('```$testembed```')

def setup(client):
    client.add_cog(Help(client))
    print('Help is loaded!')