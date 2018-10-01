# Review:
# 1-实例
# 当创建为对象之后
class CarStore(object):
    def __init__(self):
        self.factor = Factor()

    def order(self, car_type):
        return self.factor.select_car_by_type(car_type)
        # return Car() # 返回类的引用

# 定义了函数实现了解耦功能
# 再更改
class Factor(object):
    def select_car_by_type(car_type):
        if car_type == "索纳塔":
            return Suonata()
        elif car_type == "名图":
            return Mingtu()
        elif car_type == "ix35":
            return Ix35()


class Car(object):
    def move(self):
        print("车在移动。。。")
    def music(self):
        print("正在播放音乐。。。")
    def stop(self):
        print("车停止。。。")

class Suonata(Car):
    pass

class Mingtu(Car):
    pass

class Ix35(Car):
    pass

car_store = CarStore()
# car = car_store.order(100000)
# car.move()
# car.music()
# car.stop()

# 2-__new__方法
# new就是创建对象的那个人，用来创建对象。
class Dog(object):
    def __init__(self):
        print("----init方法-----")
    def __del__(self):
        print("----del方法-----")
    def __str__(self):
        print("----str方法-----")
        return "对象的描述信息"

    def __new__(cls, *args, **kwargs):
        # 相当于子类重写new方法，但是不具备创建对象的能力，
        # 所以现在要求助父类object来创建对象。
        # new里的cls，此时是Dog指向的那个类对象。


        # 类也是对象
        print(id(cls)) # 140285549016952
        print("----new方法-----")

        # 求助父类，返回创建对象的引用。
        return object.__new__(cls) #没有这一句，输出----new方法-----，创建不了对象。

print(id(Dog)) # 140285549016952

xtq = Dog()
"""
xtq = Dog() # 先调用new，将new保持；再调用init。
相当于要做3件事：
1.调用__new__方法来创建对象，然后找了一个变量来接收__new__的返回值，这个返回值表示创建出来的对象的引用；
2.调用__init()__（刚刚创建出来的对象的引用，调用init，init的self指向了对象）；
3.返回对象的引用，这里xtq指向对象（==上一步self指向的内存里的对象）。
"""
# output:
# ----new方法-----   # 只负责创建对象。
# ----init方法-----  # 只负责初始化。（和c++中的构造方法有所区别，构造方法既完成创建，又完成初始化）
# ----del方法-----
# 这一句xtq = Dog()执行，只调用了new方法，而没有调用init方法（如果new里没有写return的话）


# 3-创建单例对象
# 创建了new方法，还是要去调用init()方法，所以为什么要创建new方法呢？
# 单例———不管创建了多少次，仅仅只有一个对象。
# 程序里的窗口。所有app都在这个窗口里，打开不同的app也还在这个窗口里。
# 比如，class Dog(); a = Dog(); b = Dog()。a和b分别指向了两个不同的对象。（两个不同的位置）
# 而单例指a和b同指向内存中的一个对象。（一个位置）
# class SingleDog(object):
#
#     # 类属性(作用在类中的全局变量)
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         """
#         if xxx:
#             return object.__new__(cls)
#         else:
#             return 上一次创建的对象的引用
#         """
#         if cls.__instance == None:
#             cls.__instance = object.__new__(cls)
#             return cls.__instance
#         else:
#             return cls.__instance
#
#
# s_a = SingleDog()
# print(id(s_a)) #4307525304
# s_b = SingleDog()
# print(id(s_b)) #4307525304


# 4-只初始化一次对象
# 在3的基础上
class SingleDog(object):

    # 类属性(作用在类中的全局变量)
    __instance = None

    def __new__(cls, name, *args, **kwargs):
        """
        if xxx:
            return object.__new__(cls)
        else:
            return 上一次创建的对象的引用
        """
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

    def __init__(self, name):
        self.name = name


s_a = SingleDog("旺财")
print(id(s_a)) #4307525304
print(s_a.name)
s_b = SingleDog("哮天犬")
print(id(s_b)) #4307525304
print(s_b.name)
# output:
# 4485369696
# 旺财
# 4485369696
# 哮天犬

# 这说明，new和init是分开的。但接下来我想让两个的name都变成一样的。init指向了两次，两次都修改了内存里的name。
#     def __init__(self, name):
#         self.name = name # 只要保证这里，只有第一次执行，第二次不执行即可。


# 5-只初始化一次对象2
class SingleDog2(object):

    # 类属性(作用在类中的全局变量)
    __instance = None
    __init_flag = False
    def __new__(cls, name, *args, **kwargs):
        """
        if xxx:
            return object.__new__(cls)
        else:
            return 上一次创建的对象的引用
        """
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

    def __init__(self, name):
        if SingleDog2.__init_flag == False:
            self.name = name
            SingleDog2.__init_flag = True


s_a2 = SingleDog2("旺财")
print(id(s_a2)) #4307525304
print(s_a2.name)
s_b2 = SingleDog2("哮天犬")
print(id(s_b2)) #4307525304
print(s_b2.name)
# output:
# 4379218160
# 旺财
# 4379218160
# 旺财 # 只有第一次初始化，后面没有初始化

