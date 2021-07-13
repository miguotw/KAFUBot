import discord
from discord.ext import commands
import json
import random
import datetime
import asyncio
from core.classes import Cog_Extension


with open('seeting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class 身分組教徒(Cog_Extension):

    @commands.Cog.listener() #增加身分組
    async def on_raw_reaction_add(self,msg):
        if msg.message_id == 853665208101634048: #訊息ID
            if str(msg.emoji) == '<:ToastB:698467328689569802>': #表情符號ID
                guild = self.bot.get_guild(msg.guild_id)
                role = guild.get_role(694483436353617920) #身分組ID
                await msg.member.add_roles(role)

    @commands.Cog.listener() #移除身分組
    async def on_raw_reaction_remove(self,msg):
        if msg.message_id == 853665208101634048: #訊息ID
            if str(msg.emoji) == '<:ToastB:698467328689569802>': #表情符號ID
                guild = self.bot.get_guild(msg.guild_id)
                user = guild.get_member(msg.user_id)
                role = guild.get_role(694483436353617920) #身分組ID
                await user.remove_roles(role)

def setup(bot):
    bot.add_cog(身分組教徒(bot))