#!/bin/bash

LOG_FILE="/var/log/XiaoAi_deploy.log"
DeployPath="/root/.qqbot-tmp/plugins"

date >> "$LOG_FILE"
echo "Start deployment" >>"$LOG_FILE"
cd $DeployPath
echo "pulling source code..." >> "$LOG_FILE"
git fetch --all
git reset --hard origin/master
qq plug custom
echo "XiaoAi pull at webserver at time: $time."
echo "Finished." >>"$LOG_FILE"
echo >> $LOG_FILE