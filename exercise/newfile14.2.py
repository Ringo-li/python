import random
import numpy as np
import datetime


a = random.randint(3,10)
print(a)
b = random.random()
print("%.02f"%b)
print(round(b,2))
c = np.random.randn(3)
print("%.2f"%c[2])
print("{1:.2f}".format(c[1],c[2]))


