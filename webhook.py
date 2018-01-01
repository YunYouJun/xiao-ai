# webhook.py
import os
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    os.system('./deploy.sh')
    print('XiaoAi pull finish')