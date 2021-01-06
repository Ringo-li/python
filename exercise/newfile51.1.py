url = 'https :// sycm. taobao. com/bda/tradinganaly/overview/get_summary. json?date Range =2018-03-20%7C2018-03-20 & dateType = recenti & device = 1 & token = ff 25b109b &_-1521595613462'

import re

rec = re.compile(r'\d{4}-\d{2}-\d{2}')

res = rec.findall(url)
print(res)