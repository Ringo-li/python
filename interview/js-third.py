# 输入3[m2[c]]，输出  mccmccmcc
import re
# s = '3[m2[c]]'.replace(']', '')
s = '3[mds]'.replace(']', '')
b = re.sub(r'(\d+).*?([a-z]+)', r'\1*"\2"', s)
