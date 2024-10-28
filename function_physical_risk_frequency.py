# physical risk solution

import jieba
from collections import Counter

def physical_risk_solution_frequency(file_path):

    # 加载自定义词库
    custom_dict_path = r"C:\Users\zxy\OneDrive\桌面\ESG_20241021\物理风险v1.0.txt"
    jieba.load_userdict(custom_dict_path)

    # 读取txt文件
    with open(file_path, 'r', encoding='utf-8') as file:
        text_content = file.read()

    # 分词
    words = jieba.lcut(text_content)

    # 读取自定义词库中的词
    with open(custom_dict_path, 'r', encoding='utf-8') as dict_file:
        custom_words = [line.strip() for line in dict_file if line.strip()]

    # 统计词频
    # word_freq = Counter(words)


    def calculate_total_frequency(words, custom_words):
        word_counts = Counter(words)

        total_frequency = sum(word_counts[word] for word in custom_words)

        return total_frequency

    total_frequency = calculate_total_frequency(words, custom_words)

    print(f"自定义词库中所有词的总频率{file_path}：{total_frequency}")

    return total_frequency



if __name__ == "__main__":

    owner_path = input("pls input index: ")
    # owner_dict_path = input("dict: ")

    physical_risk_solution_frequency(owner_path)