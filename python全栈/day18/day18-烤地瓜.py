"""
# 两条主线：
# 1.炒土豆丝和时间的关系
# 2.根据口味放佐料

以面向对象的模式思考方案：
需求涉及的事务：就一个：土豆丝，涉及的类：也是一个：土豆丝类
定义类：
1.土豆丝的属性（init）
被炒时间
土豆丝状态
添加的佐料
2.土豆丝的方法（def）
炒土豆丝
加佐料
3.显示对象信息（str）
"""
class PotatoFloss():
    def __init__(self):
        # 被炒时间
        self.cook_time = 0
        # 土豆丝状态
        self.cook_stat = '生的'
        # 调料列表
        self.condiments = []
    
    def cook(self, time):
        """炒土豆丝方法"""
        # 1.先计算整体炒土豆丝时间
        self.cook_time += time
        # 2.用整体时间判断土豆丝状态
        if self.cook_time < 3:
            self.cook_stat = '生的'
        elif self.cook_time < 5:
            self.cook_stat = '脆的'
        elif self.cook_time < 8:
            self.cook_stat = '绵的'
        else:
            self.cook_stat = '糊的'

    def add_condiments(self, condiment):
        """用户添加调料列表"""
        self.condiments.append(condiment)

    def __str__(self):
        # 定义str魔法方法，确保在打印对象信息时返回的不是内存地址而是return的返回值
        return '土豆丝炒了{}分钟,现在状态是{},调料有{}'.format(self.cook_time, self.cook_stat, self.condiments)        

# 创建对象，测试实例属性和方法
potato1 = PotatoFloss()
print(potato1)
potato1.cook(2)
potato1.add_condiments('盐')
potato1.cook(2)
potato1.add_condiments('胡椒')
potato1.add_condiments('鸡精')
potato1.add_condiments('味精')
print(potato1)
potato1.cook(1)
potato1.add_condiments('小葱')
print(potato1)