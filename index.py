import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import bot

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', help_command=None, intents=intents)

startup_extensions = ['cogs.Kick', 'cogs.Help', 'cogs.Money', 'cogs.Join', 'cogs.Slot', 'cogs.Warn']

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('불러오기에 실패 하였습니다. 에러 파일 : {}\n에러 내용 : {}'.format(extension,exc))

@bot.event
async def on_ready():
    print(f'Client is Ready\n봇 이름 : {bot.user.name}\n봇 아이디 : {bot.user.id}')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('!도움말'))


@bot.command(name = '리로드', aliases = ['ㄹ', 'f'])
async def Reload(ctx):
    for extension in startup_extensions:
        bot.reload_extension(extension)
    await ctx.send('> :white_check_mark: 리로드를 완료했어요!')
    
@bot.event
async def on_member_join(member): 
    channel = bot.get_channel(788296617731555381)
    role = member.guild.get_role(803175199448760341)
    bot_role = member.guild.get_role(789747876917674015)
    if member.bot:
        await member.add_roles(bot_role)
        await channel.send(f'{member.mention} 봇이 **Team. Bit** 서버에 입장했습니다!')
    else:
        await member.add_roles(role)
        await channel.send(f'{member.mention}님 **Team. Bit** 서버에 오신 것을 진심으로 환영합니다!\n#🎄ㅣ필독규칙 채널 한 번 읽어주세요!')

bot.run('')