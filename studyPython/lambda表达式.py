# 1. 排序

# 需求：将列表中的元素按照绝对值大小进行升序排列
list1 = [3,5,-4,-1,0,-2,-6]
test1 = sorted(list1, key=lambda x: abs(x))
print(test1) # [0, -1, -2, 3, -4, 5, -6]
# sorted(list1, key=lambda x: abs(x))
# print(list1) # [3, 5, -4, -1, 0, -2, -6]


test2 = [('b',4),('a',0),('c',2),('d',3)]
# 按照列表中第一个元素排序
print(sorted(test2,key=lambda x:x[0]))
# [('a', 0), ('b', 4), ('c', 2), ('d', 3)]
# 按照列表中第二个元素排序
print(sorted(test2,key=lambda x:x[1]))
# [('a', 0), ('c', 2), ('d', 3), ('b', 4)]


# 2. 复合函数
# f(x)=ax^2+bx+c
def quadratic(a,b,c):
    return lambda x: a*x*x + b*x + c
f = quadratic(1, -1, 2)
print(f(5)) # 22
print(quadratic(1, -1, 2)(5)) # 22




