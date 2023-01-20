# 定义：函数调用自身
# 用法：
    # 定义一个基础条件
    # 调用自身
# 例题：如阶乘

def f(n):
    '''
    用于返回一个数的阶乘结果
    '''
    if n == 1:
        return 1
    else:
        return n*f(n-1)
print(f(4))