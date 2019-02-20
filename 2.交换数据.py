# python-list实现的交换
a = [1,2,3]
b = [4,5,6]
a,b = b,a
print(a) # [4, 5, 6]
print(b) # [1, 2, 3]

# numpy中交换矩阵中两列元素的方法
# 交换同一矩阵中的不同行用方法2，如果是不同矩阵用方法1
import numpy as np
A = np.array([[1,2,3],[4,5,6]])
print(A)
# [[1 2 3]
#  [4 5 6]]

# 目标:将同一矩阵的第一列和最后一列进行交换
# 方法1
A[:,0],A[:,-1] = A[:,-1],A[:,0]
print(A)
# [[3 2 3]
#  [6 5 6]] # failed

# 目标:将同一矩阵的第一列和最后一列进行交换
# 方法2
A[:,[0,-1]] = A[:,[-1, 0]]
print(A)
# [[3 2 1]
#  [6 5 4]]

# 目标:将同一矩阵的第一行和最后一行进行交换
A[[0,1],:] = A[[1,0],:]
print(A)
# [[6 5 4]
#  [3 2 1]]