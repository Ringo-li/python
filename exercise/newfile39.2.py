alist = [[1,2],[3,4],[5,6]]
print([ i for j  in alist for i in j])


blist = [[[1,2],[3,4]],[[5,6],[7,8]],[[9,10],[11,12]]]

print([i for k in  blist for j in k  for i in j])

import numpy as np 

clist = np.array(blist).flatten().tolist()
print(clist)

