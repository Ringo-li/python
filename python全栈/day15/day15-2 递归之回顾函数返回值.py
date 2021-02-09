# 函数返回值回顾： 1.写法：return 值 2.返回位置：函数调用的位置
def return_num():
    return 10
    print('此处代码不会被执行')

result = return_num()
print(result)