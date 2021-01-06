def dome1(a,*aa):
	print(a)
	for i in aa:
		print(i)
dome1(1,2,3,4,5)

def dome2(**bb):
	for x,y in bb.items():
		print(x,y)

dome2(name = 'yeye',age = 13)

adict = {'name':'yeye','age':18}
print(adict.keys())
print(list(adict.items())[0][1])
print(list(adict.values()))
for x,y in adict.items():
	print(x,y)
