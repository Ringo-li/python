import time

def decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func()
        end_time = time.time()
        print(end_time - start_time)

    return wrapper

@decorator 
def func():
    time.sleep(0.8)

func() # 函数调用
# 输出：0.800644397735595