email = ['www.nihao@163.com','www.bihao163@com','www.buhao.163@com','www.haha@163.com.cn']

import re

a = re.compile(r'.*?@163.com$')
for i in email:
	res = a.search(i)
	print(res)

for i in email:
	a = re.search(r'.*?@163.com$',i)
	if a:
		print('%s is good'%i)
	else:
		print('%s is unavalible'%i)
