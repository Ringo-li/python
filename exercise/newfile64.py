#python中的false
a0 = False
a1 = None
a2 = ()
a3 = {}
a4 = []
a5 = 0
a6 = ''
a7 = 1
print(bool(a0))
print(bool(a1))
print(bool(a2),bool(a3),bool(a4),bool(a5),bool(a6))
print(bool(a7))

b1 = [True,False]
print(any(b1),all(b1))

b2 = ('','')
print(any(b2),all(b2))

b3 = {'one':1,'':''}

print(any(b3),all(b3))

print(any('b3'),all('b3'))
