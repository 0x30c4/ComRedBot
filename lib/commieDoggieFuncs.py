import discord
from discord.ext import commands

class CommieDoggie(commands.Cog):
    '''
    A simple commie bot that does some cringe things :v
    '''
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Doggie is ready!')
        await self.client.change_presence(status = discord.Status.idle, activity=discord.Game("[ Barking in red ]"))

    @commands.command()
    async def clear(self, ctx, amout = 5):
        try:
            await ctx.channel.purge(limit = amout + 1)
        except:
            await ctx.channel.send("Can't clear in this channel!!!")

    @commands.command()
    async def gp(self, ctx, member):
        member = member.replace(">", "").replace("<", "").replace("!", "").replace("@", "").strip()
        # member_id = "https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(user)
        # user = ctx.channel.get_member(member_id)
        print(ctx.bot.users)

def setup(client):
    client.add_cog(CommieDoggie(client))