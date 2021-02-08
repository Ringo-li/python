# 在python中，一般用get_XX来获取私有属性，用set_XX来设置私有属性

class Master(object):
    def __init__(self):
        self.gongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'用{self.gongfu}制作煎饼果子')

class Apprentice(Master):
    def __init__(self):
        self.gongfu = '[秘制煎饼果子配方]'
        # self.money = 1000000000
        # 定义一个私有属性
        self.__money = 1000000000

    # 定义函数，获取私有属性值 get_XX
    def get_money(self):
        return self.__money

    # 定义函数，设置私有属性值 set_XX
    def set_money(self):
        self.__money = 500

    # 定义一个私有方法
    def __print_info(self):
        print('这是私有方法')

    def make_cake(self):
        print(f'用{self.gongfu}制作煎饼果子')

class Tusun(Apprentice):
    pass

# 验证
xiaoxiaoli = Tusun()
print(xiaoxiaoli.get_money())
xiaoxiaoli.set_money()
print(xiaoxiaoli.get_money())