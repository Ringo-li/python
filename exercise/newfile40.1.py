
a = 'abc'
b = 'def'
c = ('g','h','i','j')
d = ['k','l','m']

res1 = a.join(b)
print(res1)
res2 = a.join(c)
print(res2)
#res3 = d.join(c)
#print(res3)
import numpy as np
a1 = np.array(c)
print(a1)
b1 = a1.flatten()
print(b1)
c1 = a1.tostring()
d1 = c1.decode()
e1 = d1.encode()
print(c1,type(c1))
print(d1,type(d1))
print(e1,type(e1))

print(d1,c)
print(a.join(d1),a.join(c))
print(a + d1)
print(d1,type(d1),[d1],[b])
print(a.join(list(d1)))