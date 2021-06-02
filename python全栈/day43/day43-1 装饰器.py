# 装饰器作用：对已有函数进行额外功能扩展，本质上是一个闭包函数，也是一个函数嵌套
# 装饰器的执行时机：装饰器在加载代码时已经执行

# 装饰器特点：
# 1.不修改已有函数的源代码
# 2.不修改已有函数调用方式
# 3.给已有函数添加额外功能

def decorator(func): # 如果一个闭包函数有且仅有一个函数参数，那这个闭包函数称为装饰器
    def inner():
        # 在内部函数对已有函数进行调用
        print("装饰器已经执行了") # 测试装饰器的执行时机：作为模块导入时，不用执行comment函数，装饰器在加载代码时已经执行
        print("添加登录验证")
        func()
    return inner

@decorator # 等价于comment = decorator(comment)， comment=inner
def comment():
    print("发表评论")


# 要让comment函数实现以下功能
# 1.添加登录验证
# 2.发表评论
# 3.调用方式不变
# 调用装饰器对comment进行装饰,此时comment=inner当然可以用魔法糖@简写
# comment = decorator(comment)
comment()
