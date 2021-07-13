import discord
from discord.ext import commands
import json
import random
from core.classes import Cog_Extension

with open('seeting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class 錯誤(Cog_Extension):    

    @commands.Cog.listener() #處理指令錯誤(公用)
    async def on_command_error(self,ctx,error):
        if isinstance(error,commands.errors.MissingRequiredArgument):
            embed=discord.Embed(title=" ", color=0xa3b0ff)
            embed.add_field(name="⚠ 未輸入後續參數", value=f'以!說 為例，請輸入【!說 (文字)】', inline=False)
            await ctx.send(embed=embed)
        elif isinstance(error,commands.errors.CommandNotFound):
            embed=discord.Embed(title=" ", color=0xa3b0ff)
            embed.add_field(name="⚠ 指令不正確或沒有此指令", value="如要查看所有指令，請輸入【!指令】", inline=False)
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title=" ", color=0xa3b0ff)
            embed.add_field(name="🐞 發生預料外的錯誤", value="提示:請嘗試將錯誤回報開發人員", inline=False)
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(錯誤(bot))