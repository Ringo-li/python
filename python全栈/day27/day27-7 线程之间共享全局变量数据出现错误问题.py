## 全局变量global的用法
# num = 0
# def add():
#     for i in range(10):
#         # 当声明全局变量时，函数调用后num会被修改
#         # global num
#         num = 2 + 1
#
#     print(num)
# add()
# print(num)
## 可变数据类型和不可变数据类型的区别
# list = []
# def add():
#     for i in range(10):
#         # 当声明全局变量时，函数调用后num会被修改
#         # 列表是可变类型，不用global声明
#         # global num
#         list.append(i)
#
#     print(list)
#
# add()
# print(list)

import threading

# 全局变量
g_num = 0

def task1():
    for i in range(1000000):
        # g_gum是不可变类型，想要修改他，就要改变他的内存地址
        # 如果此处不声明global，每次取值都是0
        global g_num
        # 每次循环给全局变量加1
        g_num += 1
    print("task1:", g_num)

def task2():
    for i in range(1000000):
        # g_gum是不可变类型，想要修改他，就要改变他的内存地址
        # 如果此处不声明global，每次取值都是0
        global g_num
        # 每次循环给全局变量加1
        g_num += 1
    print("task2:", g_num)

if __name__ == '__main__':
    # 创建两个子线程
    first_thread = threading.Thread(target=task1)
    second_thread = threading.Thread(target=task2)
    # 主线程启动第一个子线程，从start开始，主线程和第一个子线程并发往下执行
    first_thread.start()
    # join时主线程会等待第一个子线程任务结束时再继续往下执行
    # first_thread.join()

    # 没有join时主线程直接到这里启动第二个子线程，从这个start开始，主线程和第一个、第二个子线程一起往下执行
    second_thread.start()
    # join时主线程会等待第二个子线程任务结束时再继续往下执行
    # second_thread.join()

    # 没有join时主线程来到了这里，直接打印了全局变量，此时全局变量已经被两个子线程改变了，但子线程没有join的话任务还没有执行完，g_num比较小
    print(g_num)



