import time

start = time.time()
sum = 0

for i in range(2,10000):
	if i == 2:
		sum += 1
		continue
	for k in range(2,i):
		if i % k == 0:
			break
			
	else:
		sum += 1
end = time.time()
print(sum)
print(end - start)
