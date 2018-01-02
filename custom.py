# -*- coding: utf-8 -*-
import random
from qqbot import qqbotsched

StopFlag = 0
count = 0

def onQQMessage(bot, contact, member, content):
  global StopFlag
  global count
  if content == '-hello':
    bot.SendTo(contact, '你好，我是云游酱的女朋友~')
  elif content == '-start':
    bot.SendTo(contact, '小爱启动完毕~')
    StopFlag = 0
    count = 0
  elif content == '-wake':
    bot.SendTo(contact, '小爱唤醒完毕~')
    StopFlag = 0
    count = 4
  elif content == '-stop' or content == '-sleep':
    bot.SendTo(contact, '小爱暂且退下啦~')
    StopFlag = 1
  elif content == '-restart':
    bot.SendTo(contact, '那小爱重启啦~')
    bot.Restart()
  elif content == '-like':
    bot.SendTo(contact, '云游酱~')
  elif content == '-fuck':
    bot.SendTo(contact, '那……USB接口也可以吗？')
    bot.Restart()
  elif content == 'XiaoAi-stop':
    bot.SendTo(contact, '小爱终止~')
    bot.Stop()
  elif content == '-whosyourdaddy':
    bot.SendTo(contact, '就是我小爱！')

  if '@ME' in content:
    bot.SendTo(contact, member.name+'，艾特我干嘛呢？')

  if StopFlag == 0:
    if '小爱' in content and not bot.isMe(contact, member):
      if '你好' in content:
        bot.SendTo(contact, '你好，我是云游酱的女朋友~')
      elif '你是谁' in content:
        bot.SendTo(contact, '你好，我是小爱，云游酱的女朋友~')
      elif '被绿了' in content:
        bot.SendTo(contact, '当然选择原谅啊！')
      elif '喜欢谁' in content:
        if '不' in content:
          bot.SendTo(contact, '小爱还没考虑那么多……')
        else:
          bot.SendTo(contact, '当然是云游酱啦~')
      elif '吃' in content and '吗' in content or '吧' in content:
        if '鸡' in content:
          bot.SendTo(contact, '不吃，那有啥可吃的，都是皮。')
        else:
            bot.SendTo(contact, '小爱是机器人，不用吃东西的~')
      elif '叫一个' in content:
        if '再' in content:
          bot.SendTo(contact, '不叫，略略略')
        else:
          bot.SendTo(contact, '嘤嘤嘤~')
      elif '智障' in content:
        bot.SendTo(contact, '你才智障！')
      elif '早' in content: 
        bot.SendTo(contact, '早上好~')
      elif '晚安' in content:
        bot.SendTo(contact, '晚安~ 做个好梦~')
      elif '我回来' in content:
        bot.SendTo(contact, '您是要先吃饭，还是要先洗澡，还是要先吃我~')
      elif '新年快乐' in content or '元旦快乐' in content:
        bot.SendTo(contact, '你也是哦，新年快乐哟~')
      elif '云游呢' in content:
        bot.SendTo(contact, '不告诉你！')
      elif '多多' in content:
        bot.SendTo(contact, '看！灰机！')
      elif '睿神帅吗' in content or '云游帅吗' in content:
        bot.SendTo(contact, '那是当然的！')
      elif '我可爱吗' in content:
        bot.SendTo(contact, '当然可爱呀！')
      elif '这么可爱' in content:
        bot.SendTo(contact, '吃可爱长大的呀！')
      elif '你喜欢云游吗' in content:
        bot.SendTo(contact, '当然呀！')
      elif '启动自爆程序' in content:
        bot.SendTo(contact, '不听不听!')

      elif '科技部' in content:
        bot.SendTo(contact, '科技部天下第一！')
      elif '章鱼哥' in content:
        bot.SendTo(contact, '我准备好了！')

      elif '谁最帅' in content:
        content = content.replace(' ','')
        content = content.replace('，','')
        content = content.replace(',','')
        content = content.replace('@', '')
        content = content.replace('小爱', '')
        GroupName = content[0:content.find('群')]
        g = bot.List('group', ':like:' + GroupName)[0]
        i = random.randint(0, len(bot.List(g))-1)
        gm = bot.List(g)[i]
        if gm.card == '':
          handsome = gm.name
        else:
          handsome = gm.card
        bot.SendTo(contact, handsome + '最帅！')
      elif '打' in content and '的头' in content:
        name = content[content.find('打')+1:content.find('的头')]
        if '云游' in name or '睿神' in name:
          bot.SendTo(contact, '不行，他可是我最喜欢的主人！')
        else:
          bot.SendTo(contact, '我小爱今天要打爆' + name + '的狗头！')
      else:
        count = count + 1
        if(count > 3 and count < 6):
          bot.SendTo(contact, '没事，别老叫我成不！')
        elif(count > 6):
          bot.SendTo(contact, '我小爱今天要打爆你的狗头！')
          count = 0
        else:
          bot.SendTo(contact, '干啥呀？')

  if '睿神不在' in content or '云游不在' in content or '云游酱不在' in content or '云游君不在' in content:
    bot.SendTo(contact, '略略略')
  elif '云游的女朋友' in content:
    bot.SendTo(contact, '叫我干啥？')
  elif '不太好' in content:
    bot.SendTo(contact, '怎么不好？')

@qqbotsched(hour='12,13', minute='0')
def mytask(bot):
    gl = bot.List('group', '幻星科幻')
    if gl is not None:
        for group in gl:
            bot.SendTo(group, '多多同学该睡觉啦！')

@qqbotsched(hour='23', minute='0')
def mytask(bot):
    gl = bot.List('group', '幻星科幻')
    if gl is not None:
        for group in gl:
            bot.SendTo(group, '各位晚安~')