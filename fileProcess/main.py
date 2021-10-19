# 根据用户输入的txt文件名，先提取出文件名name。
# 1. 将其复制到上层目录，然后命名为luna_pinyin.name.dict.yaml文件
#    1.1 如果有重名的，返回错误信息
# 2. 将其打开，在最上方写入信息
# 3. 打开extended文件，在末尾写入文件信息

import os
import shutil


def write_raw_index(file, name):
    filename = file
    with open(filename, 'r+', encoding='utf-8') as f:
        content = f.read()
        f.seek(0, 0)
        # mid, text, source, uid
        # text = 'mid' + ',' + 'text' + ',' + 'source' + ',' + 'uid'
        text = '''# Rime dictionary
# encoding: utf-8 
---
name: luna_pinyin.content
version: "2021.02.05"
sort: by_weight
use_preset_vocabulary: true
import_tables:
  - luna_pinyin
...
'''
        text = text.replace("content", name)
        f.write(text + '\n' + content)


def getFileName():
    name = input("输入文件名:")
    # name = "programmer.txt"
    os.chdir("E:\\Habei\\RIME\\Corpur\\")
    flag = os.path.exists(name)
    if not flag:
        return "没有该文件！"
    return name


def copyFile(name):
    pwd = os.getcwd()
    father_path = os.path.abspath(os.path.dirname(pwd) + os.path.sep + ".")
    # print(father_path)
    new_file_name = "luna_pinyin." + name[:-4] + ".dict.yaml"
    shutil.copy(pwd + "\\" + name, father_path + "\\" + new_file_name)


def addContent(name):
    os.chdir("E:\\Habei\\RIME")
    new_file_name = "luna_pinyin." + name[:-4] + ".dict.yaml"
    write_raw_index(new_file_name, name[:-4])
    f = open("luna_pinyin.extended.dict.yaml", 'a')
    f.write("\n    - luna_pinyin." + name[:-4])
    f.close()
    print("处理成功！")


name = getFileName()
if name == "没有该文件！":
    print(name)
else:
    copyFile(name)
    addContent(name)

