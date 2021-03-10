import discord
from discord.ext import commands

class Fix(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = '점검안내', aliases=['점검', 'fix'])
    async def Fixs(self, ctx):
        if ctx.author.id == 443734180816486441:
            channel = self.bot.get_channel(817706941311614986)
            await channel.send('서버 관리봇 상태 : <:Ofline:817968174275756052> \n봇 점검이 시작됩니다.')
        else:
            await ctx.send(f'{ctx.author.mention}, 권한이 부족합니다.')
    
    @commands.command(name = '리부팅', aliases=['리붓', '재부팅', 'reboot'])
    async def Reboot(self,ctx):
        if ctx.author.id == 443734180816486441:
            channel = self.bot.get_channel(817706941311614986)
            await channel.send('서버 관리봇 상태 : <:Ofline:817968174275756052> \n봇 재시작을 진행합니다.')
        else:
            await ctx.send(f'{ctx.author.mention}, 권한이 부족합니다.')
    
def setup(bot):
    bot.add_cog(Fix(bot))
