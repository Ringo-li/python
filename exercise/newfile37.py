s = '</div></a>"you think who you are?"</a></a>"are you ok?"</a></div>'

import re

res1 = re.findall('</a>(.*?)</a></a>(.*?)</a>',s)
print(res1)

res12 = re.search('</a>(.*?)</a></a>(.*?)</a>',s,re.S)#忽略换行
print(res12.group(2))

res2 = re.findall('</a>(.*)</a>',s)
print(res2)

p=re.compile('(\w).(\w)')
print(p.search('1a2b3c').group(2))#匹配第二个出现的字符