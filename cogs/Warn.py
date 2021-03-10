import discord
from discord.ext import commands
from pymongo import MongoClient
import asyncio

client = MongoClient('mongodb://localhost:27017/')
coll = client.sm.user

class Warning(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.client = client
        self.coll = coll

    @commands.command(name = '제재내역')
    async def my_warning(self, ctx):
        if self.coll.find_one({"_id": str(ctx.author.id)}):
            d = self.coll.find_one({"_id": str(ctx.author.id)})
            dddd = str(d['warn'])
            if d['reason']['one'] == None:
                embed = discord.Embed(title = f'{str(ctx.author)} 님의 제재내역', description = f'경고 누적 횟수 : 없음', color = 0x00FFFF, inline=False)
                await ctx.send(embed=embed)

            elif d['reason']['one'] != None and d['reason']['two'] == None:
                r2 = d['reason']['one']
                embed = discord.Embed(title = f'{str(ctx.author)} 님의 제재내역', description = f'경고 누적 횟수 : 1회\n사유 : {r2}\n\n현재 경고 횟수 : {dddd}', color = 0x00FFFF, inline=False)
                await ctx.send(embed=embed)

            elif d['reason']['one'] != None and d['reason']['two'] != None and d['reason']['three'] == None:
                r2 = d['reason']['two']
                r3 = d['reason']['three']
                embed = discord.Embed(title = f'{str(ctx.author)} 님의 제재내역', description = f'경고 누적 횟수 : 2회\n경고 1회 사유 : {r2}\n경고 2회 사유 : {r3}\n곧 경고가 3회 누적됩니다. 경고 3회 누적 시 서버에서 추방을 당하실 수 있습니다.\n주의해주세요!\n\n현재 경고 횟수 : {dddd}', color = 0x00FFFF, inline=False)
                await ctx.send(embed=embed)

        else:
            self.coll.insert_one({
                "_id": str(ctx.author.id),
                "warn": 0,
                "reason": [None, None, None]
                })
            await ctx.send(f'{ctx.author.mention} 님의 정보를 데이터베이스에 등록했습니다.')
    @commands.group(name = '경고')
    async def warn(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('none')
    
    @warn.command(name = '추가')
    async def WarnAdd(self, ctx, user: discord.Member, *, reason: str):
        role = discord.utils.find(lambda r: r.name == '[ Bot Developer ]', ctx.guild.roles)
        if role in ctx.author.roles:
            if self.coll.find_one({"_id": str(user.id)}):
                dd = self.coll.find_one({"_id": str(ctx.author.id)})

                if dd['reason']['one'] == None:
                    find = {"_id": str(user.id)}
                    setdata = {"$inc": {"warn": 1}}
                    self.coll.update_one(find, setdata)
                    setdata = {"$set": {"reason.one": str(reason)}}
                    self.coll.update_one(find, setdata)

                    d = self.coll.find_one({"_id": str(ctx.author.id)})
                    warning_count = str(d['warn'])

                    embed = discord.Embed(title = f'{str(user)} 님의 경고 횟수', description = f'경고 누적 횟수 : {warning_count}')
                    await ctx.send(embed=embed)

                    ch = self.bot.get_channel(817964393437462560)
                    embed = discord.Embed(title = f'{str(user)} - 경고', description = f'사유 : {reason}', color = 0xff0000, inline=False)
                    await ch.send(embed=embed)

                elif dd['reason']['one'] != None and dd['reason']['two'] == None:
                    find = {"_id": str(user.id)}
                    setdata = {"$inc": {"warn": 1}}
                    self.coll.update_one(find, setdata)
                    setdata = {"$set": {"reason.two": str(reason)}}
                    self.coll.update_one(find, setdata)

                    d = self.coll.find_one({"_id": str(ctx.author.id)})
                    warning_count = str(d['warn'])

                    embed = discord.Embed(title = f'{str(user)} 님의 경고 횟수', description = f'경고 누적 횟수 : {warning_count}')
                    await ctx.send(embed=embed)

                    ch = self.bot.get_channel(817964393437462560)
                    embed = discord.Embed(title = f'{str(user)} - 경고', description = f'사유 : {reason}', color = 0xff0000, inline=False)
                    await ch.send(embed=embed)
                
                elif dd['reason']['one'] != None and dd['reason']['two'] != None and dd['reason']['three'] == None:
                    find = {"_id": str(user.id)}
                    setdata = {"$inc": {"warn": 1}}
                    self.coll.update_one(find, setdata)
                    setdata = {"$set": {"reason.three": str(reason)}}
                    self.coll.update_one(find, setdata)
                    d = self.coll.find_one({"_id": str(ctx.author.id)})
                    warning_count = str(d['warn'])

                    embed = discord.Embed(title = f'{str(user)} 님의 경고 횟수', description = f'경고 누적 횟수 : {warning_count}')
                    await ctx.send(embed=embed)

                    ch = self.bot.get_channel(817964393437462560)
                    embed = discord.Embed(title = f'{str(user)} - 경고', description = f'사유 : {reason}', color = 0xff0000, inline=False)
                    await ch.send(embed=embed)
            else:
                await ctx.send(str(user) + '님의 정보가 데이터베이스에 등록되어 있지 않습니다.')
                self.coll.insert_one({
                "_id": str(ctx.author.id),
                "warn": 0,
                "reason": {
                    "one": None,
                    "two": None,
                    "three": None,
                    "four": None
                    }
                    })
                await ctx.send(str(user) + '님의 정보를 데이터베이스에 등록했습니다.')

                find = {"_id": str(user.id)}
                setdata = {"$inc": {"warn": 1, "reason.one": str(reason)}}
                self.coll.update_one(find, setdata)

                d = self.coll.find_one({"_id": str(ctx.author.id)})

                warning_count = str(d['warn'])
                embed = discord.Embed(title = f'{str(user)} 님의 제재내역', description = f'경고 누적 횟수 : {warning_count}')
                await ctx.send(embed=embed)
                ch = self.bot.get_channel(817964393437462560)
                embed = discord.Embed(title = f'{str(user)} - 경고', description = f'사유 : {reason}', color = 0xff0000, inline=False)
                await ch.send(embed=embed)
        else:
            await ctx.send(f'{ctx.author.mention}, 권한이 부족합니다.')
    
    @warn.command(name = '차감')
    async def Remove_Warn(self, ctx, user: discord.Member):
        if self.coll.find_one({"_id": str(user.id)}):
            msg = await ctx.send(f'정말로 {user} 님의 경고를 차감하시겠습니까?')
            await msg.add_reaction('⭕')
            await msg.add_reaction('❌')
            
            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) == '⭕'

            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                find = {"_id": str(user.id)}
                setdata = {"$inc": {"warn": -1}}
                self.coll.update_one(find, setdata)
                dd = self.coll.find_one({"_id": str(user.id)})
                warnning_count = dd['warn']
                await ctx.send(f'경고 1회 차감이 완료되었습니다.\n{user} 님의 누적 경고 횟수 : {str(warnning_count)}')
            except asyncio.TimeoutError:
                await ctx.send('시간이 초과되었습니다.')
        else:
            await ctx.send(f'{user} 님은 회원가입이 되어있지 않습니다.')
            self.coll.insert_one({
                "_id": str(ctx.author.id),
                "warn": 0,
                "reason": {
                    "one": None,
                    "two": None,
                    "three": None,
                    "four": None
                }
                })
            await ctx.send(f'{user} 님의 정보를 데이터베이스에 등록했습니다.')
                
    
    
def setup(bot):
    bot.add_cog(Warning(bot))