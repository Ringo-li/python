# 师傅类
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

# 徒弟类
class Apprentice(Master):
    pass

# 创建对象
xiaoli = Apprentice()

# 验证，看小李是否可以用秘籍做出古法煎饼果子
print(xiaoli.kongfu)
xiaoli.make_cake()