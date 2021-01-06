def fn(a,b,c={}):
	c[a]=b
	print(c)
print(fn('one',1))
print(fn('two',2))
print(fn('haha',0))
print(fn('three',3,{}))
print(fn('four',4,{'five':5}))
