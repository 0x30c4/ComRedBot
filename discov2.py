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


class CommieDoggie(discord.Client):
    '''
    A simple commie bot that does some cringe things :v
    '''
    def __init__(self, dataGatherFp, logfile = 'commie.log'):
        super(CommieDoggie, self).__init__()
        self.token = ''
        self.dataGatherFp = dataGatherFp
        log.basicConfig(filename = logfile, level=log.INFO)
    
    async def on_ready(self):
        print('We have logged in as {0.user}'.format(self))
    
    async def on_message(self, message):
        
        user = message.author
        print(user.avatar_url)
        
        
        print('Message from {0.author}: {0.content} {0.author.id}'.format(message))
    

    def logUserData(self, message):
        print("{0.author}, ".format(message))

    def read_token(self):
        with open('api_keys.json') as key:
            self.token = json.load(key)['Discord_token']


if __name__ == "__main__":
    bot = CommieDoggie()
    bot.read_token()

    bot.run(bot.token)

