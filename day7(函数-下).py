# 局部变量
# 全局变量
# 局部变量和全局变量的区别

# 定义一个全局变量，wendu
wendu = 0

def get_wendu():
    # 如果wendu这个变量已经在全局变量的位置定义了，此时还想再函数中对这个全局变量进行修改的
    # 话，那么，仅仅是wendu=一个值，这还不够。。。此时wendu这个变量是一个局部变量，仅仅是
    # 和全局变量的名字相同罢了
    # wendu = 33  # 最后的print还是0

    # 使用global来对一个全局变量进行声明，那么这个函数中的wendu=33就不是定义一个局部变量，
    # 而是对全局变量进行修改。
    global wendu
    wendu = 33 # 最后的print是33

def print_wendu():
    print("温度是%d"%wendu)

get_wendu()
print_wendu()  # 温度是33

# 全局变量定义的位置————放在函数调用之前即可
a = 100
def test():
    print("a=%d" % a) # a = 100
    print("b=%d" % b) # b = 200
   # print("c=%d" % c)
b = 200
test()
# print("c=%d" % c)
# NameError: name 'c' is not defined
#c = 300

print("")
print("函数管理系统")
#help(print) # 查看print作用
# 查看文档信息
"""
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

"""



# 封装
# 用来存储名片
card_infors = []

def print_menu():
    print("名片管理系统")
    # 14. 名片管理系统
    # 1. 打印功能提示
    print("="*50)
    print("  名片管理系统")
    print("1 添加一个新的名片")
    print("2 删除一个名片")
    print("3 修改一个名片")
    print("4 查询一个名片")
    print("5 show")
    print("6 退出系统")
    print("="*50)

def add_new_card_infor():
    """新建"""
    global card_infors
    new_name = input("请输入新的名字：")
    new_qq = input("请输入新的qq：")
    new_addr = input("请输入新的住址：")

    # 定义一个新的字典，用来存储一个新的名片
    new_infor = {}
    new_infor['name'] = new_name
    new_infor['qq'] = new_qq
    new_infor['addr'] = new_addr

    # 将一个字典，添加到列表中
    card_infors.append(new_infor)
    print(card_infors)

def find_card_infor():
    """查询"""
    global card_infors

    find_name = input("请输入要查找的姓名：")
    fing_flag = 0  # 默认没有找到

    for temp in card_infors:
        if find_name == temp["name"]:
            print("%s\t%s\t%s" % (temp['name'], temp['qq'], temp['addr']))
            fing_flag = 1
            break
    if fing_flag == 0:
        print("查无此人")


def show_all_infor():
    """显示所有名片信息"""  # 文档说明
    global card_infors
    print("姓名\tqq\t\t住址")
    for temp in card_infors:
        # print(temp)
        print("%s\t%s\t%s" % (temp['name'], temp['qq'], temp['addr']))

def main():
    """控制整个程序"""
    print_menu()

    while True:
        # 2. 获取用户的输入
        num = int(input("请输入操作序号："))

        # 3. 根据用户的数据执行相应的功能
        if num == 1:
            add_new_card_infor()
        elif num==2:
            pass
        elif num==3:
            pass
        elif num==4: # 查找
            find_card_infor()
        elif num == 5:
            show_all_infor()
        elif num == 6:
            break
        else:
            print("输入有误")

        print("")

# 调用主函数
#main()
help(show_all_infor())



# 列表、字典当做全局变量可以直接用，不用声明global
ok = [11,22,33]
def test():
    ok.append(44)
def test2():
    print(ok)

test()
test2() # [11, 22, 33, 44]


# 缺省参数之后放在函数的最后一位
# 命名参数or缺省参数
"""
def test3(a,d,b=11,c=22): # 缺省参数
    print(a)
    print(b)
    print(c)
    print(d)

test3(0,0,b=12) # 命名参数
"""

# 不定长参数
# arg 打印出来的是个元组
def sum_2_nums(a,b,*args): # args保存多个值
    print("-"*30)
    print(a)
    print(b)
    print(args)

sum_2_nums(11,22,33,444,55,67,88)
"""
11
22
(33, 444, 55, 67, 88)
"""
sum_2_nums(11,22,33)
"""
11
22
(33,)     # 如果一个元组里面只有一个元素，一定要在这个元素后面添加'，'
          # 否则不是元组。
"""
sum_2_nums(11,22)
"""
11
22
() # 是个元组
"""
# sum_2_nums(11) # 错误

print("")
def test3(a,b,c=33,*args,**kwargs):
    print(a)  # 1
    print(b)  # 22
    print(c)  # 33
    print(args) # (44, 55)
    print('-'*10)
    print(kwargs) # {}

# test3(1,22,33,44,55) # 44,55存在args里

# 多余参数前面带变量名的都赋给kwargs，不带变量名的给args
test3(11,22,33,task=99,done=89)
"""
11
22
33
()
--------
{'task': 99, 'done': 89}
"""

print("")
print("args内部求和")
def sum_2_nums(a,b,*args): # args保存多个值
    print("-"*30)
    print(a)
    print(b)
    print(args)
    print("sum:")
    result = a+b
    for i in args:
        result+=i
    print("result=%d"%result)
sum_2_nums(11,22,33) # result=66


print("")
print("test4")
def test4(a,b,c=33,*args,**kwargs):
    print(a)  # 1
    print(b)  # 22
    print(c)  # 33
    print(args) # (44, 55)
    print('-'*10)
    print(kwargs) # {}

A = (44,55,66)
B = {"name":"Amy","age":18}
test4(11,22,33,A,B)
"""
test4
11
22
33
((44, 55, 66), {'name': 'Amy', 'age': 18})
----------
{}
"""
print("")
test4(11,22,33,*A,**B) # **拆包，拆字典 ； *拆元组
"""
11
22
33
(44, 55, 66)
----------
{'name': 'Amy', 'age': 18}
"""
print("")
print("引用：")
a = 100
b = a
# 不是值给了b，只是把地址给了b
print(id(a)) # 4495488032
print(id(b)) # 4495488032
# 只要是Python中的赋值，统统都是引用

# 不可变，可变类型
# 数字是不可变类型
# 字符串类型不支持赋值，原来我认为的那种是引用
# 元组也是不可变类型
# ******************* 列表，字典是可以修改的变量
a = 'hello'
a = 'world'
# a[0]='W'
# print(a[0]) or print(a)
"""
Traceback (most recent call last):
  File "/Users/weiwenjing/Documents/PycharmProjects/PythonLearning/day7(函数-下).py", line 284, in <module>
    a[0]='W'
TypeError: 'str' object does not support item assignment
"""
# 所以，
# 在字典中，声明key值的时候，列表和字典不能做key
test5 = {"name":"Amy",100:"hh",(11,22):'dwe'}
print(test5) # {'name': 'Amy', 100: 'hh', (11, 22): 'dwe'}
# test6 = {"name":"Amy",100:"hh",(11,22):'dwe',[44,55]:'swn'}
# print(test6) # TypeError: unhashable type: 'list'

# 递归
print("")
print("递归")
# 内存溢出