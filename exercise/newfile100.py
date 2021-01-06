def selfadd(a):
	a += a
	return a
	
a1 = 2
print(a1)

a1add = selfadd(a1)
print(a1add)
print(a1)

alist = [1,2]
print(alist)
alistadd = selfadd(alist)
print('可变对象自加结果',alistadd)
print('可变对象自加后自己被改变',alist)

aset = (1,2)
print(aset)
asetadd = selfadd(aset)
print('不可变对象自加结果',asetadd)
print('不可变对象自加后自己不会改变',aset)