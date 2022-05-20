# data structure, a kind of structure to hold data
# 堆栈，一种data structure, stack like plates, FILO，first in last out
# 例题：反转一个列表
lst = [1, 2, 3, 4]
def rev(lst):
    resault = []
    while len(lst) > 0:
        tmp = lst.pop()
        resault.append(tmp)
    return resault

print(rev(lst))