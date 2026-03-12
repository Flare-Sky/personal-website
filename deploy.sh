#!/bin/bash

echo -e "\033[0;32m正在同步云端补丁...\033[0m"
git pull origin main --rebase

echo -e "\033[0;32m正在构建并提交到 GitHub...\033[0m"
git add .

# 自动以当前时间作为 commit 信息
msg="Update diary at $(date +'%Y-%m-%d %H:%M:%S')"
if [ -n "$1" ]; then
	msg="$1"
fi
git commit -m "$msg"

git push origin main

echo -e "\033[0;32m全部完成！请等待 GitHub Actions 部署（约 1 分钟）。\033[0m"