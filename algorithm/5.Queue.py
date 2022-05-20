# data structure, a kind of structure to hold data
# 队列，一种data structure, 顾名思义，排队，先到先得， FIFO，first in first out
# 例题：依次返回一个列表各数的平方
lst = [1, 2, 3, 4, 5]
def sqr(lst):
    resault = []
    while len(lst) > 0:
        tmp = lst.pop(0)
        resault.append(tmp*tmp)
    return resault

print(sqr(lst))
