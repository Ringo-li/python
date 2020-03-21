import random

def rai(a):
	try:
		if a >= 4:
			print('OK')		
		else:
			raise Exception('not ok') 
	except Exception as aa:
		print(aa)
		
def ran():
	try:
		b = input('your num:')
		assert  b.isdigit(),'not a num'
		b = int(b)
		for i in range(b):
			c = random.randint(1,6)
			print(c)
			rai(c)
	except Exception as aa:
		print('your num',aa)

ran()
		

