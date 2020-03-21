foo = [{"name":"zs","age":19},{"name":"IV","age":54},{"name":"wa","age":17},{"name":"rlf","age":34}]

a = sorted(foo,key=lambda x:x['name'],reverse=True)
print(a)

foo = [('zs',43),('ls',32),('wmz',37),('dzt',45)]

a = sorted(foo,key=lambda x:x[0])
print(a)
a = sorted(foo,key=lambda x:x[1],reverse=True)
print(a)