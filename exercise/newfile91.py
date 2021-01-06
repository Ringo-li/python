import time

class animal(object):
	def __init__(self,name):
		print('init方法被调用')
		self.__name = name
	def __del__(self):
		print('del方法被调用')
		print('%shas be killed'%self.__name)

user = input('your animal:')				
cat = animal(user)
cat1 = cat
cat2 = cat1


print(id(cat),id(cat1),id(cat2))
print('first object will be killed')
del cat
print('second object will be killed')
del cat1
print('third object will be killed')
del cat2
print('you will kill yourself  2 seconds late ')
time.sleep(2)
