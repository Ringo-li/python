import re

s = '小明年龄18工资10000'

res1 = re.search('\d+',s).group()
print(res1)

res2 = re.findall('\d+',s)
print(res2)

res3 = re.match('小明',s).group()
print(res3)

res4 = re.match('小明.*?年龄(\d+)工资(\d+)',s).group(2)
print(res4)

res5 = re.match('小明',s)
print(res5)

res = re.compile('.*?(\d+).*?(\d+).*?')

print(res.match(s).group(2))
print(res.search(s).group(1))
print(res.findall(s)[0][1])