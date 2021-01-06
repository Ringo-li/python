alist = [1,2,3,4,5]

def fn(a):
	return a ** 2
	
blist = map(fn,alist)
print([i for i in blist if i > 10])
	