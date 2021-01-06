#zip函数，传入多个可迭代对象，以最短对象组合成元组
a = [1,2,3,4]
b = (7,8,9)
c = zip(a,b)
d = [i for i in c]
for i in d:
	print(i)
print(d,type(c),type(d))