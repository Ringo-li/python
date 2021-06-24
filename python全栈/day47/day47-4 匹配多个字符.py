import re

# 1.正则表达式
# 2.匹配的字符串
# 3.返回的匹配结果

# * 前一个字符出现0次或者无数次
match_obj = re.match("t.*r", "tr")
if match_obj:
    result = match_obj.group()
    print(result)

else:
    print("匹配失败")

# + 前一个字符出现1次以上
match_obj = re.match("t.+r", "tor")
if match_obj:
    result = match_obj.group()
    print(result)

else:
    print("匹配失败")

# ? 前一个字符出现0次或1次
match_obj = re.match("https?:", "http:")
if match_obj:
    result = match_obj.group()
    print(result)

else:
    print("匹配失败")


# {m} 前一个字符必须出现m次
match_obj = re.match("ht{2}ps?:", "http:")
if match_obj:
    result = match_obj.group()
    print(result)

else:
    print("匹配失败")

# {m,n} 前一个字符出现m次到n次
match_obj = re.match("ht{2,4}ps?:", "httttp:")
if match_obj:
    result = match_obj.group()
    print(result)

else:
    print("匹配失败")

# {m,} 前一个字符出现m次以上
match_obj = re.match("ht{2,}ps?:", "htttttp:")
if match_obj:
    result = match_obj.group()
    print(result)

else:
    print("匹配失败")