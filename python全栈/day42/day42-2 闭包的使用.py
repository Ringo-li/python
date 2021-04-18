# 外部函数接收姓名参数
def config_name(name):

    # 内部函数保存外部函数的参数，并且完成数据显示的拼接
    def inner(msg):
        print(name, ":", msg)
    # 外部函数要返回内部函数
    return inner

# 创建tom闭包实例
tom = config_name("Tom")
# 创建jerry闭包实例
jerry = config_name("Jerry")

# 在执行tom闭包时，因为已经保存了name参数，那么之后都会完成name和msg的拼接
tom("come here, babby!")
jerry("No, you are dangerous!")
tom("Bullshit, we are friend.")
