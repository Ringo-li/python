import  time
import subprocess as sp
import os

try:
	if os.path.exists('./f36.2.txt'):
		raise Exception('has exists file')
except Exception as a:
	print('exist file,has removed',a)
	os.remove('./f36.2.txt')
if os.path.exists('./36.2.txt'):
	print('exists')

	
with open('f36.2.txt','w') as f:
	f.write('hello\nworld\nyou\r\n \nare\nso\nbeaytiful')


try:
	a = open('f36.2.txt')
#	b = a.readline()
#	print(b)
#	a.close()
#	print(a.read())
	try:
		while True:
			content = a.readline()
			if len(content) == 0:
				break
			time.sleep(0.5)
			print(content)
	finally:
		time.sleep(1)
		a.close()
		print('\n\nclose the file')
except:
	print('file not here')
sp.call('cat f36.2.txt',shell=True)
