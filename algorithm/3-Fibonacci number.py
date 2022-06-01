# 斐波那契数列：0 1 1 2 3 5 8 13
# f(n) = f(n-1) + f(n-2)
import time
from turtle import end_fill

def f(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return f(n-1)+f(n-2)
start_time = time.time()
print(f(35))
end_time = time.time()
print(end_time-start_time)

# 如何存储已经计算出的结果，不重复计算
# 找一个notebook,用字典dict
def f(n ,nb={}):
    if n in nb:
        return nb[n]
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        ans = f(n-1, nb)+f(n-2, nb)
        nb[n] = ans
        return ans
    
start_time = time.time()
print(f(35))
end_time = time.time()
print(end_time-start_time)

# 方法三：迭代器iterative
def f(n):
    a, b = 0, 1
    for _ in range(n-1):
        a, b = b, a+b
    return a
start_time = time.time()
print(f(35))
end_time = time.time()
print(end_time-start_time)


