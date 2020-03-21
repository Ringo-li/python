str = '<div class="name">中之家国</div>'

import re

res = re.compile('<.*?>(.*?)<')
print(res.search(str).group(1))
print(res.findall(str))