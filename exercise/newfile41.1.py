import time
import os

def decorater(fun):
	def fself (*ags,**kwargs):
		start = time.time()
		fun()
		end = time.time()
		timeall = end - start
		print(timeall)
		
	return fself
@decorater	
def self():
	with open('41test.txt','w') as f:
		f.write('hi man,you are so beautiful\ncan i kiss you?')
		
	try:
		if int(input('your num:')) == 3:
			raise Exception('no this file')
	except Exception:
		print('sorry')
	else:
		print('ok')	
		os.system('cat 41test*') 
	finally:
		print('finally')
		
self()