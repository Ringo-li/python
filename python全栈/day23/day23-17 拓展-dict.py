# 1.定义一个类
class A(object):
    aa = 0

    def __init__(self):
        self.b = 1

# 2.实例化类
a = A()

# 3.调用__dict__方法
print(a.__dict__)
print(A.__dict__)