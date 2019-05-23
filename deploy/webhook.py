# coding=utf-8
# webhook.py
import os
screen_name = 'xiaoai'
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    DeployPath = '/home/yunyou/github/xiao-ai/'
    os.system('cd ' + DeployPath)
    os.system('git pull --force')
    print('xiao-ai pull finish')
    os.system(f'screen -X -S {screen_name} quit')
    os.system(f'screen -S {screen_name}')
    os.system('python3 bot.py')
    os.system(f'screen -d {screen_name}')
    print('xiao-ai restart!')
    return [b'Hello, XiaoAi!']