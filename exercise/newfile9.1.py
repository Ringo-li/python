import time,random


def timesum(fun):
	def decorater(*a,**aa):
		start = time.time()
		fun()
		end = time.time()
		print(end - start)
		
	return decorater
		
@timesum
def dicttr():
	times = input('you want:')
	tim =random.randint(1,101)
	for i in range(tim):
		print(i , 'is good')
	time.sleep(1)

	

dicttr()