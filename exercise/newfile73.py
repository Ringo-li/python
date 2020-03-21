from functools import reduce

alist = [1,-5,-8,3,-15,8,4,34,76,3,48,64,-7,6,-9,53]
print(alist)
blist = sorted(alist,key=lambda x:(x<0,abs(x + 1)))
clist = list(filter(lambda x:x % 3 == 0,alist))
print(blist)
print(clist)

clist = reduce(lambda a, b: '{}, {}'.format(a,b), [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(clist)