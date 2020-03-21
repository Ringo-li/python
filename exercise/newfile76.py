foo = [['zs',42],['ls',35],['wmz',32],['bzt',32],['qxy',32]]

a = sorted(foo,key=lambda x:x[0],reverse=True)
print(a)

a = sorted(foo,key=lambda x:x[1])
print(a)

a = sorted(foo,key=lambda x:(x[1],x[0]))
print(a)