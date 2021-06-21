# num表示生成斐波那契数列的个数
def fibonacci(num):
    # 初始化前两个值
    a = 0
    b = 1
    # 记录生成次数的索引
    index =0
    # 1.循环并判断条件是否成立
    while index < num:
        result = a
        # 2.利用算法推导数据,条件成立交换变量值
        a, b = b, a + b    
        index += 1
        yield result

# 创建生成器
num = fibonacci(15)
for i in num:
    print(i)