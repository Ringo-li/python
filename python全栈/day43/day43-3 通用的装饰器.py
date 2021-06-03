# 通用的装饰器，可以装饰任意类型的函数（有无参数，有无返回值）

# # ----------------一、装饰带有参数的函数------------------
# # 定义一个装饰器
# def decorator(func):
#     # 装饰器类型和被装饰函数要一致，需要2个参数
#     def inner(a, b):
#         # 在内部函数对已有函数进行装饰
#         print("正在努力进行加法计算中。。。")
#         func(a ,b)
#     return inner

# # 用语法糖方式对函数进行装饰
# @decorator # add_num  = decorator(add_num), add_num = inner
# def add_num(num1, num2):
#     result = num1 + num2
#     print("结果为：", result)

# add_num(1 ,2)

# # ----------------二、装饰带有参数有返回值的函数------------------
# # 定义一个装饰器
# def decorator(func):
#     # 装饰器类型和被装饰函数要一致，需要2个参数和返回值
#     def inner(a, b):
#         # 在内部函数对已有函数进行装饰
#         print("正在努力进行加法计算中。。。")
#         # 返回值给inner，就是装饰后的add_num
#         num = func(a ,b)
#         return num
#     return inner

# # 用语法糖方式对函数进行装饰
# @decorator # add_num  = decorator(add_num), add_num = inner
# def add_num(num1, num2):
#     result = num1 + num2
#     return result

# result = add_num(1 ,2)
# print(result)

# ----------------三、装饰带有不定长参数且有返回值的函数------------------
# 定义一个装饰器
# 该装饰器可以成为通用装饰器
def decorator(func):
    # 装饰器类型和被装饰函数要一致，需要不定长参数和返回值
    def inner(*args, **kwargs):
        # 在内部函数对已有函数进行装饰
        print("正在努力进行加法计算中。。。")
        # 返回值给inner，就是装饰后的add_num
        num = func(*args, **kwargs)
        return num
    return inner

# 用语法糖方式对函数进行装饰
@decorator # add_num  = decorator(add_num), add_num = inner
def add_num(*args, **kwargs):
    result = 0
    # args: 元组类型
    # kwargs: 字典类型
    for value in args:
        result += value
    
    for value in kwargs.values():
        result += value

    return result

result = add_num(1 ,2, 3, a=2, b=3)
print(result)