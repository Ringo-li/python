# 定义加p标签的装饰器
def make_p(func):
    def inner():

        content = "<p>" + func() + "</p>"
    return inner

@make_p
def content():
    print("人生苦短，我用pyton！")

# 用装饰器加上p标签
content()