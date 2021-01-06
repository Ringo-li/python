foo = {'name':'zs','age':34,'sex':'male','city':'bj'}


a = set(foo.keys())
b = list(foo.values())
print(a)
print(b)

print(foo.items())
a = sorted(foo.items(),key=lambda x:x[0])
print(a)

newfoo = {i[0]:i[1] for i in a}
print(newfoo)