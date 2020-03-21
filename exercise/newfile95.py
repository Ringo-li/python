title = 'hello,你好,world,世界'

import re

pattern = re.compile(r'[\u4e00-\u9fa5]+')
res = pattern.findall(title)
print(res)
strs = ''.join(res)
print(strs)
