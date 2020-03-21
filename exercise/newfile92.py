#int(1.4)和int('1.4')

a = float(input('num:'))
print(int(a))
print(a)

try:
	print(int(str(1.5)))
except ValueError :
	print('错误的值')