import os

# 替换规则（按顺序执行）
REPLACEMENTS = [
    ("GoPang", "ToZorro"),
    ("Pang", "Zorro"),
    ("pang", "zorro")
]


def replace_in_file(file_path):
    """替换文件内容中的关键字"""
    try:
        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 按顺序执行替换
        modified = False
        for old, new in REPLACEMENTS:
            if old in content:
                content = content.replace(old, new)
                modified = True

        # 写入修改后的内容
        if modified:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"内容已修改: {file_path}")
    except UnicodeDecodeError:
        print(f"跳过二进制文件: {file_path}")
    except Exception as e:
        print(f"处理文件失败 {file_path}: {str(e)}")


def rename_file_or_dir(path):
    """重命名文件/目录"""
    dirname, basename = os.path.split(path)

    # 按顺序执行替换
    new_basename = basename
    for old, new in REPLACEMENTS:
        new_basename = new_basename.replace(old, new)

    # 执行重命名
    if new_basename != basename:
        new_path = os.path.join(dirname, new_basename)
        try:
            os.rename(path, new_path)
            print(f"重命名: {path} -> {new_path}")
            return new_path  # 返回新路径用于后续处理
        except Exception as e:
            print(f"重命名失败 {path}: {str(e)}")
    return path


def process_directory(root_dir):
    """递归处理目录"""
    # 先处理深层目录（topdown=False保证从底层开始）
    for root, dirs, files in os.walk(root_dir, topdown=False):
        # 处理文件内容
        for name in files:
            file_path = os.path.join(root, name)
            replace_in_file(file_path)

        # 处理目录和文件名
        for name in files + dirs:
            old_path = os.path.join(root, name)
            new_path = rename_file_or_dir(old_path)

            # 如果路径改变，更新后续处理路径
            if new_path != old_path and os.path.isdir(new_path):
                process_directory(new_path)  # 重新处理新目录


# 实现修改对应文件夹及子文件夹，文件名称及文件内容中关键字，按照顺序匹配，并替换成新的关键字，区分大小写
if __name__ == "__main__":
    target_dir = input("请输入要处理的目录路径:").strip()

    if os.path.isdir(target_dir):
        process_directory(target_dir)
        print("操作完成！")
    else:
        print("无效的目录路径")
