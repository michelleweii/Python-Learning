# 字符串常见操作
# <find> 找到返回下标，找不到返回-1
# <index> 找到返回下标，找不到报错
# <count> 统计个数
# <replace> 替换
# ...
"""
myStr = "hello world itcast and hahaitcastcpp    *"
print(myStr.find("dog"))    # -1
print(myStr.find("world"))  # 6
print(myStr.find("itcast")) # 12
print(myStr.rfind("itcast")) # 27 从右边开始找
print(myStr.rindex("itcast")) # 27
print(myStr.count("itcast")) # 2
print(myStr.count("hahahahahahh")) # 0
print(myStr.replace("world","WORLD")) # 字符串是不可变类型,返回一个新的，记得接收
print(myStr.replace("itcast","****"))
print(myStr.split(" "))
print(myStr.startswith("aaaa")) # False
print(myStr.startswith("hello")) # True
print(myStr.endswith(".txt")) # False
print(myStr.ljust(50))
print(myStr.center(50))
print(myStr.rjust(50))
print(myStr.strip(" ")) # 用于去除字符串的首尾字符
print(myStr.partition("itcast")) # ('hello world ', 'itcast', ' and hahaitcastcpp    *')
print(myStr.splitlines()) # 按换行符进行切割
print(myStr.isalpha()) # 判断是不是纯字母
print(myStr.isalnum()) # 判断里面有没有数字（数字+字母，纯数字）
a = '_'
print(a.join(myStr)) # 按照_进行连接
content = "cwbf   \t\t qwe bb\nuy s  ba isbdo"
# split()中什么都没传，按照不可见字符进行切割
c = content.split()
print(c) # ['cwbf', 'qwe', 'bb', 'uy', 's', 'ba', 'isbdo']
print(" ".join(c))
"""

print("文件操作：\n")
# 硬盘只能存2进制文件，图片png、音乐mp4
# 文本文件要转换为2进制文件b
# +打开可读/可写 w+,r+
# readlines # 按行读写，读完之后是一个列表，每行是一个字符串
# read 整个内容读出来，是一个字符串




"""
文件备份的流程：
1. 获取要复制的文件名 input()
2. 打开这个文件（"r"）
3. 创建一个文件 xxxx[复件].txt
4. 从原文件中读取数据
5. 将读取的数据写入到新文件中
6. 关闭两个文件
"""
"""
old_file_name = input("输入复制文件名:")
f_read = open(old_file_name,"r")

position = old_file_name.rfind(".")
new_file_name = old_file_name[:position]+"[复件]"+old_file_name[position:]

f_write = open(new_file_name,"w")
# content = f_read.read() # read()很危险，容易内存溢出
# f_write.write(content)
while True:
    content = f_read.read(1024)
    if len(content)==0:
        break
    f_write.write(content)
        
f_read.close()
f_write.close()
"""

# 定位到某个位置
# seek(offset,from)
# offset: 偏移量
# from: 方向
# 0：表示文件开头
# 1：表示当前位置
# 2：表示文件末尾

# demo:把位置设置为：从文件开头，偏移5个字节
f = open("pythonTest.txt")
print(f.read(1)) #{
print(f.read(1)) #\
print(f.read(1)) #r
print(f.tell())  #3
print(f.seek(0,2)) #387
print(f.seek(0,0)) #0 回文件开头

import os
# 操作文件的包
print(os.listdir("."))

# print("批量修改文件名：\n")
# os.mkdir("DocBatchRename/1.txt")
# os.mkdir("DocBatchRename/2.txt")
# os.mkdir("DocBatchRename/3.txt")

# 1. 获取一个要重命名的文件夹的名字
folder_name = input("input rename needed :\n")
# 2. 获取那个文件夹中所有的文件名字
file_names = os.listdir(folder_name)

'''
# 方法一
# 不加报错
"""
报错：
Traceback (most recent call last):
  File "/Users/weiwenjing/Documents/PycharmProjects/PythonLearning/day8(字符串操作、文件).py", line 112, in <module>
    os.rename(name,"[michelle出品]-"+name)
FileNotFoundError: [Errno 2] No such file or directory: '3.txt' -> '[michelle出品]-3.txt'
"""
os.chdir(folder_name) # os.chdir() 方法用于改变当前工作目录到指定的路径。

# 3. 对获取的名字进行重命名即可
for name in file_names:
    print(name)
    os.rename(name,"[michelle出品]-"+name)
'''

# 方法二
for name in file_names:
    print(name)
    old_file_name = "./"+ folder_name +"/"+name
    new_file_name = "./"+ folder_name +"/"+"[michelle出品]-"+name

    os.rename(old_file_name,new_file_name)
