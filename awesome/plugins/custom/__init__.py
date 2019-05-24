
from nonebot import on_command, CommandSession

@on_command('master', aliases=('主人'))
async def weather(session: CommandSession):
    master_report = '当然是云游大人！'
    await session.send(master_report)