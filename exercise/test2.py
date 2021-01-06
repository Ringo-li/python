
def abc():
	a = 5
	global b 
	b = 5
abc()
print(b)
#print(a)
adict = {'a':1,'b':2,'c':3}
print(adict)
del(adict['a'])
print(adict)

bdict = {'aa':10,'bb':20,'cc':30}
print(bdict)
cdict = bdict.update(adict)
print(cdict,bdict,adict)

alist = [1,2,3,1,2,4]
aset = set(alist)
print(aset)
blist = list(aset)
print(blist)
clist = [i for i in aset]
print(clist)

