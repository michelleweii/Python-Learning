# 1-隐藏属性
# 用属性设置不能做判断，用方法替代直接获取属性的方式。
class Dog:
    def set_age(self, new_age):
        if new_age>0 and new_age<=100:
            self.age = new_age
        else:
            self.age = 0

    def get_age(self):
        return self.age # day9中有关于这里是否是全局变量的解释。。。


dog = Dog()
# 直接对对象进行修改存在一定的风险，如果age=-10，也会直接print(dog.age)
# dog.age = 10
# dog.name = "xiaobai"
# dog.get_name()
# dog.get_age()
# 两种方法都可以获取到age和name，但用方法更好
dog.set_age(-10)
age = dog.get_age()
print(age) #0

# 2-私有方法
# 加两个下划线__称为私有方法，比较重要，不想让其他用户直接使用。
# 开发的时候真正的思想，先做一些判断，是否满足再调用函数，
class Valid:
    # 私有方法
    def __send_msg(self):
        print("....正在发送短信....")

    # 公有方法
    def send_msg(self, new_money):
        if new_money>10000:
            self.__send_msg()
        else:
            print("余额不足，请充值")
valid = Valid()
# valid.__send_msg() #AttributeError: 'Valid' object has no attribute '__send_msg'
valid.send_msg(100) #余额不足，请充值
valid.send_msg(100000) #....正在发送短信....

# 3-__del__方法
class Dog:
    # 在内存删除（对象真正的临死之前）的时候，自动调用del()方法。
    def __del__(self): # 程序临死前的善后工作。
        print("---英雄over----")

dog1 = Dog()
dog2 = dog1
del dog1
del dog2
print("===============")
# 只是删除了dog1这个名字的引用，dog2还存在，所以内存中还有Dog()

# output: 无del dog2
# =============== # 意味着还有引用，内存还在，但是没有代码了，程序退出，程序在运行期间占用的内存都要还给操作系统。
# ---英雄over----

# output: del dog2
# ---英雄over----
# ===============


# 4-测量对象的引用个数
import sys
# sys.getrefcount() # 测量对象的引用计数是几（比实际个数多一个，因为调用的时候也传递了一个）
class T:
    pass
t = T()
print(sys.getrefcount(t)) #2
tt = t
print(sys.getrefcount(t)) #3
del tt
print(sys.getrefcount(t)) #2

# 5-继承
# 6- 新的类继续继承子类
# 7-重写
# 比如说哮天犬是狂叫，不是普通的叫
# 8-调用被重写的方法

# 子类（派生类）继承 父类（基类）
class Animal:
    def eat(self):
        print("-----吃------")
    def drink(self):
        print("-----喝-----")
    def sleep(self):
        print("-----睡------")
    def run(self):
        print("-----跑------")

class Dog2(Animal): # 继承
    """
    def eat(self):
        print("-----吃------")
    def drink(self):
        print("-----喝-----")
    def sleep(self):
        print("-----睡------")
    def run(self):
        print("-----跑------")
    """
    def bark(self):
        print("-----汪汪叫------")

class xiaotq(Dog2): # 6-继承子类
    def bark(self): # 7-重写（有就用自己的<和父类名字一样>，没有就去找父亲的）
        print("-----狂叫------")
    # 如果哮天犬只有第一声是狂叫，后面又是普通的狗叫
    # 再回去调用父类
        # 第1种，调用被重写的父类的方法
        # Dog2.bark(self)  # 8-调用被重写的父类的方法，self必须加
        # 第2种，
        super().bark()

    def fly(self):
        print("-----飞------")

class Cat(Animal):
    def catch(self):
        print("-----抓老鼠------")
# wangcai只能使用Dog2，Animal类中的方法，不允许出现使用Cat类的方法。
wangcai = Dog2()
wangcai.sleep() #-----睡------
tom=Cat()
tom.catch() #-----抓老鼠------
tom.run() #-----跑------

# 6 拥有前面all（多次继承）加起来的所有功能
xiaotq = xiaotq()
xiaotq.fly() #-----飞------
# 8-output：
# -----狂叫------
# -----汪汪叫------
xiaotq.bark() #-----汪汪叫------ # 7 -----狂叫------
xiaotq.run() #-----跑------


# 9-私有方法、私有属性在继承中的表现（私有方法和属性不会被继承）
# 私有方法并没有被继承下来
# （如果调用的是 继承的父类中的共有方法，可以在这个共有方法中访问父类中的私有属性和私有方法）
# （但是，如果在子类中实现了一个公有方法，那么这个方法是不能够调用继承的父类中的私有方法和私有属性的）
class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200
    def test1(self):
        print("test1")
    def __test2(self):
        print("test2")

    def test3(self):# 让子类调用
        self.__test2()# 让子类调用
        print(self.__num2)# 让子类调用

class B(A):
    def test4(self):
        self.__test2()
        print(self.__num2)
    # pass


b = B()
b.test1() #test1
# 私用方法并不会被继承
# b.test2() #AttributeError: 'B' object has no attribute 'test2'
print(b.num1) #100
# 私有属性不会被继承
# print(b.num2)#AttributeError: 'B' object has no attribute 'num2'

# 但是调用了父类的公用方法，父类的公有方法里面有调用了私有方法，私有属性，
# 那么，可以调用
b.test3() # 使用成功！！！
#output:
# test2
# 200

# but!
# b.test4() # 子类自己声明一个公有方法，调用父类里的私有属性和私有方法就gg了o(╥﹏╥)o
# output:
# self.__test2()
# AttributeError: 'B' object has no attribute '_B__test2'



# 10-多继承(之前都是单继承)
class Base(object): # python默认继承object
    def test(self):
        print("---Base")

class A(Base):
    def test1(self):
        print("---test1")
class B(Base):
    def test2(self):
        print("---test2")
class C(A,B):
    pass

c = C()
c.test1() #---test1
c.test2() #---test2
c.test() # 老祖宗 #---Base



# 11-多继承注意点


# 12-多态

# 13-多态-强调

# 14-多态的理解


# 15-类属性、实例属性

# 16-实例方法、类方法、静态方法