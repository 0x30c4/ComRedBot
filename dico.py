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
import os
import requests
import json
from getImg_v2 import getImg
import logging as log

client = discord.Client()


log.basicConfig(filename='commie.log', encoding='utf-8', level=log.DEBUG)


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
            return "Bainchod number dite koisi text des ken ???"
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
        q = message.content.lower().replace("$send img", '').replace(",img", '').strip()
        img_names = getImg(q)
        print(q, img_names, getImg('dog'))
        if type(img_names) is str or img_names == []:
            log.error('Query: {}\nError : Not found!!\n'.format(q))
            await message.channel.send("Sorry Image not found!! :/")
        else:
            for i in img_names:
                print('Query: {}\nSending: {}\n----------------------------------------------------------------'.format(q, i))
                log.info('Query: {}\nSending: {}\n----------------------------------------------------------------'.format(q, i))
                await message.channel.send(file=discord.File(i))


with open('api_keys.json') as key:
    key = json.load(key)

client.run(key['Discord_token'])
