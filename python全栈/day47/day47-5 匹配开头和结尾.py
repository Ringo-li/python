import re

# ^ 匹配开头
match_obj = re.match("^n.{3,}", "node")
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print("fail to match")

# $ 匹配结尾
match_obj = re.match("n.{3,}\d$", "nodes2")
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print("fail to match")

# [^] 除了指定字符外都匹配
match_obj = re.match("c[^eft]o", "coo")
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print("fail to match")