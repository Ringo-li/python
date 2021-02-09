# 需求：定义一个函数，返回值100
# 1.普通函数
def return_num():
    return 100
result = return_num()
print(result)

# 2.lambda
# lambda 参数列表（可有可无）:（冒号不可省略） 表达式（表达式不可省略）
fn = lambda :100
result = fn()
print(result)
