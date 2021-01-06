s = '</div></a>"you think who you are?"</a>\n</a>"are you ok?"</a></a>"are you ok?"</a></div>'

import re

rea = re.compile(r'</a>(.*)</a>')
rea2 = re.compile(r'</a>(.*?)</a>')

res = rea.findall(s,re.S)

res11 = rea.findall(s)

print('不忽略换行findall',res11)
print('忽略换行findall.re.S',res)

res1 = rea2.findall(s)
print('非贪婪匹配不忽略换行findall',res1)

res12 = rea2.findall(s,re.S)
print('非贪婪匹配忽略换行findall.re.S',res12)

res2 = rea.search(s,re.S).group(1)
res22 = rea.search(s).group(1)
print('贪婪，忽略,search.re.S',res2)
print('贪婪，不忽略,search',res22)
res3 = rea2.search(s).group(1)
print('非贪婪,不忽略,search',res3)