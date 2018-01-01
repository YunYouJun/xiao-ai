# webhook.py
import os
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    DeployPath = '/root/.qqbot-tmp/plugins'
    os.system('cd ' + DeployPath)
    os.system('git fetch --all')
    os.system('git reset --hard origin/master')
    os.system('qq plug custom')
    print('XiaoAi pull finish')