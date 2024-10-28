# physical risk solution

import jieba
from collections import Counter
import pandas as pd

# 自定义词库路径
custom_dict_path = r"C:\Users\zxy\OneDrive\桌面\ESG_20241021\物理风险v1.0.txt"  # 替换为你的词库文件路径

# 加载自定义词库
jieba.load_userdict(custom_dict_path)

# 读取txt文件
file_path = r"C:\Users\zxy\OneDrive\桌面\A股年报TXT\2023_5361份\000001_2023_平安银行_2023年年度报告_2024-03-15.txt"  # 替换为你要分词的文件路径
with open(file_path, 'r', encoding='utf-8') as file:
    text_content = file.read()

# print(text_content)

# 分词
words = jieba.lcut(text_content)

# 读取自定义词库中的词
with open(custom_dict_path, 'r', encoding='utf-8') as dict_file:
    custom_words = [line.strip() for line in dict_file if line.strip()]

# 统计词频
word_freq = Counter(words)

# 按照自定义词库中的词进行统计
# custom_word_freq = {word: word_freq[word] for word in custom_words}

# # 打印结果
# for word, freq in custom_word_freq.items():
#     print(f'{word}: {freq}')

# # 创建 DataFrame
# df = pd.DataFrame(list(custom_word_freq.items()), columns=['Word', 'Frequency'])
#
# # 将结果保存到 Excel 文件
# output_excel_path = r"C:\Users\zxy\OneDrive\桌面\demo.xlsx"
#
# df.to_excel(output_excel_path, index=False)
#
# print(f"success {output_excel_path}")


def calculate_total_frequency(words, custom_words):
    word_counts = Counter(words)

    total_frequency = sum(word_counts[word] for word in custom_words)

    return total_frequency

total_frequency = calculate_total_frequency(words, custom_words)

# 输出总频率
print(f"自定义词库中所有词的总频率：{total_frequency}")