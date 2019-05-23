from datetime import datetime

import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQHttpError

group = {
    'feiwu': 83765557,
    'lost_time': 102588810
}

@nonebot.scheduler.scheduled_job('cron', hour='*')
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        await bot.send_group_msg(group_id=group['lost_time'], message=f'现在{now.hour}点整啦！熬夜一时爽，一直熬夜一直爽！')
    except CQHttpError:
        pass


drink_time = 0
@nonebot.scheduler.scheduled_job('interval', minutes=10)
async def _():
    global drink_time
    drink_time += 1
    bot = nonebot.get_bot()
    # now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        await bot.send_group_msg(group_id=group['feiwu'], message=f'大家好，我是本群的“提醒喝水小助手”，这是今天的第{drink_time}轮。希望此刻看到消息的人可以和我一起来喝一杯水。10分钟后的我继续提醒大家喝水。和我一起成为一天48杯水的人吧！多喝热水。谢谢合作！')
    except CQHttpError:
        pass