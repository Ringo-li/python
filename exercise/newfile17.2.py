import random

a = random.randrange(10)
print(a)
try:
	assert(a < 6)
except AssertionError:
	print('ok')
try:
	assert(a > 6)
except AssertionError:
	print('no')