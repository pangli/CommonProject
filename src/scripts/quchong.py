# 内容去重
# 定义文件路径
from collections import OrderedDict

file_path = '../outputs/queries_packages.txt'


def deduplicated():
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 对每行内容去除开头空格和末尾换行符
    unique_lines = []
    for line in lines:
        unique_lines.append(line.strip())
    # 创建一个有序且不重复的集合
    ordered_set = OrderedDict.fromkeys(unique_lines)
    # 转换为列表以便查看结果
    ordered_set_list = list(ordered_set.keys())
    # 将去重后的内容写回文件或输出
    # 写回文件
    with open('../outputs/queries_packages_deduplicated.txt', 'w', encoding='utf-8') as file:
        for line in ordered_set_list:
            file.write(line + '\n')
    print("内容已成功写入outputs/queries_packages_deduplicated文件。")
    # 或者输出到控制台
    # for line in unique_lines:
    #     print(line)


if __name__ == '__main__':
    deduplicated()
