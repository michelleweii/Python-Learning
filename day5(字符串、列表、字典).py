# 1. 嵌套循环中break的作用范围
i = 1
while i<=5:

    j = 1
    while j<=i:
        print("*",end="")
        j += 1
        # break # 结束整个while循环
        # continue # 结束这一次的循环，转而执行下一次的循环

    print("")  # 换行

    i += 1
    # break
"""
*
*
*
*
* while循环里的break，只作用在当前的while里

如果while_j里没有break，那么输出：
*
**
***
****
*****
"""

# 2. 字符串在内存中的存储方式
# cpu速度快，但是存储量少；硬盘存储东西多，但是和cpu相比速度是蜗牛；
# 内存是他们两者的折中。1G=1024M；1M=1024K；1K=1024bytes(字节)。
# 最小的分配单元是一个字节，一个字节存的最大值是255(数值)。
# 数字不超过255，存储占一个字节；字符串，每一个字符占一个字节+'\0'，（'\0'在Python中不计，c语言要算）。
# e.g. test="hello"
# 所以在Python中len(test)=5,在C语言中,len(test)=6。(c多了一个'\0'的计算)


# 3. 常用的数据类型转换
# 4. 字符串的输入和输出

# 5. 组成字符串的2种方式
a = "hello"
b = "bob"
c = a+b
# 第一种
print(c) # hellobob
e = "===%s==="%(a+b)
# 第二种
print(e) # ===hellobob===

# 6. 字符串
# 7. 切片  [起始位置:终止位置:步长]
# index索引
# 取逆序
name = 'abcdefABCDEF'
print(name[::-1]) # [起始位置:终止位置:步长] # FEDCBAfedcba

# 8. 列表
names = ['A','B','C']
# 存储多个数据
# 和C中的数组的不同之处在于，数组要求存储同一类型，不同类型会奔溃
nums = [11,22,3.14,"100"] # 可以同时存储多种不同的数据类型 stronger!!

# 9. 列表的增删改查
# 增加--1  names.append()  【只能最后】
names.append('D')
print(names) # ['A', 'B', 'C', 'D']
# 增加--2  names.insert(位置，要添加的内容)   【想加哪里加哪里】
names.insert(0,'Z')
print(names)  # ['Z', 'A', 'B', 'C', 'D']
# 增加--3 列表也可以和字符串一样直接相加'+'
names3 = ["Amy","Ann","Mike"]
print(names+names3) # ['Z', 'A', 'B', 'C', 'D', 'Amy', 'Ann', 'Mike']
# 增加--4 names.extend(names3)
names2 = ['W','S','X']
names2.extend(names3)
print(names2) # ['W', 'S', 'X', 'Amy', 'Ann', 'Mike']
################
# 总结——添加
################
# 添加新元素
# append()
# insert()
# extend()


# 删除--1 .pop 每次从最后一位删除
names2.pop()    # 弹栈
print(names2)  # ['W', 'S', 'X', 'Amy', 'Ann']
# 删除--2 remove("要删除的内容")
names2.remove('S')
print(names2)   # ['W', 'X', 'Amy', 'Ann']
# 删除--3 切片

# 删除--4 del names[下标]
del names2[-1]
print(names2) # ['W', 'X', 'Amy']

##############
# 总结———删除
##############
# pop() ------>删除最后一个
# remove() ----->根据内容删除
# del xxx[下标] ------>根据下标来删除


# 改
names2 [0] = 'www'
print(names2) # ['www', 'X', 'Amy']

# 查 in
if 'X' in names2:
    print("find it ....")
if 'q' not in names2:
    print("not find it ...")


# 10. 名字管理系统
print("*"*5+" 名字管理系统 "+"*"*5)
# pass 占坑，不会报错


print("start 字典....")
# 11. 字典
# infor = {键：值,键：值}
information = {"name":"班长","addr":"山东","age":18}
print("%s %s %d"%(information["name"],information["addr"],information["age"]))

# 12. 增删改查
infor = {'name':'bangzhang','age':19}
infor['qq']=100
print(infor)
infor['qq']=1111
print(infor)
del infor['qq']
print(infor)

# 查询  （字典根据key来查询，不是根据下标进行查询）
# .get()避免直接报错
print(infor.get('qq'))  # None
print(infor.get('name'))    # bangzhang

#############
#  总结
#############
# 添加
# xxx[新的Key] = value

# 删除
# del xxx[key]

# 修改
# xxx[已存在的key] = new_value

# 查询
# xxx.get(key)

list1 = ["aa","bb","cc"]
for temp in list1:
    print(temp)
# aa
# bb
# cc

infors1 = [{"name":"aa","age":18},{"name":"bb","age":28}]
for temp in infors1:
    print(temp)
# {'name': 'aa', 'age': 18}
# {'name': 'bb', 'age': 28}

for temp in infors1:
    print(temp['name'])
# aa
# bb


print("")
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

# 用来存储名片
card_infors = []

while True:

    # 2. 获取用户的输入
    num = int(input("请输入操作序号："))

    # 3. 根据用户的数据执行相应的功能
    if num == 1:
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
    elif num==2:
        pass
    elif num==3:
        pass
    elif num==4: # 查找
        find_name = input("请输入要查找的姓名：")

        fing_flag = 0 # 默认没有找到

        for temp in card_infors:
            if find_name == temp["name"]:
                print("%s\t%s\t%s"%(temp['name'],temp['qq'],temp['addr']))
                fing_flag = 1
                break
        if fing_flag == 0:
            print("查无此人")

    elif num == 5:
        print("姓名\tqq\t\t住址")
        for temp in card_infors:
            # print(temp)
            print("%s\t%s\t%s"%(temp['name'],temp['qq'],temp['addr']))

    elif num == 6:
        break
    else:
        print("输入有误")

    print("")

print("")
print("extend()和append()的区别")
a = [11,22,33]
d = [11,22,33]
b = [44,55]
e = [44,55]
c = a.extend(b)
f = d.append(e)
print("after extend: ")
print(c) #None  # append的操作返回值就是None，是直接操作在a上
print(a.extend(b)) # None
print(a)
# [11, 22, 33, 44, 55, 44, 55]
print("after append: ")
print(f) # None
print(d.append(e)) # None
print(d)
# [11, 22, 33, [44, 55], [44, 55]]  # append当做整体添加
