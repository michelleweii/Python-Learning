import day11sendmsg
# print("__name__发生神奇的变化")
# test11
# test22
# day11sendmsg # 导入的模块名

def test11():
    print("test11")
def test22():
    print("test22")
def recv():
    print("recv--test1")

if __name__ == '__main__':
    test11()
    test22()
    recv()

# print("-------now---------")
# recv()
# print(__name__) #__main__此程序的名字




"""
output:
/usr/local/bin/python3.6 /Users/weiwenjing/Documents/PycharmProjects/PythonLearning/day11recvmsg.py
recv--test1
__main__
"""

"""
导入了import day11sendmsg这个模块之后：
test11
test22
day11sendmsg
-------now---------
recv--test1
__main__
"""

"""

在模块文件中新添加了if __name__ == '__main__':
结果变成这样：

-------now---------
recv--test1
__main__

"""