# 目标：定义init魔法方法，设置初始化属性，并访问调用
"""
1.定义类
    init魔法方法，添加属性
    访问属性方法

2.创建实例对象
3.验证成果
    调用访问属性方法
"""

class Washer():
    def __init__(self):
        # 添加实例属性
        self.width = 500
        self.height = 800

    def print_info(self):
        print('我的高度是{}'.format(self.height))
        print('我的宽度是{}'.format(self.width))

haier = Washer()
haier.print_info()
