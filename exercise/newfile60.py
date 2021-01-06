a = ('a','b','c','d')
b = (1,2,3,4)
c = zip(a,b)
print(c)
a0 = dict(c)
a1 = list(range(10))
a2 = [i for i in a1 if i in b]
a3 = [a0[s] for s in a0]
print(a0)
print(c)
print(dict(c))
print(a1)
print(a2)
print(a3)
#print(list(set(2,3,7)))
aset = (1,2,4)
print(list(aset))
#zip的内容在被调用后会在内存中释放?
c = zip(a,b)
a4 = list(c)
print(a4)


#用dict加工有两个元素的元组或列表

adict = dict([('hdhf','1'),('two',2)])
print(adict)

bdict = dict((('one',1),('two',2)))
print(bdict)

cdict = dict([['one',1],['two',2]])
print(cdict)