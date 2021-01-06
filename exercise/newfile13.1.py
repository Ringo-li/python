#alist = [1,2,3,4,5,]
#def func(a):
#	a = a**2
#	return a
#blist = map(func,alist)
#res = [i for i in blist if i >= 16]
#print(res)
#print(list(i for i in blist if i >= 16))

import random
import time

def dec(fun):
	def obj(*args,**kwargs):
		star = time.time()
		fun()
		end = time.time()
		tim = end - star
		print(tim)
		
	return obj

	
def fun(args):
	if args > 50:
		return ('sheep')
	if args < 50:
		return ('dog')
	else:
		return ('master')

@dec

def aa():
	
	num = input('nums:')
	alist = []
	
	try:
		for i in range(int(num)):
			alist.append(random.randint(1,101))	
		print(alist)
		blist = list(map(fun,alist))
#		print(blist)
	except ValueError:
		print('please input a num')
		
	print([i for i in blist if i == 'master'])
	
aa()
