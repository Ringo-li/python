
import time

for i in range(10):
	try:
		if i < 6:
			print('you are %d yers old'%(i+10))
			i += 1
			time.sleep(1)
		else:
			raise Exception('you are so urgly')
	except Exception as res:
		print(res)
	
	else:
		print('a~')
	finally:
		print('beautiful')