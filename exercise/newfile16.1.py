import re

str = '<div class="name">中之家国</div>'

res = re.search(r'<.*?>(.*?)<.*?>',str)
print(res.group(1))

res2 = re.search(r'[\u4e00-\u9fa5]{2,4}',str)
print(res2.group())