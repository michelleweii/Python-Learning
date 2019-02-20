# https://blog.csdn.net/u011630575/article/details/78604226

old = [1,[1,2,3],3]
new = old[:]
print("before1:")
print(old,id(old))
print(new,id(new))
# before1:
# [1, [1, 2, 3], 3] 4516542024
# [1, [1, 2, 3], 3] 4516542664

new[0]=3 # 切片只对第一层实现深拷贝
new[1][0]=3 # 切片对第二层就是不深拷贝了（list套list）
print("after1:")
print(old,id(old)) # 原有样本被影响了，从1变成了3
print(new,id(new))
# after1:
# [1, [3, 2, 3], 3] 4516542024
# [3, [3, 2, 3], 3] 4516542664

# 如果我想对list套list中（第二层）的数据进行改变，但不想影响原有样本
import copy
list_old = [1,[1,2,3],3]
list_new = copy.deepcopy(list_old[:])
print("before2:")
print(list_old,id(list_old))
print(list_new,id(list_new))
# before2:
# [1, [1, 2, 3], 3] 4516543880
# [1, [1, 2, 3], 3] 4516542792

list_new[0]=3
list_new[1][0]=3
print("after2:")
print(list_old,id(list_old))
print(list_new,id(list_new))
# after2:
# [1, [1, 2, 3], 3] 4516543880
# [3, [3, 2, 3], 3] 4516542792