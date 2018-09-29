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
# new就是创建对象的那个人
class Dog(object):
    def __init__(self):
        print("----init方法-----")
    def __del__(self):
        print("----del方法-----")
    def __str__(self):
        print("----str方法-----")
        return "对象的描述信息"

    def __new__(cls, *args, **kwargs):
        print("----new方法-----")
        object.__new__(cls)

print(id(Dog))
xtq = Dog()







# 3-创建单例对象

# 4-只初始化一次对象


# 5-


# 6-异常处理



# 7-异常处理基本功能




# 8-异常的传递





# 9-抛出自定义异常





# 10-异常处理中抛出异常







# 11-if的各种真假判断






# 12-模块
















# 13-
