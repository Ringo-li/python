# super用法：
# 1.有参数，有缺陷，父类名变化后要修改代码
# super(父类名, self).函数()
# 2.无参数，自动查找父类，调用__mro__，比较适合单继承
# super().函数()

# 如果想调用祖父类的方法，需要父类在该方法中也加入super().函数()

class Master(object):
    def __init__(self):
        self.gongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'用{self.gongfu}制作煎饼果子')

class Apprentice(Master):
    def __init__(self):
        self.gongfu = '[秘制煎饼果子配方]'

    def make_cake(self):
        print(f'用{self.gongfu}制作煎饼果子')

        # 2.1super带参数写法
        # super(Apprentice, self).__init__()
        # super(Apprentice, self).make_cake()

        # 2.2super不带参数用法
        super().__init__()
        super().make_cake()

class Tusun(Apprentice):
    # 一次调用父类和祖父类属性及方法
    
    def old_make_cake(self):
        # 方法一：逐一指定，缺点：代码量大，一个父类要写一个封装，且修改父类名要修改代码
        # Master.__init__(self)
        # Master.make_cake(self)
        # Apprentice.__init__(self)
        # Apprentice.make_cake(self)

        # 方法二：super()
        # 2.1有参数的super写法super(当前类名,self).函数()
        # 发现无法调用父类，只调用了祖父类的属性和方法，需要在父类中也添加super方法
        # super(Tusun, self).__init__()
        # super(Tusun, self).make_cake()

        # 2.2无参数super
        super().__init__()
        super().make_cake()

# 验证
xiaoxiaoli = Tusun()
xiaoxiaoli.old_make_cake()