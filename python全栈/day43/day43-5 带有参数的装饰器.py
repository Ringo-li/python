
def return_decorator(flag):
    # 装饰器的定义就是只能传入一个参数且是函数
    # 为了让装饰器有参数，可以再次进行封装
    def decorator(func):
        def inner(a, b):
            if flag == "+":
                print("正在执行加法运算，结果为：")
                func(a, b)
            if flag == "-":
                print("正在执行减法运算，结果为：")
                func(a, b)
        return inner
    # 调用函数时返回一个装饰器
    return decorator

@return_decorator("+")   
def add_num(a, b):
    print(a + b)

@return_decorator("-")
def sub_num(a, b):
    print(a - b)

add_num(1, 2)
sub_num(1, 2)