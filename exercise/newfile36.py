def fn():
	try:
		for i in range(5):
			if i < 3:
				print('so nice')
			else:
				raise Exception('OK,you win')
	except Exception as ret:
		print(ret)

fn()