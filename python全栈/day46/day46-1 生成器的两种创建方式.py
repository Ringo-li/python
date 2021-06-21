# 生成器：根据程序员指定的算法规则循环生成数据，当条件不成立时数据停止生成，这样每次都只生成一个数据，节省大量内存
# 创建生成器的两种方式
# 1.生成器推导式，把列表推导式的中括号换成小括号即可
# 2.yield关键字。只要函数中有yield关键字，这个函数就是一个生成器。

# 创建生成器
my_generator = (i ** 2 for i in range(4))
print(my_generator)

# 生成器取值,使用next函数获取生成器中的下一个值
# 当没有可取的值时,会抛出StopIteration,表示数据生成完毕 
# print(next(my_generator))
# print(next(my_generator))

# while True:
#     try:
#         value = next(my_generator)
#         print(value)
#     except Exception as e:
#         break

# for 循环内部调用next函数获取生成器中的下一个值,出现异常是for循环自动捕获
for i in my_generator:
    print(i)


# 在函数中有yield关键字,那么这个函数就是生成器
def my_generator():
    print("开始生成数据了...")
    # 当程序执行到yield时代码暂停并返回结果,再次启动生成器时从暂停位置继续向下
    for i in range(3):
        yield i
        print("上一次数据生成完了")

result = my_generator()
print(result)
for value in result:
    print(value)
