astr = '我们要替换掉这个分数:59'

bstr = astr.replace('59','95')
print(bstr)

import re

bstr = re.sub('\d+','89',astr)
print(bstr)