import re
import os

# --- 配置区 ---
directory = "content/posts"  # 你的日记存放路径
start_num = 71
end_num = 79
# --------------

def transform_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. 拆分 Front Matter 和 正文
    # 匹配 +++ ... +++ 之间的内容
    parts = re.split(r'(\+\+\+[\s\S]*?\+\+\+)', content)
    if len(parts) < 3:
        return # 跳过非 Hugo 格式文件

    front_matter = parts[1]
    body = parts[2]

    # 2. 解析正文行
    lines = body.strip().split('\n')
    table_rows = []
    notes = []
    
    # 正则：匹配 0:00-8:00 这种格式开头
    time_pattern = re.compile(r'^(\d{1,2}:\d{2}-\d{1,2}:\d{2})\s+(.*)')

    for line in lines:
        match = time_pattern.match(line.strip())
        if match:
            time_range = match.group(1)
            activity = match.group(2)
            table_rows.append(f"|{time_range}|{activity}|")
        else:
            # 如果不是时间行，且我们已经收集了表格，或者这行本身不是空的，就存入注释
            if line.strip() or table_rows:
                notes.append(line)

    # 3. 重新组装内容
    # 构造 Markdown 表格（无标题格式）
    table_header = "| | |\n|---|---|"
    table_content = "\n".join(table_rows)
    
    # 过滤掉注释部分开头的空行
    final_notes = "\n".join(notes).strip()

    new_content = f"{front_matter}\n\n{table_header}\n{table_content}\n\n{final_notes}\n"

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"✅ 已转换: {os.path.basename(file_path)}")

# 循环处理指定的编号
for i in range(start_num, end_num + 1):
    file_name = f"diary-{str(i).zfill(3)}.md"
    file_path = os.path.join(directory, file_name)
    
    if os.path.exists(file_path):
        transform_file(file_path)
    else:
        print(f"❌ 未找到文件: {file_name}")

print("\n所有转换任务已完成！")