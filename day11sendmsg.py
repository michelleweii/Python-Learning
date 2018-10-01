def test11():
    print("test11")
def test22():
    print("test22")

# 新添加，看变化在day11recvmsg.py
if __name__ == '__main__':
    # 有了这个条件，当名字不是__main__的话，比如在day11recvmsg中导入day11sendmsg这个模块时，
    # day11recvmsg在打印day11sendmsg的有关信息时，name会相应的转化为day11sendmsg，而不是main,
    # 所以，main里的内容就不会执行，也就达到了，或者说《避免了导入一个模块，实际上会将模块整个都执行一遍!!!》
    # 这个问题。
    test11()
    test22()

# print(__name__)

"""
/usr/local/bin/python3.6 /Users/weiwenjing/Documents/PycharmProjects/PythonLearning/day11sendmsg.py
test11
test22
__main__
"""