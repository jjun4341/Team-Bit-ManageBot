import discord
import asyncio
from discord.ext import commands
from pymongo import MongoClient
import random

client = MongoClient('mongodb://localhost:27017/')
coll = client.ManageBot.user

class Slot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.client = client
        self.coll = coll

    @commands.cooldown(1, 30, commands.BucketType.user)
    @commands.command(name = '도박')
    async def DoBack(self, ctx, money=None):
        if money == None:
            await ctx.send('올바른 사용법은 `!도박 <원하는-금액>` 이에요!')
        elif self.coll.find_one({"_id": str(ctx.author.id)}) and money != None:
            ddd = self.coll.find_one({"_id": str(ctx.author.id)})
            if ddd['money'] < money:
                await ctx.send(f'{ctx.author.mention}님이 소유하신 돈 보다 배팅하시려는 돈이 더 많아요!')
            else:
                findss = {"_id": str(ctx.author.id)}
                money = int(money)
                setdatass = {"$inc": {"money": -money}}
                self.coll.update_one(findss, setdatass)
                a = await ctx.send('룰렛을 돌렸습니다!\n과연 무엇이 당첨될까요?')
                e = await ctx.send('https://cdn.discordapp.com/emojis/809373131978309644.gif?v=1')
                await asyncio.sleep(3)
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
                        money = int(money) * 5
                        find = {"_id": str(ctx.author.id)}
                        setdata = {"$inc": {"money": int(money)}}
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
                    await a.delete()
                    await e.delete()
                    await ctx.send(f'꽝이네요. 아쉽네요.')
        else:
            await ctx.send('회원 가입이 되어있지 않아요. `!가입`으로 회원 가입을 진행해주세요!')
        

def setup(bot):
    bot.add_cog(Slot(bot))