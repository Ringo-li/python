#generator

def fibonacci(n): # 生成器函数 - 斐波那契
    c, d, counter = 0, 1, 0
    while True:
        if counter > n :
            return
        yield c
        c, d = d, c + d
        counter += 1

f = fibonacci(30) #获得一个迭代器

while True:
    try:
        print( next(f), end=" ")
    except StopIteration:
        break