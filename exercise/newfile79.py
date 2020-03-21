import random

alist = [ i for i in range(10)]
print(alist,type(alist))

scq = (i for i in range(10))
print(scq,type(scq))
print(next(scq))
print(next(scq))

for i in scq:
	print(i)
adict = {i:random.randint(4,9) for i in ('a','b','c','d')}
print(adict)