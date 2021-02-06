#!/usr/bin/python3
# Copyright (c) 2021 0x30c4

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
from json import load
from os import listdir
from random import randint

import discord
import youtube_dl
from discord.ext import commands, tasks

with open('configNdKeys.json') as key:
        key = load(key)
        token = key['Discord_token']

client = commands.Bot(command_prefix = '.')
c = True

@client.command(aliases = ["reload_exts"])
async def rl(ctx):
    global c
    if str(ctx.message.author.id) != "723478906266452011": 
        await ctx.channel.send('Not authorized to run this command !!')
        return 0
    for f in listdir(key['cogsDir']):
        if f.endswith(".py") and f.find('Funcs') != -1:
            client.unload_extension("{}.{}".format(key['cogsDir'], f.replace(".py", '')))

    for f in listdir(key['cogsDir']):
        if f.endswith(".py") and f.find('Funcs') != -1:
            client.load_extension("{}.{}".format(key['cogsDir'], f.replace(".py", '')))
    
    await ctx.channel.send('Extentions was reloaded !!')
    if c:
        change_status.start()
        c = False

@tasks.loop(seconds = 2)
async def change_status():
    await client.change_presence(status = discord.Status.idle, activity=discord.Game("[ {} ]".format(randint(1, 69))))

for f in listdir(key['cogsDir']):
    if f.endswith(".py") and f.find('Funcs') != -1:
        client.load_extension("{}.{}".format(key['cogsDir'], f.replace(".py", '')))

# @client.command()
# async def play(ctx, url : str):
#     print(os.getcwd())
#     os.chdir('lib')
#     print(os.getcwd())

#     song_there = os.path.isfile("song.mp3")
#     try:
#         if song_there:
#             os.remove("song.mp3")
#     except PermissionError:
#         await ctx.send("Wait for the current playing music to end or use the 'stop' command")
#         return

#     voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
#     await voiceChannel.connect()
#     voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

#     ydl_opts = {
#         'format': 'bestaudio/best',
#         'postprocessors': [{
#             'key': 'FFmpegExtractAudio',
#             'preferredcodec': 'mp3',
#             'preferredquality': '192',
#         }],
#     }
#     with youtube_dl.YoutubeDL(ydl_opts) as ydl:

#         ydl.download([url])
#     for file in os.listdir("./"):
#         if file.endswith(".mp3"):
#             os.rename(file, "song.mp3")
#     voice.play(discord.FFmpegPCMAudio("song.mp3"))


# @client.command()
# async def leave(ctx):
#     voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
#     if voice.is_connected():
#         await voice.disconnect()
#     else:
#         await ctx.send("The bot is not connected to a voice channel.")


# @client.command()
# async def pause(ctx):
#     voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
#     if voice.is_playing():
#         voice.pause()
#     else:
#         await ctx.send("Currently no audio is playing.")


# @client.command()
# async def resume(ctx):
#     voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
#     if voice.is_paused():
#         voice.resume()
#     else:
#         await ctx.send("The audio is not paused.")


# @client.command()
# async def stop(ctx):
#     voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
#     voice.stop()





client.run(token)

