import re

str = '<div class="name">中国</div>'
p = re.compile(r'<div class=".*?">(.*?)</div>')
print(p.findall(str))
print(str)

b = re.compile(r'<div class=".*">(.*)</div>')
print(b.findall(str))   #查找所有包含'b'的单词


m=re.search(r'(\d{3})-(\d{3})-(\d{4})','My phone number is 028-888-5566') #每个括号为一个组
print(m.group(1)) #返回第一组的值
print(m.group(2))
print(m.group(3))
print(m.group())#返回整个匹配的文本

