import threading as td
import time
import subprocess as sp

def pingtool(ip):
	res = sp.call('ping -c2 -i0.2 -w1 12%s.0.0.1 &> /dev/null '%ip,shell=True)
	if res:
		print('{0:#^30d} is NOT ok'.format(ip))		
	else:
		print('{0:=^30d} is OK one'.format(ip))
if __name__ == '__main__':
	start = time.time()
	for i in range(5,100):
		pingtool(i)
	end = time.time()
	print('it used {0:.2f}s if in order'.format(end - start))
	for i in range(5,9):
		print('{} is rung'.format(td.current_thread().name))
		p1 = td.Thread(target=pingtool,args=(i,))
		p1.start()
#		p1.join()
	end1 = time.time()
	print('it used {0:.2f}s if thread'.format(end1 - end))