import time
import os
import multiprocessing

def son_process():
#	num = int(input('a num big enough:'))
	print('son_process pid:{0:=^30d}'.format(os.getpid()))
	for i in range(5000):
		i += i
	print('i:',i)
	time.sleep(2)
	
if __name__ == '__main__':
	print('mon pid:{0:=^30d}'.format(os.getpid()))
	start = time.time()
	for i in range(2):
		son_process()	
	end = time.time()
	print('two times to do it used {0:.2f}s'.format(end - start))
	
	p1 = multiprocessing.Process(target=son_process,args=())
	p2 = multiprocessing.Process(target=son_process,args=())
	p1.start()
	p2.start()
	p1.join()
	p2.join()
	end2 = time.time()
	print('two processes run together {0:=^30.2f}'.format(end2-end))