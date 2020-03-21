alist = [1,3,2,4]
blist = [4,5,3,6]

#交集
jj1 = [i for i in alist if i in blist]
print('交集',jj1)
jj2 = list(set(alist).intersection(set(blist)))
print('交集',jj2)

clist = [1,2,3,2]
print('列表',clist)
print('列表转元组',set(clist))



#并集
bj = list(set(alist).union(set(blist)))
print('并集',bj)

#差集
cj1 = list(set(alist).difference(set(blist)))
print('差集',cj1)
cj2 = list(set(blist).difference(set(alist)))
print('差集',cj2)
