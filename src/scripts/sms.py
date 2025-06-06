def process():
    # 打开输入文件并读取内容
    with open('../inputs/bd_sms.txt', 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    # 打开输出文件以写入内容
    with open('../outputs/bd_sms.txt', 'w', encoding='utf-8') as outfile:
        for line in lines:
            # 去除每行末尾的换行符（如果有）
            line = line.strip()
            # 将内容格式化为 "%1$s",
            formatted_line = f'"{line}",\n'
            # 写入输出文件
            outfile.write(formatted_line)
    print("内容已成功写入outputs/bd_sms文件。")


if __name__ == '__main__':
    process()
