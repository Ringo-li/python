url = 'htrp://qq.com/nuhaodud2018-04-31bat/%2$%/2018-04-32baesi/jcur.jpg'

import re

ret = re.compile('.*?(\d+-\d+-\d+).*?(\d+-\d+-\d+)')
res = re.search(ret,url)
print(res.group(2))
print(re.findall(ret,url))

resall = re.findall(ret,url)
print(type(resall))
print(resall[0][1])