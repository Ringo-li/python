str = '这里说了一堆,但是小明只得了68分'
print(str)
import re

rec1 = re.sub('\d+','98',str)
print(rec1)

rec2 = re.sub('只','已然',rec1)
print(rec2)