# 元组不可以修改（只读文件）、增加、删除，与列表最大的不同之处，除此之外，没有什么太大区别
# 与c中的const一样

# 字典的操作
print("字典的操作：")
infor = {'age':18,'name':'Amy'}

print(infor.keys()) # dict_keys(['age', 'name']) 是一个对象
print(infor.values()) # dict_values([18, 'Amy']) 是一个对象

for temp in infor.keys():
    # 一个值
    print(temp)
# age
# name
print(".items()返回一个列表中存放元组 的一个对象")
print(infor.items()) # dict_items([('age', 18), ('name', 'Amy')])

for temp in infor.items():
    # 输出类型为元组
    print(temp)
# ('age', 18)
# ('name', 'Amy')

# 将元组 c,d = a = (11,22)逐个赋值，拆包
a = (11,22)
c,d = a
print(c)  # 11
print(d)  # 22
print(a)  # (11, 22)
for A,B in infor.items():
    print("开始拆包：")
    print(A) # 键
    print(B) # 值

# 函数
# 函数里面定义的变量，只能在函数里面使用，出了函数就不能使用。
print("")
print("函数：")
def test():
    a = 11
    b = 22
    c = 33
    # 第1种，用一个列表来封装3个变量的值
    d = [a,b,c]
    # return d # [11, 22, 33]

    # 第2种，
    # return [a,b,c] # [11, 22, 33]

    # 第3种，
    # return (a,b,c) # (11, 22, 33)

    # 第4中，默认封装成元组返回
    return a,b,c # (11, 22, 33)

num = test()
print(num)

# 函数的4种类型
# 函数的嵌套调用
# 用百度百科理解函数的嵌套调用
# 嵌套调用--应用
# 嵌套调用--要求
print("")
# 先写大框架
def sum_3_nums(a,b,c): # 接收————形参
    result = a+b+c
    print(result)
    return result

def average(sum):
    avg = sum / 3
    print("%d"%avg)

# 1. 获取3个值
num1 = int(input("第1个值："))
num2 = int(input("第2个值："))
num3 = int(input("第3个值："))

sum = sum_3_nums(num1,num2,num3) # 传递————实参
average(sum)