# coding=utf-8
# webhook.py
import os
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    DeployPath = '/root/github/xiao-ai'
    os.system('cd ' + DeployPath)
    os.system('git pull --force')
    print('xiao-ai pull finish')
    return [b'Hello, XiaoAi!']