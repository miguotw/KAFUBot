import discord
from discord.ext import commands
import json
import requests
import random,os,asyncio  
import datetime
import keep_alive
import re

endpoint = "https://api.twitch.tv/helix/streams?"
headers = {"Client-ID": "e0557y19d6pqf1zkefty21awjbqvj2"}
params = {"user_login": "Solary"}

intents = discord.Intents.default()
intents.members = True

with open('seeting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

time = datetime.datetime.now().strftime('[%H:%M:%S]')

bot = commands.Bot(command_prefix='!', intents = intents)  #觸發指令


@bot.event  #開機
async def on_ready():
    
    random_game = random.choice(jdata['game'])
    await bot.change_presence(activity=discord.Game(name=random_game))

    channel = bot.get_channel(700653612367609867)
    embed=discord.Embed(title=" ", color=0xa3b0ff)
    embed.add_field(name=f'⚙ 程式正在初始化...', value=f'{bot.user.name} 初始化完成，當前版本為:1.5.3',inline=False)
    await channel.send(embed=embed)

    print(f'{time}{bot.user.name} 啟動成功')
    print(f'{time}discord.py版本:{discord.__version__}')

@bot.command()  #載入cmd
async def 載入(ctx, extension):
    if ctx.author.id == 474460820131151874: 
      bot.load_extension(f'cmds.{extension}')
      embed=discord.Embed(title=" ", color=0xa3b0ff)
      embed.add_field(name="⚙ 核心指令", value=f'{extension}已成功載入', inline=False)
      await ctx.send(embed=embed)
      print(f'{time} {extension}已成功載入')
    else:
      embed=discord.Embed(title=" ", color=0xa3b0ff)
      embed.add_field(name="⚠ 權限不足", value="您沒有權限執行該操作，該指令僅限開發者操作", inline=False)
      await ctx.send(embed=embed)

@bot.command()  #取消載入cmd
async def 卸載(ctx, extension):
    if ctx.author.id == 474460820131151874: 
      bot.unload_extension(f'cmds.{extension}')
      embed=discord.Embed(title=" ", color=0xa3b0ff)
      embed.add_field(name="⚙ 核心指令", value=f'{extension}已解除載入', inline=False)
      await ctx.send(embed=embed)
      print(f'{time} {extension}已解除載入')
    else:
      embed=discord.Embed(title=" ", color=0xa3b0ff)
      embed.add_field(name="⚠ 權限不足", value="您沒有權限執行該操作，該指令僅限開發者操作", inline=False)
      await ctx.send(embed=embed)

@bot.command()  #重新載入cmd
async def 重載(ctx, extension):
    if ctx.author.id == 474460820131151874: 
      bot.reload_extension(f'cmds.{extension}')
      embed=discord.Embed(title=" ", color=0xa3b0ff)
      embed.add_field(name="⚙ 核心指令", value=f'{extension}已重新載入', inline=False)
      await ctx.send(embed=embed)
      print(f'{time} {extension}已重新載入')
    else:
      embed=discord.Embed(title=" ", color=0xa3b0ff)
      embed.add_field(name="⚠ 權限不足", value="您沒有權限執行該操作，該指令僅限開發者操作", inline=False)
      await ctx.send(embed=embed)


for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    keep_alive.keep_alive()
    bot.run('NjkyMDA4NzY4MDgyNDExNTQw.XnoRYw.XykCNq_OUpSWgsPnG8zGiQiWKH8')
