import re

# | 对竖线两边的表达式分别进行匹配
fruit_list = ["apple", "orange", "banana", "peach", "pear"]
for fruit in fruit_list:
    match_obj = re.match("pear|peach", fruit)
    if match_obj:
        print("I like", fruit)
    else:
        print("I don't like", fruit)

# 匹配163、126、qq邮箱
match_obj = re.match("[0-9a-zA-Z][0-9a-zA-Z_]{4,19}@(126|163|qq)\.com", "hello_@126.com")
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print("fail to match")

# 从字符中提取一部分，使用分组
match_obj = re.match("([0-9a-zA-Z_]{4,20})@(qq|126|163)\.com", "hello_@126.com")
if match_obj:
    result = match_obj.group(1)
    style = match_obj.group(2)
    print(style)
    print(result)
else:
    print("fail match")

# 1.要前后呼应，使用引用分组
# 2.双反斜杠表示未转译的单反斜杠

str = "<html><div>nihao</div></html>"
match_obj = re.match("<([a-zA-Z0-6]+)><([a-zA-Z0-6]+)>(.*)</\\2></\\1>", str)
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print("fail to match")