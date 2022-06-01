# 3! = 1 x 2 x 3 = 6
# 4! = 3! x 4 = 24
# 给定一个数，24，求是几的阶乘
# def invFatorail(n):
#     if n <= 0:
#         return -1
#     if n == 1:
#         return 1
#     i = 2
#     s = 1
#     while s < n:
#         s = s * i
#         i += 1
#     return i-1 if s == n else -1

# print(invFatorail(120))



def inFatorail(n):
    s = 2
    while n >= 2:
        if n % s == 0:
            n /= s
            s += 1
        else:
            return -1
    return s - 1
print(inFatorail(24))