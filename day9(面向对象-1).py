# review 13 14 15 16
# 面向对象和面向过程的区别
# 函数是面向过程的
# 面向过程：根据业务逻辑从上到下写代码
# 面向对象：将数据与函数绑定到一起，进行封装，这样能够更快速的开发程序，减少了重复代码的重写过程。

# 面向对象重要概念——————类和对象
# 对象需要类才能创建出来
# 概念是类，具体的事情是对象

# 类由3个部分构成
# 类的名称：类名
# 类的属性：一组数据（属性类似于之前学的全局变量）
# 类的方法：允许对进行操作的方法（行为）

# <1>举例
# 1）人类设计，只关心3样东西
# 事物名称（类名）：人（Person）
# 属性：身高（height）、年龄（age）
# 方法（行为/功能）：跑（run）、打架（fight）

"""
# 定义一个类
class 类名：
    # 属性
    # 方法
    def xxx(self):  # 方法（在类内部定义的函数）需要写上self ！！！！！
                    # 函数，不是在类里面的，普通的def
        pass
"""

class Cat:
    """定义了一个Cat类"""
    # 属性

    # 初始化对象
    def __init__(self, new_name, new_age):
        # print("---haha---")
        self.name = new_name # self是对象里面添加的变量，所以str也可以继续使用
        self.age = new_age
#    def __str__(self):
#        return "{}的年龄是{}".format(self.name, self.age)


    # 方法
    def eat(self):
        print("猫仔吃鱼。。。")
    def drink(self):
        print("猫在喝水...")
    def introduce(self):
        # print("{}的年龄是{}".format(tom.name, tom.age))
        # 不应该用tom，应该变成用自己self
        print("{}的年龄是{}".format(self.name, self.age))


# 创建一个对象
tom = Cat("汤姆",40)

# 调用tom指向的对象中的 方法
tom.eat()
tom.drink()

# 给tom指向的对象添加2个属性
# tom.name = "汤姆"
# tom.age = 40

# print("{}的年龄是{}".format(tom.name,tom.age))
# tom.introduce() # str时注释

# 但是这样存在一个问题
lanmao = Cat("蓝猫",10)
# lanmao.name = "蓝猫"
# lanmao.age = 10
# lanmao.introduce()  # str时注释
# output:
# 猫仔吃鱼。。。
# 猫在喝水...
# 汤姆的年龄是40
# 汤姆的年龄是40 # 蓝猫的结果没有被存进去  # 这里不太懂
# 因为introduction用的是format(tom.name, tom.age)，对象是tom

"""
# 改成self之后：self是你通过哪个对象去调用，这个self就是谁
# 第一次用tom去调用类，所以self是tom；第二次用lanmao去调用类，所以self是lanmao
# self指向了自己，类似于其他语言中的this指针。
# self用来传递当前对象
# tom.introduce()# 相当于 tom.introduce(tom)
# tom指向谁self就指向谁，不传递参数的时候，python解释器自动将tom的引用传递过去，self用来接收对象。
"""

# 猫仔吃鱼。。。
# 猫在喝水...
# 汤姆的年龄是40
# 蓝猫的年龄是10

# __init__方法 ----- 13
# 在类的里面定义一个新的方法，作用是初始化对象。
# ######
# 创建对象的过程：
# 1. 创建一个对象
# 2. python会自动的调用init()方法 （多了这一步！！！魔法方法）
# 3. 返回 创建的对象的引用 给tom

# 调用init方法的流程 ----- 14


# 调用__str__方法 ---- 15
#print(tom)
#print(lanmao)
# 通过str产生的结果：
# 汤姆的年龄是40
# 蓝猫的年龄是10


# -----应用1-----：烤地瓜
# 对象结束的那一刹那，属性才结束
print("应用1")
class SweetPotato:

    def __init__(self): # 作用：初始化对象
        self.cookedString = "生的"
        self.cookedLevel = 0
        self.condiments = []

    def __str__(self):
        return "地瓜-状态：{}-{}，添加的佐料有：{}".format(self.cookedString,
                                              self.cookedLevel,str(self.condiments))

    def cook(self, cooked_time):

# 属性结束的那一刹那，方法才结束
        self.cookedLevel += cooked_time

        if self.cookedLevel >= 0 and self.cookedLevel<3:
            self.cookedString = "生的"
        elif self.cookedLevel >= 3 and self.cookedLevel<5:
            self.cookedString = "半生不熟"
        elif self.cookedLevel >= 5 and self.cookedLevel<8:
            self.cookedString = "熟了"
        elif self.cookedLevel >8:
            self.cookedString = "烤糊了"

    def addCondiments(self, item):
        self.condiments.append(item)

# 创建了一个地瓜对象
digua = SweetPotato()
print(digua)

# 开始烤地瓜
digua.cook(1)
print(digua)
digua.addCondiments("dasuan")
digua.cook(1)
print(digua)
digua.addCondiments("ziran")
digua.cook(1)
print(digua)





print("")
print("应用2")
# 应用2----：存放家具
# 把一个对象bed放到另一个对象home里面去
class Home:

    # 初始化对象
    def __init__(self,new_area,new_info,new_addr):
        self.area = new_area
        self.info = new_info
        self.addr = new_addr
        self.left_area = new_area
        self.contain_items = []


    def __str__(self):
        msg = "房子的总面积是{}，剩余面积是{}，户型是{}，地址是{}".format(self.area,
                                                      self.left_area,self.info,self.addr)
        msg += " 当前房子里的物品有：{}".format(str(self.contain_items))
        return msg

    def add_item(self,item):  # item是bed类，self指向home
        # self.left_area -= item.area
        # self.contain_items.append(item.name)
        self.left_area -= item.get_area()
        self.contain_items.append(item.get_name())


class Bed:
    def __init__(self, new_name, new_area):
        self.name = new_name
        self.area = new_area

    def __str__(self):
        return "{}占用的面积是：{}".format(self.name,self.area)

    def get_name(self): # self指向bed
        return self.name

    def get_area(self):
        return self.area



appartment = Home(129,"三室一厅","北京市 朝阳区 长安街 666号")
print(appartment)

bed1 = Bed("席梦思",4)
print(bed1)

appartment.add_item(bed1)
print(appartment)


bed2 = Bed("三人床",3)
appartment.add_item(bed2)
print(appartment)





















































