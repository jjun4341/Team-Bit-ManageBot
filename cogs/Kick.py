import discord
import asyncio
from discord.ext import commands

class Kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = '킥')
    async def KickMember(self, ctx, user: discord.Member, *, reason: str):
        if ctx.author.id == 443734180816486441:
            await user.kick(reason=reason)
            await ctx.send(f'{user} 님은 Team. Bit 서버에서 추방 당하셨습니다.\n사유 : {reason}')
            try:
                await user.send(f'{user} 님은 Team. Bit 서버에서 추방 당하셨습니다.\n사유 : {reason}')
            except Exception as e:
                await ctx.send(f'에러 발생 : {e}')
        else:
            await ctx.send(f'{ctx.author.mention}님은 권한이 없습니다.')
    
    @commands.command(name = '밴')
    async def BanMember(self, ctx, user: discord.Member, *, reason: str):
        if ctx.author.id == 443734180816486441:
            await user.ban(reason=reason)
            await ctx.send(f'{user} 님은 Team. Bit 서버에서 밴 당하셨습니다.\n사유 : {reason}')
            try:
                await user.send(f'{user} 님은 Team. Bit 서버에서 밴 당하셨습니다.\n사유 : {reason}')
            except Exception as e:
                await ctx.send(f'에러 발생 : {e}')
        else:
            await ctx.send(f'{ctx.author.mention}님은 권한이 없습니다.')
    
    @commands.command(name = '뮤트')
    async def MuteMember(self, ctx, user: discord.Member, *, reason: str):
        if ctx.author.id == 443734180816486441:
            roles = ctx.guild.get_role(798509528136024064)
            if roles in user.roles:
                await ctx.send(f'`{user}`님은 이미 뮤트 상태에요!')
            else:
                await user.add_roles(roles)
                channel = self.bot.get_channel(800925530126811166)
                embed = discord.Embed(title = f'{user} - 뮤트', description = ' ', colour = 0xff0000)
                embed.add_field(name = '뮤트 사유', value = f'{reason}')
                await channel.send(embed=embed)
        else:
            await ctx.send(f'{ctx.author.mention}님은 권한이 없습니다.')
    
    @commands.command(name = '뮤트해제')
    async def UnMuteMember(self, ctx, userss: discord.Member):
        if ctx.author.id == 443734180816486441:
            roles = ctx.guild.get_role(798509528136024064)
            if roles not in userss.roles:
                await ctx.send(f'`{userss}`님은 뮤트 상태가 아니에요!')
            else:
                await userss.remove_roles(roles)
                channel = self.bot.get_channel(800925530126811166)
                embed = discord.Embed(title = f'{userss} - 뮤트 해제', description = ' ', colour = 0x00FFFF)
                await channel.send(embed=embed)
        else:
            await ctx.send(f'{ctx.author.mention}님은 권한이 없습니다.')


def setup(bot):
    bot.add_cog(Kick(bot))