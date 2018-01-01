# webhook.py
import os
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    DeployPath = '/root/.qqbot-tmp/plugins'
    os.system('cd ' + DeployPath)
    os.system('git reset --hard')
    os.system('git pull')
    os.system('qq plug custom')
    print('XiaoAi pull finish')