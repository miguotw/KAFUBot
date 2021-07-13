import discord
from discord.ext import commands
import json
import random
import datetime
import asyncio
from core.classes import Cog_Extension

with open('seeting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class 一般指令(Cog_Extension):

    @commands.command() #權限查詢
    async def 權限(self,ctx):
      if str(ctx.author.id) in (jdata['admin']) and  str(ctx.author.id) in (jdata['developer']):
        embed=discord.Embed(title=" ", color=0xa3b0ff)
        embed.add_field(name="🛡您具有以下權限", value="開發者、管理員 與 一般 權限", inline=False)
        await ctx.send(embed=embed)
      elif str(ctx.author.id) in (jdata['admin']):
        embed=discord.Embed(title=" ", color=0xa3b0ff)
        embed.add_field(name="🛡您具有以下權限", value="管理員 與 一般 權限", inline=False)
        await ctx.send(embed=embed)
      else:
        embed=discord.Embed(title=" ", color=0xa3b0ff)
        embed.add_field(name="🛡您具有以下權限", value="一般 權限", inline=False)
        await ctx.send(embed=embed)
    
    @commands.command() #版本
    async def 版本(self,ctx):
        embed=discord.Embed(title=" ", color=0xa3b0ff)
        embed.set_author(name=f'我的當前版本為:1.5.3')
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/700653612367609867/775669783831773194/1.png")
        embed.add_field(name=f'完善權限分級', value=f'新增:開發者權限組',inline=False)
        embed.add_field(name=f'優化', value=f'機器人後臺優化',inline=False)
        embed.add_field(name=f'!指令顯示方式更新', value=f'列出所有隱藏指令',inline=False)
        embed.set_footer(text="Maker by 米淉MiGuo")
        await ctx.send(embed=embed)
    
    @commands.command() #版本
    async def pp(self,ctx):
        if  'miguo_tw@icould.com'== 'miguo_tw@icloud.com':
          print('1')
        else:
          print('0')

    @commands.command() #指令列表
    async def 指令(self,ctx,):
        embed=discord.Embed(title=" ", color=0xa3b0ff)
        embed.set_author(name=f'💬一般指令')
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/700653612367609867/775669783831773194/1.png")
        embed.add_field(name="!權限", value=f'查詢自己所在的權限組',inline=True)
        embed.add_field(name="!版本", value=f'查看我當前的版本', inline=True)
        embed.add_field(name="!指令", value=f'顯示此指令',inline=True)
        embed.add_field(name="!延遲", value=f'查看我與所在伺服器的延遲', inline=True)
        embed.add_field(name="!工商", value=f'你想要知道SERVER BOOT的力量嗎?', inline=True)
        embed.add_field(name="!午餐", value=f'讓我幫你決定午餐該吃什麼', inline=True)
        embed.add_field(name="!機率 (文字)", value=f'讓我幫你占卜你輸入的內容',inline=True)
        embed.add_field(name="!說 (文字)", value=f'讓我刪除並覆誦你輸入的文字',inline=True)
        embed.add_field(name="可不你怎麼看", value=f'關於我的看法?', inline=True)
        embed.set_footer(text="目前僅顯示一般指令，如要查看其他指令，請輸入 !指令2 或 !指令3")
        await ctx.send(embed=embed)

    @commands.command() #指令列表
    async def 指令2(self,ctx,):
        embed=discord.Embed(title=" ", color=0xa3b0ff)
        embed.set_author(name=f'💬管理員指令')
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/700653612367609867/775669783831773194/1.png")
        embed.add_field(name="!規章", value=f'伺服器規章', inline=True)
        embed.add_field(name="!開台 (標題)", value=f'米淉淉開台通知', inline=True)
        embed.add_field(name="!公告 (文字)", value=f'伺服器公告\n(有@everyone標註)', inline=True)
        embed.add_field(name="!公告普通 (文字)", value=f'伺服器公告\n(無@everyone標註)', inline=True)
        embed.add_field(name="!公告南應 (文字)", value=f'南應熊頭公告', inline=True)
        embed.add_field(name="!公告MC (文字)", value=f'Minecraft伺服器公告', inline=True)
        embed.add_field(name="!開服", value=f'minecraft開服通知', inline=True)
        embed.add_field(name="!關服", value=f'minecraft關服通知', inline=True)
        embed.set_footer(text="目前僅顯示管理員指令，如要查看其他指令，請輸入 !指令 或 !指令3")
        await ctx.send(embed=embed)

    @commands.command() #指令列表
    async def 指令3(self,ctx,):
        embed=discord.Embed(title=" ", color=0xa3b0ff)
        embed.set_author(name=f'💬開發者指令')
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/700653612367609867/775669783831773194/1.png")
        embed.add_field(name="!載入 (cmd name)", value=f'載入指令分區', inline=True)
        embed.add_field(name="!卸載 (cmd name)", value=f'卸載指令分區', inline=True)
        embed.add_field(name="!重載 (cmd name)", value=f'重載指令分區', inline=True)
        embed.set_footer(text="目前僅顯示管理員指令，如要查看其他指令，請輸入 !指令 或 !指令2")
        await ctx.send(embed=embed)

    @commands.command() #工商
    async def 工商(self,ctx,):
        embed=discord.Embed(title=" ", color=0xff73fa)
        embed.set_author(name="現在一個月只要兩次加成，就可以加成本伺服器並解鎖:",icon_url="https://ponyvilleplaza.com/files/img/boost.png")
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Unclesamwantyou.jpg/578px-Unclesamwantyou.jpg")
        embed.add_field(name="語音通訊", value="+50伺服器表情符號空位", inline=False)
        embed.add_field(name="語音通訊", value="128 Kbps音訊品質", inline=False)
        embed.add_field(name="伺服器圖示", value="動畫伺服器圖示", inline=False)
        embed.add_field(name="伺服器邀請背景", value="自訂伺服器邀請背景", inline=False)
        embed.add_field(name="好友直播", value="以高畫質向好友串流", inline=False)
        embed.set_footer(text="不考慮一下嗎?")
        await ctx.send(embed=embed)

    @commands.command() #延遲
    async def 延遲(self,ctx):
        embed=discord.Embed(title=" ", color=0xa3b0ff)
        embed.add_field(name=f'我與當前伺服器的延遲為:',value=f'{round(self.bot.latency*1000)}毫秒',inline=False)
        embed.set_footer(text="Maker by 米淉MiGuo")
        await ctx.send(embed=embed)
    
    @commands.command() #午餐
    async def 午餐(self,ctx):
        random_lunch = random.choice(jdata['lunch'])
        await ctx.send(f'今天我想來點: {random_lunch}')

    @commands.command() #機率
    async def 機率(self,ctx,*,msg):
        await ctx.send(f'{msg}的機率為{random.randint(0,100)}%')

    @commands.command() #說
    async def 說(self,ctx,*,msg):
        await ctx.message.delete()
        await ctx.send(msg)    

 
def setup(bot):
    bot.add_cog(一般指令(bot))