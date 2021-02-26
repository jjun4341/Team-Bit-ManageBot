import discord
import asyncio
from discord.ext import commands
import random
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
coll = client.ManageBot.user

class Money(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.client = client
        self.coll = coll

    @commands.command(name = '일', aliases = ['돈줘', '돈얻기', '돈받기', '돈지급'])
    async def GetMoney(self, ctx):
        if self.coll.find_one({"_id": str(ctx.author.id)}):
            random_money = random.randint(1, 100)
            find = {"_id": str(ctx.author.id)}
            setdata = {"$inc": {"money": int(random_money)}}
            embed = discord.Embed(title = '돈 지급', description = ' ', color=0x00FFFF, inline=False)
            embed.add_field(name = '획득한 돈의 양', value = f'{str(ctx.author)}님은 일을 하여 {random_money}를 얻었습니다.')
            self.coll.update_one(find, setdata)
            await ctx.send(embed=embed)
    
    @commands.command(name = '내돈', aliases = ['내돈확인', '나의돈'])
    async def MyMoney(self, ctx):
        if self.coll.find_one({"_id": str(ctx.author.id)}):
            MyMoney_User_Data = self.coll.find_one({"_id": str(ctx.author.id)})
            embed = discord.Embed(title = f'{str(ctx.author)}님의 돈', description = ' ', color = 0xFF00)
            embed.add_field(name = '현재 돈', value = ':money_with_wings:' + str(MyMoney_User_Data['money']))
            await ctx.send(embed=embed)
    
    @commands.command(name = '도박')
    async def DoBack(self, ctx, money=None):
        if money == None:
            await ctx.send('올바른 사용법은 `!도박 <원하는-금액>` 이에요!')
        if self.coll.find_one({"_id": str(ctx.author.id)}):
            a = await ctx.send('룰렛을 돌렸습니다!\n과연 무엇이 당첨될까요?')
            find_user_data = {"_id": str(ctx.author.id)}
            setdatas = {"$inc": -money}
            self.coll.update_one(find_user_data, setdatas)
            e = await ctx.send('https://cdn.discordapp.com/emojis/809373131978309644.gif?v=1')
            emoji = '😍'
            emoji_2 = '😎'
            emoji_3 = '😴'
            random_number_1 = random.randint(1, 3)
            random_number_2 = random.randint(1, 3)
            random_number_3 = random.randint(1, 3)
            
            if random_number_1 == random_number_2 == random_number_3:
                await a.delete()
                await e.delete()
                if random_number_1 == 1:
                    await ctx.send(emoji)
                    await asyncio.sleep(1)
                    await ctx.send(emoji)
                    await asyncio.sleep(1)
                    await ctx.send(emoji)
                    money = money * 5
                    find = {"_id": str(ctx.author.id)}
                    setdata = {"$inc": {"money": money}}
                    self.coll.update_one(find, setdata)
                    await ctx.send(f'당첨이 되셨네요?! 축하드립니다!\n{money}의 5배인 {0}원을 지급해드렸습니다!').format(money * 5)
                if random_number_1 == 2:
                    await ctx.send(emoji_2)
                    await asyncio.sleep(1)
                    await ctx.send(emoji_2)
                    await asyncio.sleep(1)
                    await ctx.send(emoji_2)
                    money = money * 5
                    find = {"_id": str(ctx.author.id)}
                    setdata = {"$inc": {"money": money}}
                    self.coll.update_one(find, setdata)
                    await ctx.send(f'당첨이 되셨네요?! 축하드립니다!\n{money}의 5배인 {0}원을 지급해드렸습니다!').format(money * 5)
                if random_number_1 == 2:
                    await ctx.send(emoji_3)
                    await asyncio.sleep(1)
                    await ctx.send(emoji_3)
                    await asyncio.sleep(1)
                    await ctx.send(emoji_3)
                    money = money * 5
                    find = {"_id": str(ctx.author.id)}
                    setdata = {"$inc": {"money": money}}
                    self.coll.update_one(find, setdata)
                    await ctx.send(f'당첨이 되셨네요?! 축하드립니다!\n{money}의 5배인 {0}원을 지급해드렸습니다!').format(money * 5)
            else:
                await ctx.send('앗, 꽝이네요. 
        else:
            await ctx.send('회원 가입이 되어있지 않아요. `!가입`으로 회원 가입을 진행해주세요!')

                

def setup(bot):
    bot.add_cog(Money(bot))
