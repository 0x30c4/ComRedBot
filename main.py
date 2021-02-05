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

import discord
from os import listdir
from discord.ext import commands
from json import load

with open('configNdKeys.json') as key:
        key = load(key)
        token = key['Discord_token']

client = commands.Bot(command_prefix = '.')

@client.command(aliases = ["reload_exts"])
async def rl(ctx):
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


for f in listdir(key['cogsDir']):
    if f.endswith(".py") and f.find('Funcs') != -1:
        client.load_extension("{}.{}".format(key['cogsDir'], f.replace(".py", '')))

client.run(token)

