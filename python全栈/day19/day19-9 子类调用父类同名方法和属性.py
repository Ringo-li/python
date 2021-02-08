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
        # 调用父类同名属性和方法后，子类属性及方法会被覆盖，需要重新调用
        self.__init__()
        print(f'利用{self.kongfu}制作煎饼果子')

    # 子类调用父类同名属性和方法，把父类属性和方法再封装
    def mater_make_cake(self):
        # 父类类名.函数(self)
        # 因为是新实例对象调用，所有要将实例对象self传进来,调用父类的属性和方法
        Master.__init__(self)
        Master.make_cake(self)
    
    def school_make_cake(self):
        
        School.__init__(self)
        School.make_cake(self)


# 创建对象
xiaoli = Apprentice()

# 验证
xiaoli.make_cake()
xiaoli.mater_make_cake()
xiaoli.school_make_cake()
xiaoli.make_cake()