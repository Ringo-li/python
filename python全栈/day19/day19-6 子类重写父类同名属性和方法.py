# 师傅类
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

# 培训学校类
class School(object):
    def __init__(self):
        self.kongfu = '[流行煎饼果子配方]'

    def make_cake(self):
        print(f'利用{self.kongfu}制作煎饼果子')


# 徒弟类，继承学校和师傅类，添加与父类相同的属性和方法
class Apprentice(School, Master):
    def __init__(self):
        self.kongfu = '[秘制煎饼果子配方]'

    def make_cake(self):
        print(f'利用{self.kongfu}制作煎饼果子')

# 创建对象
xiaoli = Apprentice()

# 验证
print(xiaoli.kongfu)
xiaoli.make_cake()

# 结论：如果子类和父类有相同属性和方法，子类调用到的是自己的属性和方法

print(Apprentice.__mro__)