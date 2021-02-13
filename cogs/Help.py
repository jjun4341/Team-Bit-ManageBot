import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import bot

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = '도움말', aliases = ['도움', '명령어', 'help', 'H', 'HELP', 'Help'])
    async def Help(self, ctx):
        command_name = ['!뮤트 @유저-멘션', '!뮤트해제 @유저-멘션', '!킥 @유저-멘션', '!밴 @유저-멘션', '!일', '!도박 <도박-금액>', '!내돈']
        command_usage = ['멘션한 유저를 뮤트합니다.', '멘션한 유저를 뮤트 해제합니다.', '멘션한 유저를 추방합니다.', '멘션한 유저를 밴 합니다.', '일을 하여 돈을 법니다.', '도박 금액만큼 슬롯머신으로 도박을합니다.', '자신의 돈을 확인합니다.']
        command_example = ['!뮤트 @땅콩', '!뮤트해제 @땅콩', '!킥 @땅콩', '!밴 @땅콩', '!일', '!도박 5000', '!내돈']
        embed = discord.Embed(title = '길드 - 도움말', description = ' ', color=0x00FFFF, inline=False)
        for i in command_name:
            embed.add_field(name = f'> `{i}`', value = '\n' + str(command_usage[0]) + '\n사용 예시 : ' + str(command_example[0]), inline=False)
            del command_usage[0]
            del command_example[0]
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))