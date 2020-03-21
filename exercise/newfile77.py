foo = {'name':'zs','age':34,'sex':'male','city':'bj'}

foozip = zip(foo.keys(),foo.values())
print(foozip,type(foozip))
foolist = [i for i in foozip]
print(foolist)
a = sorted(foolist,key=lambda x:x[0])
print(a)
foodic = dict(a)
print(foodic)

foodicnew = {i[0]:i[1] for i in a}
print(foodicnew)