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
from requests import get
import json
from getImg_v2 import getImg
import logging as log
from random import randint, choice
from string import ascii_lowercase
from platform import system

class CommieDoggie(discord.Client):
    '''
    A simple commie bot that does some cringe things :v
    '''
    def __init__(self, dataGatherFp, logfile = 'commie.log'):
        super(CommieDoggie, self).__init__()
        self.token = ''
        self.dataGatherFp = dataGatherFp
        log.basicConfig(filename = logfile, level=log.INFO)
        self.path_sep = '/'
        if system() == 'Windows': self.path_sep = "\\"

    
    async def on_ready(self):
        print('We have logged in as {0.user}'.format(self))
    
    async def on_message(self, message):

        self.logUserData(message)

    
        if message.content.lower().startswith(',sp'):
            try:
                message.content = message.content.split()[1]
                m_id = message.content.replace('<', '').replace('>', '').replace('@', '').replace('!', '')
                print(m_id)
                user = message.channel.get_member(m_id)
                print(user.avatar_url)
                await message.channel.send(user.avatar_url)
            except Exception as e:
                await message.channel.send("Command Syntax error!")
                log.error(str(e))

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

        # print('Message from {0.author}: {0.content} {0.author.id} {0.author.avatar_url}'.format(message))

    def logUserData(self, message):
        try:
            imgUrl = str(message.author.avatar_url)
            con = get(imgUrl).content
            of = "userPhoto" + self.path_sep + str(randint(0, 4096)) + "".join([choice(ascii_lowercase) for _ in range(16)]) + "." + imgUrl.split("?")[0].split(".")[-1]
            with open(of, 'wb') as op:
                op.write(con)

            print('{0.author}, {0.content}, {0.author.id}, {}'.format(message, of), file=self.dataGatherFp)
        except Exception as e:
            print("Error : {}".format(str(e)), file=self.dataGatherFp)
            log.error(str(e))

    def read_token(self):
        with open('api_keys.json') as key:
            self.token = json.load(key)['Discord_token']


if __name__ == "__main__":
    with open('user_data.csv', 'a+') as dataGatherFp: 
        bot = CommieDoggie(dataGatherFp)
        bot.read_token()

        bot.run(bot.token)