# 6-异常处理
# 7-异常处理基本功能
# 打开文件、用户输入、
print("")
print("异常处理")
try:
    11/0
    # 可能出错的代码放在这里。
    # FileNotFoundError: [Errno 2] No such file or directory: 'xxx.txt'
    open("xxx.txt")
    print(num)
    print("-----1-----")
except NameError:
    # 善后处理
    print("如果捕获到异常后做的 处理....")
except FileNotFoundError: # 错误的名字是指定的，不能自己随便乱取
    print("打不开文件")
# 用元组合并前两种
# except (NameError, FileNotFoundError):

except Exception as ret:   # 所有异常的一个总称
    print("如果用了Exception,那么意味着只要上面的except没有捕获到异常，这个except一定会捕获到")
    # 用ret查看异常的真正原因
    print(ret) #division by zero
else:
    print("没有异常才会执行的功能")
finally:
    # 比如，不管怎么样都要关闭文件。
    print("---finally---")
    print("不管发生异常，还是没发生异常，都会执行的功能。")

print("----2-----")# 还是会正常处理代码

print("8-异常的传递")
# 8-异常的传递
def test1():
    print("--- test1-1 ---")
    print(num)
    print("--- test1-2 ---")

def test2():
    print("--- test2-1 ---")
    # test1() # 在这里gg了
    print("--- test2-2 ---")

def test3():
    try:
        print("--- test3-1 ---")
        test1()
        print("--- test3-2 ---")
    except Exception as result:
        print("捕获到了异常，信息是：{}".format(result))
    print("--- test3-3 ---")

test3() # 这里有异常传递
print("---------华丽的分割线------------")
test2() # 程序直接崩！

# output:
# --- test3-1 ---
# --- test1-1 ---
# 捕获到了异常，信息是：name 'num' is not defined
# --- test3-3 ---
# ---------华丽的分割线------------
# --- test2-1 ---
# --- test1-1 ---


# 9-抛出自定义异常
# raise自定义的异常
class ShortInputException(Exception):
    """自定义的异常类"""
    def __init__(self, length, atleast):
        self.length = length
        self.atleast = atleast

def main(): # 没有那个if...，是不会有结果产生的。
    try:
        s = input('请输入 --> ')
        if len(s) < 3:
            # raise引发一个你定义的异常（一个类）
            raise ShortInputException(len(s),3)

    except ShortInputException as result: # x这个变量被绑定到了错误的实例
        print("ShortInputException:输入的长度是{}，长度至少应是{}".format(result.length,result))
    else:
        print("没有异常发生")

# if __name__ == '__main__':
#     main()

# 请输入 --> 2
# ShortInputException:输入的长度是1，长度至少应是3
# 请输入 --> 0074310970
# 没有异常发生.

# 10-异常处理中抛出异常
print("")
print("10-异常处理中抛出异常")
class Test(object):
    def __init__(self, switch):
        self.switch = switch # 开关
    def calc(self,a,b):
        try:
            return a/b
        except Exception as result:
            if self.switch:
                print("捕获开启，已经捕获到了异常，信息如下：")
                print(result)
            else:
                # 重新抛出这个异常，此时就不会被这个异常处理给捕获到，从而触发默认的异常处理。
                raise

a = Test(True)
a.calc(11,0)
# 捕获开启，已经捕获到了异常，信息如下：
# division by zero

# print("--------华丽的分割线------------")
# a.switch = False
# a.calc(11,0)
# ZeroDivisionError: division by zero # 报错



# 11-if的各种真假判断
# 假
if "":
    print("haha")
if None:
    print("haha")
if 0:
    print("haha")
if []:
    print("haha")
if {}:
    print("haha")

# 真
if 1: # 0表示假，非0表示真
    print("haha")
if -1:
    print("haha")
if "a":
    print("haha")

# 12-模块
# import 模块

# 13-模块
# 自定义一个模块
# 我会的
# sklearn.cpython-36.pyc是模块的缓存文件，因为cpu中只存储0/1的文件，每次都进行翻译就很麻烦。
# 找个.pyc将模块里的程序翻译为0/1之后，进行缓存，方便下次读取。提升效率。
# .pyc称为字节码

# 两种不同的使用方法
# import sendmsg
# sendmsg.test1() #haha

# from sengmsg import test1,test2
# test1() # haha

# 如果用from sengmsg import *
# 存在一个问题，如果连着两个，
# from sengmsg1 import *
# from sengmsg2 import *
# 且这两个模块中有重名的函数，那么sengmsg2会顶替掉sengmsg1中的函数。
# 也就是说只调用sengmsg2中的那个名字的函数。



print("")
print("module:")
import day11recvmsg
import day11sendmsg
day11sendmsg.test11()
day11sendmsg.test22()
day11recvmsg.recv()

"""
# 注：导入一个模块，实际上会将模块整个都执行一遍!!!
output:
recv--test1
test11
test22
test11
test22
recv--test1
"""

# 实现别人导入模块就不执行，
# 自己在当前模块做测试的执行，用'__name__'!!!!!!

# 在两个模块中都添加了if __name__ == '__main__':
# 此时，output为：
# test11
# test22
# recv - -test1
#