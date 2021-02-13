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

    @commands.cooldown(1, 30, commands.BucketType.user)
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
    
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f'해당 명령어는 `{round(error.retry_after, 2)}`초 뒤에 사용하실 수 있습니다.')

                

def setup(bot):
    bot.add_cog(Money(bot))