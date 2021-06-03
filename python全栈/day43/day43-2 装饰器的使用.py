# 定义装饰器
import time

def decorator(func):
    def inner():
        # 内部函数对已有函数进行装饰
        begin = time.time()
        func()
        end = time.time()
        result = end - begin
        print("执行完成，耗时：", result)

    return inner

@decorator  # work = decorator(work), work =  inner
def work():
    for i in range(10000):
        print(i)

work()