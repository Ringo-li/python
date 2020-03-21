import time
import random
class Lib(object):
	def __new__(cls,*args,**kwargs):
		print('new has been used')
		return object.__new__(cls,*args,**kwargs)
		
	def __init__(self):
		print('init has been used')
		
	def sty(self,a):
		if a <= 10:
			print('small')
		elif a <=20:
			print('middle')
		else:
			print('big')
		
libs = Lib()

li = libs.sty(30)

def der(func):
	def war(*argd,**kwargs):
		start = time.time()
		func()
		end =time.time()
		print(end -start)
		
	return war
	
@der

def lib():
	for i in range(2):
		sum = random.randint(1,100)
		li = Lib()
		li.sty(sum)
		time.sleep(1)
	
lib()