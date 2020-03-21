urls = 'http://m.qiqipu.com/zxdm/49065/player.html?49065-0-10 '

import re

res = re.compile(r'\w{5}')
print(res.findall(urls))
print(res.search(urls).group())