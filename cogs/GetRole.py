import discord
from discord.ext import commands
import asyncio 

class GetRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = '역할')
    async def GetRoles(self, ctx):
        m = await ctx.send(':one: 을 눌러 <@&817598594009661450> 역할을 얻으세요.\n\n:two: 를 눌러 <@&817978024700018719> 역할을 얻으세요.\n\n:three: 를 눌러 <@&817978098531172362> 역할을 얻으세요.\n\n이모지를 누르면 역할이 지급되고, 누른 것을 취소하면 역할이 제거됩니다.')
        await m.add_reaction('1️⃣')
        await m.add_reaction('2️⃣')
        await m.add_reaction('3️⃣')
    
    @commands.command(name = '청소')
    @commands.has_permissions(manage_messages=True)
    async def 청소(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount + 1)
        a = await ctx.send("메세지 " + str(amount) + "개를 삭제했습니다.")
        await asyncio.sleep(4)
        await a.delete()

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        member = payload.member
        guild = member.guild
        if member.bot:
            return

        if str(payload.emoji) == "1️⃣":
            role = guild.get_role(817598594009661450)
            await member.add_roles(role)
            await member.send('`[ User }` 역할이 지급되었습니다.')
            roles = guild.get_role(817705377646510090)
            await member.remove_roles(roles)
            

        if str(payload.emoji) == '2️⃣':
            role = guild.get_role(817978024700018719)
            await member.add_roles(role)
            await member.send('`[ 업데이트 알림 ]` 역할이 지급되었습니다.')
            
        
        if str(payload.emoji) == '3️⃣':
            role = guild.get_role(817978098531172362)
            await member.add_roles(role)
            await member.send('`[ 서버 공지 알림 ]` 역할이 지급되었습니다.')
            
    
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload: discord.RawReactionActionEvent):
        guild = self.bot.get_guild(payload.guild_id)
        m = guild.get_member(payload.user_id)

        if str(payload.emoji) == "1️⃣":
            role = guild.get_role(817598594009661450)
            await m.remove_roles(role)
            await m.send('`[ User ]` 역할을 제거했습니다.')
        
        if str(payload.emoji) == '2️⃣':
            role = guild.get_role(817978024700018719)
            await m.remove_roles(role)
            await m.send('`[ 업데이트 알림 ]` 역할을 제거했습니다.')
        
        if str(payload.emoji) == '3️⃣':
            role = guild.get_role(817978098531172362)
            await m.remove_roles(role)
            await m.send('`[ 서버 공지 알림 ]` 역할을 제거했습니다.')
    

        
        
def setup(bot):
    bot.add_cog(GetRole(bot))
