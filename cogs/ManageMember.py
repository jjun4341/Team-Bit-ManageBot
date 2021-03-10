import discord
from discord.ext import commands
import asyncio 

class ManageMember(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = '추방')
    async def kick_member(self, ctx, user: discord.Member, *, reason=None):
        if user == None or reason == None:
            await ctx.send(f'{ctx.author.mention}, 올바른 사용법은 `!추방 @유저멘션 사유` 입니다.')
        if ctx.author.id == 443734180816486441:
            try:
                await user.kick
                await ctx.send(f'{str(user)} 님을 밴하였습니다.')
                user = await user.create_dm()
                await user.send(f'{user.mention}님은 `완두콩 서포트 서버` 에서 추방되셨습니다\n사유 : {reason}')
                await ctx.send(f'{str(user)} 님에게 DM 전송을 완료했습니다.')

            except Exception as e:
                await ctx.send(f'에러 발생 : {e}')
        else:
            await ctx.send(f'{ctx.author.mention}, 권한이 부족합니다.')
    
    @commands.command(name = '밴')
    async def ban_member(self, ctx, user: discord.Member, *, reason=None):
        if user == None or reason == None:
            await ctx.send(f'{ctx.author.mention}, 올바른 사용법은 `!밴 @유저멘션 사유` 입니다.')
        if ctx.author.id == 443734180816486441:
            try:
                await user.ban(reason=reason)
                await ctx.send(f'{str(user)} 님을 밴하였습니다.')
                user = await user.create_dm()
                await user.send(f'{user.mention}님은 `완두콩 서포트 서버` 에서 추방되셨습니다\n사유 : {reason}')
                await ctx.send(f'{str(user)} 님에게 DM 전송을 완료했습니다.')

            except Exception as e:
                await ctx.send(f'에러 발생 : {e}')
        else:
            await ctx.send(f'{ctx.author.mention}, 권한이 부족합니다.')
    
    @commands.command(name = '뮤트')
    async def MuteMember(self, ctx, user: discord.Member, time: int, *, reason=None):
        if ctx.author.id == 443734180816486441:
            if reason == None:
                await ctx.send(f'{ctx.author.mention}, 올바른 사용법은 `!뮤트 @유저멘션 사유` 입니다.')
            roles = ctx.guild.get_role(817963983352102922)
            if roles in user.roles:
                await ctx.send(f'`{user}`님은 이미 뮤트 상태입니다.')
            else:
                await user.add_roles(roles)
                channel = self.bot.get_channel(817964393437462560)
                embed = discord.Embed(title = f'{user} - 뮤트', description = ' ', colour = 0xff0000)
                embed.add_field(name = '뮤트 사유', value = f'{reason}')
                await channel.send(embed=embed)
                await user.send(f'완두콩 서포트 서버에서 뮤트를 당하셨습니다.\n시간 : {time * 60}분\n사유 : {reason} ')
                await asyncio.sleep(time * 60)
                await user.remove_roles(roles)
        else:
            await ctx.send(f'{ctx.author.mention}, 권한이 부족합니다.')
    
    @commands.command(name = '뮤트해제')
    async def UnMuteMember(self, ctx, userss: discord.Member):
        if ctx.author.id == 443734180816486441:
            roles = ctx.guild.get_role(817963983352102922)
            if roles not in userss.roles:
                await ctx.send(f'`{userss}`님은 뮤트 상태가 아닙니다.')
            else:
                await userss.remove_roles(roles)
                channel = self.bot.get_channel(817964393437462560)
                embed = discord.Embed(title = f'{userss} - 뮤트 해제', description = ' ', colour = 0x00FFFF)
                await channel.send(embed=embed)
        else:
            await ctx.send(f'{ctx.author.mention}, 권한이 부족합니다.')
    
def setup(bot):
    bot.add_cog(ManageMember(bot))
    print('ManageMember On Ready.')