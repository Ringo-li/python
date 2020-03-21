

try:
	a = input('your numb:')
	assert a.isdigit(),'not ok'
	a = int(a)	
except Exception as ex:
	print('your num is',ex)



	
#assert a < 3
#print('everything is all right')

try:
	assert a > 2,'are you kiding me'
	
except AssertionError as bb:
	print(bb,'ok,slow down')

#assert(a > 2)
#print('are you kiding me')
