import discord
from discord.ext import commands
import json
import random
import datetime
from core.classes import Cog_Extension

with open('seeting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class 加入與離開(Cog_Extension):

    @commands.Cog.listener() #加入伺服器
    async def on_member_join(self,member):
        channel1 = self.bot.get_channel(684752098671198238)
        channel2 = self.bot.get_channel(853308704140165181)
        embed=discord.Embed(title=" ", color=0xa3b0ff)
        embed.set_author(name="🟢加入伺服器")
        embed.add_field(name=f'歡迎 {member} 加入伺服器', value=f'先到頻道【#📢公告及規章_information】看看吧!', inline=True)
        await channel1.send(embed=embed)
        await channel2.send(embed=embed)

    @commands.Cog.listener() #離開伺服器
    async def on_member_remove(self,member):
        channel1 = self.bot.get_channel(684752098671198238)
        channel2 = self.bot.get_channel(853308704140165181)
        embed=discord.Embed(title=" ", color=0xa3b0ff)
        embed.set_author(name="🔴離開伺服器")
        embed.add_field(name=f'{member} 離開了伺服器', value=f'我們懷念他/她', inline=False)
        await channel1.send(embed=embed)
        await channel2.send(embed=embed)

def setup(bot):
    bot.add_cog(加入與離開(bot))