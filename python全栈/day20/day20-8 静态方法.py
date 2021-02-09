# 1.定义类：定义静态方法
class Dog(object):
    @staticmethod
    def info_print():
        print('这是一个静态方法')

# 2.创建对象
wangcai = Dog()

# 3.用类和实例分别调用静态方法
wangcai.info_print()
Dog.info_print()