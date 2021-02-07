# 继承：子类默认继承父类所有属性和方法

# 用基类定义父类
class A(object):
    def __init__(self):
        self.num = 1
    
    def print_info(self):
        print(self.num)

# 定义子类，继承父类
class B(A):
    pass

# 创建对象，验证结论
b = B()
b.print_info()