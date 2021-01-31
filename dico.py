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
import os
import requests
import json
from getImg import getImg

client = discord.Client()

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

def addNum(n):
    s = 0
    for i in n:
        try:
            if bool(i):
                i = int(i)
                s += i
        except:
            return "Bainchod number dite koisi text des ke ???"            
    return s

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    if message.content.lower().startswith('$hotsaxx'):
        quote = "Your daddy gaiii!!"
        await message.channel.send(quote)

    if message.content.lower().startswith('$add'):
        num = message.content.replace("$add", '').split(" ")
        print(num)
        quote = addNum(num)
        await message.channel.send(quote)

    if message.content.lower().startswith("$img") or message.content.lower().startswith(",img"):
        q = message.content.lower().replace("$send img", '').strip()
        img_name = getImg(q)
        if img_name == '404':
            print('sending ', img_name)
            await message.channel.send("Sorry Image not found!! :/")
        else:
            await message.channel.send(file=discord.File(img_name))


client.run('ODA0Nzk5MDY3NTY0NTM5OTU0.YBRlig.rIkMldBnIYb_-L_hKaR_kvy8yTo')
