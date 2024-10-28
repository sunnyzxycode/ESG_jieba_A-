import os
import pandas as pd

def save_file_names_to_excel(folder_path, output_file):
    # 初始化一个空列表来存储文件信息
    file_list = []

    # 遍历文件夹
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # 构建完整的文件路径
            file_path = os.path.join(root, file)
            # 将文件路径添加到列表中
            file_list.append(file_path)

    # 创建一个DataFrame
    df = pd.DataFrame(file_list, columns=['File Path'])


    df.to_excel(output_file, index=False)

if __name__ == "__main__":
    folder_path = r"C:\Users\zxy\OneDrive\桌面\A股年报TXT"

    output_file = r"C:\Users\zxy\OneDrive\桌面\file_names.xlsx"
    save_file_names_to_excel(folder_path, output_file)

    print(f"File names have been saved to {output_file}")
