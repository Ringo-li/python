# 类装饰器，使用类装饰已有函数
class MyDecorator(object):
    def __init__(self, func):
        self.__func = func

    # 实现__call__方法，让实例对象变为像函数一样的可调用对象
    def __call__(self, *args, **kwds):
        # 对已有函数进行封装
        print("课已经讲完了")
        self.__func()

@MyDecorator # MyDecorator => show = MyDecorator(show)
def show():
    print("可以放学了！")

# 执行show 就等于执行MyDecorator创建的实例对象 
show()