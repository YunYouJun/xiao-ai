cd /home/yunyou/
docker run -ti --rm --name cqhttp-xiaoai \
            -v $(pwd)/coolq:/home/user/coolq \
            -p 9000:9000 \
            -p 5700:5700 \
            -e COOLQ_ACCOUNT=996955042 \
            -e CQHTTP_SERVE_DATA_FILES=yes \
            -e VNC_PASSWD=MAX8char \
            -e CQHTTP_USE_WS_REVERSE=true \
            -e CQHTTP_WS_REVERSE_API_URL=ws://172.17.0.1:9969/ws/api/ \
            -e CQHTTP_WS_REVERSE_EVENT_URL=ws://172.17.0.1:9969/ws/event/ \
            richardchien/cqhttp:latest