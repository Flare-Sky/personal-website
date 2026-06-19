#!/bin/bash

set -e

echo -e "\033[0;34m[1/4]\033[0m \033[0;32m正在打包本地修改...\033[0m"
git add .

msg="Update diary at $(date +'%Y-%m-%d %H:%M:%S')"
if [ -n "$1" ]; then
    msg="$1"
fi
git commit -m "$msg" || echo -e "\033[0;33m没有需要提交的更改，继续执行...\033[0m"

echo -e "\033[0;34m[2/4]\033[0m \033[0;32m正在同步云端进度并进行智能合并...\033[0m"
if ! git pull origin main --rebase; then
    echo -e "\033[0;31m💥 同步失败！云端与本地代码出现冲突。\033[0m"
    echo -e "\033[0;33m请打开 VS Code 解决冲突文件后，手动执行 'git rebase --continue' 然后 push。\033[0m"
    exit 1
fi

echo -e "\033[0;34m[3/4]\033[0m \033[0;32m正在推送到 GitHub 云端...\033[0m"
git push origin main

echo -e "\033[0;34m[4/4]\033[0m \033[0;32m🎉 全部完成！请等待 GitHub Actions 部署（约 1-2 分钟）。\033[0m"