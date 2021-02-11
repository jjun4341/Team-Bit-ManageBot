import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import bot

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = '도움말', aliases = ['도움', '명령어', 'help', 'H', 'HELP', 'Help'])
    async def Help(self, ctx):
        embed = discord.Embed(title = 'Team. Bit 관리봇 명령어', description = ' ', color=0x00FFFF, inline=False)
        embed.add_field(name = '> `!킥 @유저멘션 사유`', value = '멘션한 유저를 서버에서 추방합니다.', inline=False)
        embed.add_field(name = '> `!밴 @유저멘션 사유`', value = '멘션한 유저를 서버에서 밴합니다.', inline=False)
        embed.add_field(name = '> `!뮤트 @유저멘션 사유`', value = '멘션한 유저를 뮤트합니다.', inline=False)
        embed.add_field(name = '> `!뮤트해제 @유저멘션`', value = '멘션한 유저를 뮤트 해제합니다.', inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))