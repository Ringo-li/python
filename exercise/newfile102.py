import random


b = 0
while b <= 10:
	a = random.randint(1,100)
	c = random.random()*100
	d = random.choice(range(1,101))
	e = random.uniform(2,3)
	print(a)
	print(round(c,2))
	print(d)
	print(round(e,2))
	b += 1
	
	
