urls = ['<html><h1>www.itcast.cn</h1></html>','<html><h2>www.itcast.cn</h2></html>','<html><h1>www.itcast.com</h1></html>']


import re


for url in urls:
#	ret = re.match(r'<(\w*)><(\w*)>.*?</2></1>',url)
	ret = re.match(r'<\w*><h1>(.*?)</h1>',url)
	if ret:
		print('right url:%s'%ret.group(1))
	else:
		print('not good:%s'%url)
