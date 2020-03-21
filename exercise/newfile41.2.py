def decorater(fun):
	def shell(*args,**kwargs):
		print('start')
		fun()
		print('end')
	return shell

@decorater
def trytest():

	try:
		num = int(input('you num:'))	
	except Exception:
		print('need a num')	
	else:
		if num > 37:
			print('need <= 37')	
		else:
			print('ok')
		
	finally:
		print('good job')
		
trytest()
