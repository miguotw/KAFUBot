import discord
from discord.ext import commands
import json
import random
import asyncio
from core.classes import Cog_Extension


with open('seeting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class 管理員指令(Cog_Extension):

    @commands.command() #公告 伺服器
    async def 公告(self,ctx,*,msg):
      if str(ctx.author.id) in (jdata['admin']):
        await ctx.message.delete()
        embed=discord.Embed(title=" ", color=0xa3b0ff)
        embed.add_field(name="📢 【伺服器公告】", value=(msg), inline=False)
        await ctx.send('@everyone',embed=embed)
      else:
        embed=discord.Embed(title=" ", color=0xa3b0ff)
        embed.add_field(name="⚠ 權限不足", value="您沒有權限執行該操作，該指令僅限管理員操作", inline=False)
        await ctx.send(embed=embed)  

    @commands.command() #公告 普通
    async def 公告普通(self,ctx,*,msg):
      if str(ctx.author.id) in (jdata['admin']):
        await ctx.message.delete()
        embed=discord.Embed(title=" ", color=0xa3b0ff)
        embed.add_field(name="📢 【伺服器公告】", value=(msg), inline=False)
        await ctx.send(embed=embed)
      else:
        embed=discord.Embed(title=" ", color=0xa3b0ff)
        embed.add_field(name="⚠ 權限不足", value="您沒有權限執行該操作，該指令僅限管理員操作", inline=False)
        await ctx.send(embed=embed)  
      
    @commands.command() #公告 南應熊頭
    async def 公告南應(self,ctx,*,msg):
      if str(ctx.author.id) in (jdata['admin']):
        await ctx.message.delete()
        embed=discord.Embed(title=" ", color=0xa3b0ff)
        embed.add_field(name="📢 【南應熊頭公告】", value=(msg), inline=False)
        await ctx.send('<@&687182478045478932>',embed=embed)
      else:
        embed=discord.Embed(title=" ", color=0xa3b0ff)
        embed.add_field(name="⚠ 權限不足", value="您沒有權限執行該操作，該指令僅限管理員操作", inline=False)
        await ctx.send(embed=embed)  

    @commands.command() #公告 minecraft
    async def 公告MC(self,ctx,*,msg):
      if str(ctx.author.id) in (jdata['admin']):
        await ctx.message.delete()
        embed=discord.Embed(title=" ", color=0xa3b0ff)
        embed.add_field(name="📢 【Minecraft伺服器公告】", value=(msg), inline=False)
        await ctx.send('@here',embed=embed)
      else:
        embed=discord.Embed(title=" ", color=0xa3b0ff)
        embed.add_field(name="⚠ 權限不足", value="您沒有權限執行該操作，該指令僅限管理員操作", inline=False)
        await ctx.send(embed=embed)  

    @commands.command() #開台通知
    async def 開台(self,ctx,*,msg):
      if str(ctx.author.id) in (jdata['admin']):
        await ctx.message.delete()
        embed=discord.Embed(title=(msg),url="https://www.twitch.tv/yelang9980", color=0xa3b0ff)
        embed.set_author(name="📢 實況開台通知")
        embed.set_thumbnail(url="https://static-cdn.jtvnw.net/jtv_user_pictures/dd8310f4-595e-4f32-a5d9-c17517b514b9-profile_image-300x300.png")
        embed.set_image(url=f'https://static-cdn.jtvnw.net/previews-ttv/live_user_yelang9980-320x180.jpg?r={random.randint(100000,999999)}')
        await ctx.send('<@&853359713592672317> 米淉淉開台了!\nhttps://www.twitch.tv/yelang9980',embed=embed)
      else:
        embed=discord.Embed(title=" ", color=0xa3b0ff)
        embed.add_field(name="⚠ 權限不足", value="您沒有權限執行該操作，該指令僅限管理員操作", inline=False)
        await ctx.send(embed=embed)  

    @commands.command() #開服通知 minecraft
    async def 開服(self,ctx):
      if str(ctx.author.id) in (jdata['admin']):
        await ctx.message.delete()
        embed=discord.Embed(title=" ", color=0xa3b0ff)
        embed.set_author(name="📢 【Minecraft伺服器開放通知】")
        embed.add_field(name=f'伺服器當前狀況 : [ 🟢 已開放 ]', value="伺服器IP位址 : hololive.dons.net",inline=False)
        embed.add_field(name=f'伺服器檔案下載 :', value="https://reurl.cc/ZG7ayl",inline=False)
        await ctx.send('@here',embed=embed)
      else:
        embed=discord.Embed(title=" ", color=0xa3b0ff)
        embed.add_field(name="⚠ 權限不足", value="您沒有權限執行該操作，該指令僅限管理員操作", inline=False)
        await ctx.send(embed=embed)  

    @commands.command() #關服通知 minecraft
    async def 關服(self,ctx):
      if str(ctx.author.id) in (jdata['admin']):
        await ctx.message.delete()
        embed=discord.Embed(title=" ", color=0xa3b0ff)
        embed.set_author(name="📢 【Minecraft伺服器開放通知】")
        embed.add_field(name=f'伺服器當前狀況 : [ 🔴 已關閉 ]', value="伺服器IP位址 : hololive.dons.net",inline=False)
        embed.add_field(name=f'伺服器檔案下載 :', value="https://reurl.cc/ZG7ayl",inline=False)
        await ctx.send('@here',embed=embed)
      else:
        embed=discord.Embed(title=" ", color=0xa3b0ff)
        embed.add_field(name="⚠ 權限不足", value="您沒有權限執行該操作，該指令僅限管理員操作", inline=False)
        await ctx.send(embed=embed)  

#    @commands.command() #清理訊息
#    async def 清理訊息(self,ctx,num: int):
#        await ctx.channel.purge(limit=num+1)
#        await ctx.send(f'已刪除 {num} 則訊息')
#        time = datetime.datetime.now().strftime('[%H:%M:%S]')
#        print(f'{time} 已刪除 {num} 則訊息')

#    @commands.Cog.listener()
#    async def on_message_delete(self,msg):
#        coynter = 1
#        async for audilog in msg.guild.audit_logs(action=discord.AuditLogAction.message_delete):
#            if coynter == 1:
#                await msg.channel.send(audilog.user.name)
#                coynter += 1

    @commands.command() #規章
    async def 規章(self,ctx,):
      if str(ctx.author.id) in (jdata['admin']):
        await ctx.message.delete()
        embed=discord.Embed(title=" ", color=0xa3b0ff)
        embed.set_author(name=f'📢 【規章】為了版面整潔及推廣網路正面發言風氣，有以下幾點請大家配合:')
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/698467328689569802.png?v=1")
        embed.add_field(name="1.所有發言及行為須遵守 Discord 服務條款，以及 Discord 社群指南", value='https://discordapp.com/terms , https://discordapp.com/guidelines .', inline=False)
        embed.add_field(name="2.推廣正面聊天風氣", value='禁止影響伺服器內秩序，例:「惡意挑釁/引戰/種族歧視/仇恨言論」。', inline=False)
        embed.add_field(name="3.張貼連結衝人氣/影響伺服器內秩序", value='惡意張貼個人部落格、留言板等意圖衝人氣之影響伺服器內秩序行為將予以刪除。', inline=False)
        embed.add_field(name="4.禁止張貼會使多數人反感之圖文", value='曬卡請至頻道:【🎮遊戲交流_games】。', inline=False)
        embed.set_footer(text="#本規章是以【巴哈姆特-場外休憩區】之板規為藍本，並修改訂製。")
        embed.set_footer(text="(ver1.2.2)")
        await ctx.send(embed=embed)
        say=(jdata['rule'])
        await ctx.send(say)
      else:
        embed=discord.Embed(title=" ", color=0xa3b0ff)
        embed.add_field(name="⚠ 權限不足", value="您沒有權限執行該操作，該指令僅限管理員操作", inline=False)
        await ctx.send(embed=embed,)  


def setup(bot):
    bot.add_cog(管理員指令(bot))