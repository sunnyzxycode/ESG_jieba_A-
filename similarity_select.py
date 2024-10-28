# 读取文件并寻找相同部分
def read_file(file_path):
    """读取文件内容并以'、'进行分割"""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    # 使用'、'进行分割，去除空白字符
    return set(content.split('、'))


def find_common_parts(file1, file2):
    content1 = set(read_file(file1))
    content2 = set(read_file(file2))

    common_parts = content1.intersection(content2)

    return common_parts


def find_differ_parts(file1, file2):
    content1 = set(read_file(file1))
    content2 = set(read_file(file2))

    common_parts = content1.intersection(content2)
    # 找到去重后的部分（并集减去交集）
    # unique_content1 = content1 - common_parts
    unique_content2 = content2 - common_parts

    return unique_content2



# 文件路径
file1_path = r"C:\Users\zxy\OneDrive\桌面\气候转型风险.txt"
file2_path = r"C:\Users\zxy\OneDrive\桌面\种子库.txt"

common_content = find_common_parts(file1_path, file2_path)

differ_content = find_differ_parts(file1_path, file2_path)


# 打印相同部分
if common_content:
    print("两个文件中的相同部分如下：")
    for line in common_content:
        print(line.strip())
else:
    print("两个文件中没有找到相同的部分。")


# 打印不同部分
if differ_content:
    print("两个文件中的不同部分如下：")
    for line in differ_content:
        print(line.strip())
else:
    print("两个文件全部相同")
