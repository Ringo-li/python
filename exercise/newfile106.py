import time

class car(object):
	
	def __init__(self,name):
		print('init has been used')
		self.__name = name
		
	def __del__(self):
		print('del has been used')
		time.sleep(1)
		print('%s has been killed'%self.__name)
		
car1 = car('bus')
car2 = car1
car3 = car1
print(id(car),id(car2),id(car3))
print('car1 will be killed')
del(car1)
time.sleep(1)
print('car2 will be killed')
time.sleep(1)
del(car2)
print('car3 will be killed')
del(car3)
del(car)
		
		
