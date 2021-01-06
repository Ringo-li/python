alist = []
a = 0
while True:
	if a <= 3 :
		val = input('please give me your num:')
		alist.append(val)
		a += 1
		print(a)
	else:
		break
alist.append(4)	
print(alist)
numlist = list(map(int,alist))
print(numlist)