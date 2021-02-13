import discord
import asyncio
from discord.ext import commands
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
coll = client.ManageBot.user

class Join(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.client = client
        self.coll = coll

    @commands.command(name = '가입')
    async def JoinSystem(self, ctx):
        if self.coll.find_one({"_id": str(ctx.author.id)}):
            await ctx.send('앗! 이미 가입이 되어있어요!')
        else:
            self.coll.insert_one({"_id": str(ctx.author.id), "money": 0, "warn": 0})
            await ctx.send('> :white_check_mark: 가입이 완료되었어요!')
    
    @commands.command(name = '탈퇴')
    async def LeaveSystem(self, ctx):
        await ctx.send('정말로 탈퇴하시겠습니까?')
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ['⭕', '❌']

        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
            if str(reaction.emoji) == '⭕':
                self.coll.delete_one({"_id": str(ctx.author.id)})
                await ctx.send('탈퇴가 완료되었어요.')
            if str(reaction.emoji) == '❌':
                await ctx.send('탈퇴를 취소했어요.')
        except asyncio.TimeoutError:
            await ctx.send('시간이 초과되었어요.')

def setup(bot):
    bot.add_cog(Join(bot))