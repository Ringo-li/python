
a = 10
print('全局a',a)
def gloarg():
	global a
	a = 12
	print('函数a',a)
	
print('全局a',a)
print('执行函数')
gloarg()
print('全局a',a)

