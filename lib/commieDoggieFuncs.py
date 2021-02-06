import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
# from discord.utils import get
import os
import youtube_dl
from requests import get

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
        """
        Will clear last 5 messages by default.
        """
        try:
            await ctx.channel.purge(limit = amout + 1)
        except:
            await ctx.channel.send("Can't clear in this channel!!!")

    @commands.command(aliases = ['p'])
    async def play(self, ctx, *, url):
        """
        To Play a song just type `.p Mariya Takeuchi Plastic Love`
        """
        if not ctx.message.author.voice:
            await ctx.send('`Your not connected to a voice channel!`')
            return
        else:
            channel = ctx.message.author.voice.channel
            
        try:
            await channel.connect()
        except:
            if not ctx.message.author.voice:
                await ctx.send('`Your not connected to a voice channel!`')
                return
            else:
                channel = ctx.message.author.voice.channel
            

        server = ctx.message.guild
        voice_channel = server.voice_client

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        async with ctx.typing():
            try:
                # with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                #     song_info = ydl.extract_info(url, download=False)
                if not url.startswith("https://youtube.com"):
                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        try:
                            get(ydl_opts) 
                        except:
                            song_info = ydl.extract_info(f"ytsearch:{url}", download=False)['entries'][0]
                            await ctx.send('`Searching the song`')
                        else:
                            song_info = ydl.extract_info(url, download=False)
                else:
                    song_info = ydl.extract_info(url, download=False)
                
                print(url)
            except Exception as e:
                await ctx.send("`Doggie has encountered a internal problem!!`")
                return str(e)

            voice_channel.play(discord.FFmpegPCMAudio(song_info["formats"][0]["url"]), after=lambda e: print(e))
            await ctx.send("Now Playing `[ {} ]`".format(song_info['title']))

    @commands.command(aliases = ['s'])
    async def stop(self, ctx):
        """
        Stops currently playing song 
        """
        try:
            voice_client = ctx.message.guild.voice_client
            await voice_client.disconnect()
        except:
            await ctx.send('`No music is playing`')

    @commands.command()
    async def gp(self, ctx, member):
        member = member.replace(">", "").replace("<", "").replace("!", "").replace("@", "").strip()
        # member_id = "https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(user)
        # user = ctx.channel.get_member(member_id)
        print(ctx.bot.users)

def setup(client):
    client.add_cog(CommieDoggie(client))