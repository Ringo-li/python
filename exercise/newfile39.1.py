alist = [[1,2],[3,4],[5,6]]

print(alist)

print([j for i in alist for j in i])

blist = [[[1,2],[3,4]],[[5,6],[7,8]],[[9,10],[11,12]]]
print(blist)
print([k for i in blist for j in i for k in j] )

import numpy as np

b = np.array(alist)
c = b.flatten()
d = c.tolist()
print(b,type(b))
print(c,type(c))
print(d,type(d))
print(np.array(blist).flatten().tolist())