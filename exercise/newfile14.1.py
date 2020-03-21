from  random import *
import numpy as np

a = randint(2,4)
a1 = randrange(1,3)
print(a)
print(a1)


b = random()
print(b)
print(round(b,2))

c = uniform(1,3)
print(c)
print(round(c,2))

items = ['aa','bb','cc','dd']
d = choice(items)
print(d)

eshuffle = shuffle(items)
print(items)

fsample = sample(items,2)
print(fsample)

npa = np.random.randn()
print(npa)
print(round(npa,3))