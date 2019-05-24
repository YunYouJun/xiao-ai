# coding=utf-8
# webhook.py
import os
import signal
import time

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    DeployPath = '/home/yunyou/github/xiao-ai/'
    os.system('cd ' + DeployPath)
    os.system('git pull --force')
    print('xiao-ai pull finish')
    stopXiaoAi()
    time.sleep(10)
    startXiaoAi()
    return [b'Hello, XiaoAi!']

def startXiaoAi():
    os.system('nohup python3 bot.py &')
    print('xiao-ai start!')


def stopXiaoAi():
    list = os.popen("ps -ef|grep python3|grep bot.py|grep -v grep|awk '{print $2}'").readlines()
    for pid in list:
        os.kill(int(pid),signal.SIGKILL)
