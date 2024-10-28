def remove_duplicates(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        words = file.readlines()

    unique_words = []
    for word in words:
        if word.strip() not in unique_words:
            unique_words.append(word.strip())

    with open(output_file, 'w', encoding='utf-8') as file:
        for word in unique_words:
            file.write(word + '\n')


# 使用函数
input_file = r"C:\Users\zxy\OneDrive\桌面\物理风险.txt"  #这里替换为你的输入文件名
output_file = r"C:\Users\zxy\OneDrive\桌面\物理风险v1.0.txt"  # 这里替换为你想要保存的输出文件名

remove_duplicates(input_file, output_file)