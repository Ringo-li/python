# 需求：两个数字比大小，返回较大值
# lambda, 三目运算符
fn = lambda a, b: a if a > b else b
print(fn(100, 50))
print(fn(100, 500))