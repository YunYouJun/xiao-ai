# coding=utf-8
# webhook.py
import os
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    DeployPath = '/home/yunyou/github/xiao-ai/'
    os.system('cd ' + DeployPath)
    os.system('git pull --force')
    print('xiao-ai pull finish')
    os.system('screen -S xiaoai -X quit')
    os.system('screen -S xiaoai')
    os.system('python3 bot.py')
    print('xiao-ai restart!')
    return [b'Hello, XiaoAi!']