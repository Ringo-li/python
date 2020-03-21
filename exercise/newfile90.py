phnum = ['123','284','736','2386','0295','6831','2649','2547']

import re
#选出四位以2开头不以为3,6,9结尾的数字
ref = re.compile('2\d{2}[0-2,4-5,7-8]') 

for i in phnum:
	res = ref.match(i)
	res2 = ref.findall(i)
	if res:
		print(res.group())
		print(res2)