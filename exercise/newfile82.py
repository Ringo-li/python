s = "info:xiaozhang 33 shandong,xuesheng" 

import re

a = re.split(r':| |,',s)
print(a)