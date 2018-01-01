# -*- coding: utf-8 -*-

def onQQMessage(bot, contact, member, content):
  if content == '-hello':
    bot.SendTo(contact, '你好，我是云游酱的女朋友~')
  elif content == '-start':
    bot.SendTo(contact, '小爱启动完毕~')
    stop = 0
  elif content == '-stop':
    bot.SendTo(contact, '小爱暂且退下啦~')
    stop = 1
  elif content == '-restart':
    bot.SendTo(contact, '那小爱重启啦~')
    bot.Restart()
  elif content == 'XiaoAi-stop':
    bot.SendTo(contact, '小爱终止~')
    bot.Stop()

  if stop = 0
    if '小爱' in content and not bot.isMe(contact, member) :
      if '你好' in content:
        bot.SendTo(contact, '你好，我是云游酱的女朋友~')
      elif '你是谁' in content:
        bot.SendTo(contact, '你好，我是小爱，云游酱的女朋友~')
      elif '智障' in content:
        bot.SendTo(contact, '你才智障！')
      elif '吃鸡吗' in content:
        bot.SendTo(contact, '不吃，那有啥可吃的，都是皮。')
      elif '新年快乐' in content or '元旦快乐' in content:
        bot.SendTo(contact, '你也是哦，新年快乐哟~')
      elif '云游呢' in content:
        bot.SendTo(contact, '不告诉你！')
      elif '我可爱吗' in content:
        bot.SendTo(contact, '当然可爱呀！')
      elif '你喜欢云游吗' in content:
        bot.SendTo(contact, '当然呀！')
      elif '启动自爆程序' in content:
        bot.SendTo(contact, '不听不听!')
      else:
        bot.SendTo(contact, '干啥呀？')

    if '睿神不在' in content or '云游不在' in content or '云游酱不在' in content or '云游君不在' in content:
        bot.SendTo(contact, '略略略')
    elif '云游的女朋友' in content:
        bot.SendTo(contact, '叫我干啥？')
    elif '不太好' in content:
      bot.SendTo(contact, '怎么不好？')
