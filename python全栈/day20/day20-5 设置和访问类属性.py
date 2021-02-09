# 定义类属性
class Dog(object):
    tooth = 30

# 创建对象
wangcai = Dog()
xiaohei = Dog()

# 用类和对象调用类属性
print(Dog.tooth)
print(wangcai.tooth)
print(xiaohei.tooth)