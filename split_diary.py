import re
import os

# --- 配置区 ---
input_file = "all_diaries.txt"   # 你的原始日记文件名
output_dir = "content/posts"     # 输出到 Hugo 的文章目录
year = "2026"                    # 设置日记年份
# --------------

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

with open(input_file, "r", encoding="utf-8") as f:
    content = f.read()

# 正则表达式：匹配数字行，紧接着匹配括号里的日期
# 格式：数字 \n （月.日）
pattern = r"(\d+)\n（(\d+)\.(\d+)）([\s\S]+?)(?=\n\d+\n（|$)"

entries = re.findall(pattern, content)

for index, month, day, text in entries:
    # 格式化日期和文件名
    date_str = f"{year}-{month.zfill(2)}-{day.zfill(2)}"
    file_name = f"diary-{index.zfill(3)}.md"
    file_path = os.path.join(output_dir, file_name)
    
    # 构造 TOML Front Matter
    hugo_content = f"""+++
title = "寄居者的日记-{index}"
date = {date_str}T12:00:00-05:00
draft = false
categories = ["寄居者的日记"]
tags = ["朗维尤"]
+++

{text.strip()}
"""
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(hugo_content)
    print(f"已生成: {file_name}")

print(f"\n成功！共处理 {len(entries)} 篇日记。")