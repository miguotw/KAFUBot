import discord
from discord.ext import commands
import json
import random
from core.classes import Cog_Extension

with open('seeting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class 關鍵字觸發(Cog_Extension):

    @commands.Cog.listener()
    async def on_message(self,msg):

        if msg.content.endswith('婆') and msg.author != self.bot.user:
            await msg.channel.send('又你婆了 馬的臭DD')

        if msg.content.endswith('ㄐㄐ') and msg.author != self.bot.user:
            await msg.channel.send('ㄐㄐ')

        if msg.content.endswith('r r') and msg.author != self.bot.user:
            await msg.channel.send('是ㄐㄐ，不是r r 拉白癡')

        if msg.content.endswith('〓 〓') and msg.author != self.bot.user:
            await msg.channel.send('〓 〓')

        if msg.content.endswith('???') and msg.author != self.bot.user:
            await msg.channel.send('???')   

        if msg.content.endswith('不要') and msg.author != self.bot.user:
            await msg.channel.send('= =')                   

        if msg.content.endswith('幹你娘') and msg.author != self.bot.user:
            await msg.channel.send('幹 你是全家死人逆') 

        if msg.content.endswith('睡覺') and msg.author != self.bot.user:
            await msg.channel.send('不准 睡屁 起來嗨') 

        if msg.content.endswith('想舔') and msg.author != self.bot.user:
            await msg.channel.send('OMG 噁男') 

        if msg.content.endswith('我知道') and msg.author != self.bot.user:
            await msg.channel.send('你怎麼又知道了') 
            
        if msg.content.endswith('笑死') and msg.author != self.bot.user:
            await msg.channel.send('阿你怎麼還沒死') 

        if msg.content.endswith('等等') and msg.author != self.bot.user:
            await msg.channel.send('不要，就是現在')     

        if msg.content.endswith('我死了') and msg.author != self.bot.user:
            await msg.channel.send('NSL')           
            
        if msg.content.endswith('不知道') and msg.author != self.bot.user:
            await msg.channel.send('不知道就惦惦')  

        if msg.content.endswith('發財') and msg.author != self.bot.user:
            await msg.channel.send('發呆')     

        if msg.content.endswith('道歉') and msg.author != self.bot.user:
            await msg.channel.send('歉三小，是有欠你逆')  

        if msg.content.endswith('佛心公司') and msg.author != self.bot.user:
            await msg.channel.send('╰(⊙Д⊙)╮佛心公司╭(⊙Д⊙)╯')
            await msg.channel.send('https://i.makeagif.com/media/12-20-2016/HxBOJJ.gif')

        keyword = ['幹你娘雞掰','幹你娘機掰']
        if msg.content in keyword and msg.author != self.bot.user:
            await msg.channel.send('https://youtu.be/bLekVp4ui3s')

        keyword = ['星爆氣流斬',':AcgB:',':AcgB: ','撐10秒','撐十秒','16','16連擊','十六連擊','8763','c8763','C8763']
        if msg.content in keyword and msg.author != self.bot.user:
            await msg.channel.send('噓拉')

        keyword = ['可不你怎麼看','可不你覺得呢','可不你怎麼說','可不妳怎麼看','可不妳覺得呢','可不妳怎麼說',]
        if msg.content in keyword and msg.author != self.bot.user:
            random_judgment = random.choice(jdata['judgment'])
            await msg.channel.send(f'我覺得{random_judgment}')

        keyword = ['！','驚嘆號']
        if msg.content in keyword and msg.author != self.bot.user:
            await msg.channel.send('是那個驚嘆號，不是這個驚嘆號拉，白癡喔')

def setup(bot):
    bot.add_cog(關鍵字觸發(bot))