# 线性搜索：一种暴力搜索方式，遍历所有情况
# 例题：开平方
from turtle import right


def line_sqrt(n):
    for i in range(n):
        if i * i == n:
            return i
        elif i * i > n:
            return


# print(line_sqrt(10))

# 二分搜索：每次排除一半的可能性
def binary_sqrt(n):
    left = 0
    right = n
    while left <= right:
        mid = (left+right)//2

        if mid * mid ==  n:
            return mid
        elif mid * mid > n:
            right = mid + 1
        else:
            left = mid - 1
            
print(binary_sqrt(25))



