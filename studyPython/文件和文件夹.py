# python实现删除某路径下文件及文件夹的脚本
import os
import shutil
import sys

delList = []
delDir = "test"
delList = os.listdir(delDir)
# print("delList:{}".format(delList))
for f in delList:
    filePath = os.path.join(delDir,f)
    # print("filePath:{}".format(filePath))
    if os.path.isfile(filePath):
        os.remove(filePath)
        print(filePath+" was removed!")
    elif os.path.isdir(filePath):
        shutil.rmtree(filePath,True)
        print("Directory: "+filePath+" was removed!")

# delList:['2.txt.py', 'test_isdir', '1.txt']
# filePath:test/2.txt.py
# test/2.txt.py was removed!
# filePath:test/test_isdir
# Directory: test/test_isdir was removed!
# filePath:test/1.txt
# test/1.txt was removed!


# shutil是一个高层次的文件操作模块。True参数表示ignore_errors(忽略拷贝时候的错误)。
#
# 类似于高级API，而且主要强大之处在于其对文件的复制与删除操作更是比较支持好


# 有关文件夹与文件的查找，删除等功能 在 os 模块中实现。

# 一、取得当前目录
# 1.1
s = os.getcwd()
# s 中保存的是当前的执行目录(即执行所在的文件夹)
print(s)
# /Users/.../Documents/PycharmProjects/studyPython
print("-----{}------".format(sys.path[0]))
# -----/Users/weiwenjing/Documents/PycharmProjects/studyPython------

# [注意]
# 如果是要获得程序运行的当前目录所在位置，那么可以使用os模块的os.getcwd()函数。
# 如果是要获得当前执行的脚本的所在目录位置，那么需要使用sys模块的sys.path[0]变量或者sys.argv[0]来获得
# 1.2
import time
floder = time.strftime(r"%Y-%m-%d_%H-%M-%S",time.localtime())
# os.makedirs(r'%s/%s'%(os.getcwd(),floder)) # 创建一个文件夹

# 二、更改当前目录
# os.chdir("root/123") # #说明： 当指定的目录不存在时，引发异常。
# e.g.
path = "/tmp"
# 查看当前工作目录
retval = os.getcwd()
print("当前工作目录为 %s" % retval) # 当前工作目录为 /www
# 当前工作目录为 /Users/.../Documents/PycharmProjects/studyPython/root/123
# 修改当前工作目录
os.chdir(path)
# 查看修改后的工作目录
# retval = os.getcwd()
# print("目录修改成功 %s" % retval) # 目录修改成功 /tmp
# 目录修改成功 /private/tmp


# 三、将一个路径名分解为目录名和文件名两部分
fpath , fname = os.path.split( "/root/123/hello.py")
print("filePath:{}".format(fpath)) # filePath:/root/123
print("fname:{}".format(fname)) # fname:hello.py


# 四、分解文件名的扩展名
fpathandname , fext = os.path.splitext( "/root/123/world.py")
print("fpathandname:{}".format(fpathandname)) # fpathandname:/root/123/world
print("fext:{}".format(fext)) # fext:.py


# 五、判断一个路径（ 目录或文件）是否存在   -----why
b = os.path.exists("./sa") # False
a = os.path.exists("test") # False
c = os.path.exists("./root/123") # # False
# print(b)
# print(a)
# print(c)

# 六、判断一个路径是否文件          -----why
d = os.path.isfile("test")
e = os.path.isfile("root/123/hello.py")
f = os.path.isfile("root/123/1.txt")
# print(d) # False
# print(e) # False
# print(f) # False

# 七、判断一个路径是否目录          ----why
d = os.path.isdir("test")
e = os.path.isdir("root/123/hello.py")
f = os.path.isdir("root/123/")
# print(d) # # False
# print(e) # # False
# print(f) # False

# 八、获取某目录中的文件及子目录的列表
# L = os.listdir("./root/123")
# print(L)

# 九、创建子目录
# os.makedirs( path )  # path 是"要创建的子目录"
# os.makedirs("./winter")
# 例如:
# os.makedirs("/root/123")
# 调用有可能失败，可能的原因是：
#
# (1) path 已存在时(不管是文件还是文件夹)
#
# (2) 驱动器不存在
#
# (3) 磁盘已满
#
# (4)磁盘是只读的或没有写权限

# 十、删除子目录
# os.rmdir("path") # # path: "要删除的子目录"

# 产生异常的可能原因:
#
# (1) path 不存在
#
# (2) path 子目录中有文件或下级子目录
#
# (3) 没有操作权限或只读

# 十一、删除文件
# os.remove(filename)  # filename: "要删除的文件名"
# 产生异常的可能原因:
#
# (1) filename 不存在
# (2) 对filename文件， 没有操作权限或只读。

# 十二、文件改名
# os.name("test","rename_test")
# os.name( oldfileName, newFilename)


# ../ 表示上级目录  /root表示绝对路径 根目录
# root 和 ./root是一样的