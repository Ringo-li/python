# 定义加p标签的装饰器
def make_p(func):
    def inner():
        # 在内部对已有函数进行装饰
        content = "<p>" + func() + "</p>"
        return content
    return inner

# 定义加div标签的装饰器
def make_div(func):
    def inner():
        # 在内部对已有函数进行装饰
        content = "<div>" + func() + "</div>"
        return content
    return inner

# 多个装饰器执行过程：由内向外执行

@make_div # content = make_div(make_p(content)), content = make_div.inner
@make_p # content = make_p(content), content = make_p.inner
def content():
    return "人生苦短，我用pyton！"

# 用装饰器加上p标签
result = content()
print(result)