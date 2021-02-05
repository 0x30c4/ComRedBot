import discord
from discord.ext import commands
import logging as log
from platform import system
from sys import exit as sys_exit

token = "ODA0Nzk5MDY3NTY0NTM5OTU0.YBRlig.5IedYuKleS2Bvows8jBopkoNMqE"
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
    print(member)

@client.event
async def on_member_remove(member):
    print(member)

# @client.event
# async def on_message(message):
#     print(message.content)

@client.command()
async def add(ctx, n):
    n = n.split()
    # print(n)
    s = 0
    for i in n:
        try:
            if bool(i):
                i = int(i)
                s += i
        except:
            s = "."
            await ctx.send("Bainchod number dite koisi text des ken ???")
            break
    if s != ".":
        await ctx.send(s)

@client.command()
async def clear(ctx, amout = 5):
    try:
        await ctx.channel.purge(limit = amout + 1)
    except:
        await ctx.channel.send("Can't clear in this channel!!!")

@client.command()
async def getprofile(ctx, member : discord.Member, *, reason = None):
    print(member.is_on_mobile())


@client.command()
async def shutdown(ctx):
    if str(ctx.message.author.id) == "723478906266452011":
        await ctx.channel.send('stoping the bot')
        sys_exit()
    else:
        await ctx.channel.send('You are not the admin')
    


client.run(token)