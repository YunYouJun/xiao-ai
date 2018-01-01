# -*- coding: utf-8 -*-
def onQQMessage(bot, contact, member, content):
  global StopFlag
  global count
  if content == '-hello':
    bot.SendTo(contact, '你好，我是云游酱的女朋友~')
  elif content == '-start':
    bot.SendTo(contact, '小爱启动完毕~')
    StopFlag = 0
    count = 0
  elif content == '-stop':
    bot.SendTo(contact, '小爱暂且退下啦~')
    StopFlag = 1
  elif content == '-restart':
    bot.SendTo(contact, '那小爱重启啦~')
    bot.Restart()
  elif content == '-fuck':
    bot.SendTo(contact, '那……USB接口也可以吗？')
    bot.Restart()
  elif content == 'XiaoAi-stop':
    bot.SendTo(contact, '小爱终止~')
    bot.Stop()

  if StopFlag == 0:
    if '小爱' in content and not bot.isMe(contact, member):
      if '你好' in content:
        bot.SendTo(contact, '你好，我是云游酱的女朋友~')
      elif '你是谁' in content:
        bot.SendTo(contact, '你好，我是小爱，云游酱的女朋友~')
      elif '吃' in content and '吗' in content or '吧' in content:
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
      elif '吃鸡吗' in content:
        bot.SendTo(contact, '不吃，那有啥可吃的，都是皮。')
      elif '新年快乐' in content or '元旦快乐' in content:
        bot.SendTo(contact, '你也是哦，新年快乐哟~')
      elif '云游呢' in content:
        bot.SendTo(contact, '不告诉你！')
      elif '睿神帅吗' in content or '云游帅吗' in content:
        bot.SendTo(contact, '那是当然的！')
      elif '我可爱吗' in content:
        bot.SendTo(contact, '当然可爱呀！')
      elif '你喜欢云游吗' in content:
        bot.SendTo(contact, '当然呀！')
      elif '启动自爆程序' in content:
        bot.SendTo(contact, '不听不听!')
      elif '谁最帅' in content:
        # i = int(random.random() * len(bot.List('group', '182332107')[0]))
        gm = bot.List(bot.List('group', '182332107')[0])[2]
        bot.List('group')
        bot.SendTo(contact, gm.name + '最帅！')
      else:
        count = count + 1
        if(count > 3):
          bot.SendTo(contact, '没事，别老叫我成不！')
          count = 0
        else:
          bot.SendTo(contact, '干啥呀？')

  if '睿神不在' in content or '云游不在' in content or '云游酱不在' in content or '云游君不在' in content:
    bot.SendTo(contact, '略略略')
  elif '云游的女朋友' in content:
    bot.SendTo(contact, '叫我干啥？')
  elif '不太好' in content:
    bot.SendTo(contact, '怎么不好？')


