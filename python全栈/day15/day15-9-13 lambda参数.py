# 1.无参数
fn = lambda: 100
print(fn())

# 2.一个参数
fn2 = lambda a: a + '!'
print(fn2('hello world'))

# 3.默认参数
fn3 = lambda a, b, c=100 : a + b + c
print(fn3(10 ,20, 30))
print(fn3(10, 20))

# 4.可变参数*args
# 可变参数传入lambda后，返回一个元组
fn4 = lambda *args: args
print(fn4(12, 32, 'ds'))
print(fn4(12))

# 5.可变参数**kwargs
# 收集不定长关键字参数，返回一个字典
fn5 = lambda **kwargs: kwargs
print(fn5(aa=1, name='python'))
