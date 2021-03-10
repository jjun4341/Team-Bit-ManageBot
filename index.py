import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import bot

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', help_command=None, intents=intents)

startup_extensions = ['cogs.ManageMember', 'cogs.Fix', 'cogs.GetRole', 'cogs.Warn']

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('불러오기에 실패 하였습니다. 에러 파일 : {}\n에러 내용 : {}'.format(extension,exc))


@bot.event
async def on_ready():
    print('서버 관리#3443 On Ready.')
    channel = bot.get_channel(817707522617639032)
    await channel.send('서버 관리봇 상태 : <:Online:817968174103265282> \n봇이 온라인입니다.')


@bot.command(name = '리로드')
async def Reload(ctx):
    for i in startup_extensions:
        bot.reload_extension(i)
    await ctx.send('리로드를 완료했습니다.')

@bot.event
async def on_member_join(member):
    role = member.guild.get_role(817705377646510090)
    channel = bot.get_channel(817597919313526817)
    c = bot.get_channel(817704888980340737)
    cc = bot.get_channel(817971236969512991)
    await channel.send(f'{member.mention}님 **완두콩 서포트 서버**에 오신 것을 환영합니다.\n{c.mention}에서 유저 역할을 받으시면 활동이 가능하고, 다른 역할도 받을 수 있습니다.\n\n마지막으로, {cc.mention}에서 완두콩 서포트 서버의 규칙을 읽어주세요.')
    await member.add_roles(role)

bot.run('TOKEN')