import discord
import asyncio
from discord.ext import commands
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
coll = client.ManageBot.user

class Warning(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.client = client
        self.coll = coll

    @commands.command(name = '경고')
    async def GivaWarning(self, ctx, user: discord.Member):
        if ctx.author.id == 443734180816486441:
            if self.coll.find_one({"_id": str(user.id)}):
                d = self.coll.find_one({"_id": str(user.id)})
                warn = d['warn']
                if warn >= 2:
                    await ctx.send(f'{str(ctx.user)}님은 경고가 3회 이상 누적되었습니다.')
                    await ctx.send(f'{str(ctx.user)}님의 역할에서 팀원 역할을 제거하려면 1️⃣을 누르고, 아니면 2️⃣를 누르세요.')
                    def check(reaction, user):
                        return user == ctx.author and str(reaction.emoji) in ['1️⃣', '2️⃣']

                    try:
                        reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                        if str(reaction.emoji) == '1️⃣':
                            for i in user.roles:
                                await i.delete()
                            role = user.guild.get_role(803175199448760341)
                            await user.add_roles(role)
                            find = {"_id": str(user.id)}
                            setdata = {"$set": {"warn": 0}}
                            self.coll.update_one(find, setdata)
                            await ctx.send('> :white_check_mark: 팀원 역할 제거와 함께, 유저 역할을 지급 완료했습니다!')
                        if str(reaction.emoji) == '2️⃣':
                            await ctx.send('경고 지급을 중단했어요.')
                    except asyncio.TimeoutError:
                        await ctx.send('시간이 초과되었어요.')
                else:
                    findd = {"_id": str(user.id)}
                    setdataaa = {"$inc": {"warn": 1}}
                    self.coll.update_one(findd, setdataaa)
                    await ctx.send('경고 지급을 완료했어요.')
            else:
                await ctx.send(f'{str(ctx.user)}님은 가입이 되어있지 않아요.')
        else:
            await ctx.send('> :no_entry_sign: 권한이 없습니다.')
    
    @commands.command(name = '경고확인')
    async def WarnCheck(self, ctx, members: discord.Member):
        if self.coll.find_one({"_id": str(members.id)}):
            aaaa = self.coll.find_one({"_id": str(members.id)})
            aaaa = aaaa['warn']
            await ctx.send(f'{str(members)}님의 경고 횟수는 {str(aaaa)}입니다!')
        else:
            await ctx.send(f'{str(members)}님은 회원가입이 되어있지 않아요!')
    
    @commands.command(name = '경고초기화')
    async def ClearWarn(self, ctx, member: discord.Member):
        if self.coll.find_one({"_id": str(member.id)}):
            user_find_data = {"_id": str(member.id)}
            set_data_user = {"$set": {"warn": 0}}
            self.coll.update_one(user_find_data, set_data_user)
            await ctx.send('경고 초기화를 완료했어요!')

def setup(bot):
    bot.add_cog(Warning(bot))