# 互斥锁可以保证同一时间只有一个线程去执行代码，能够保证全局变量的数据没有问题
# 线程等待（join）和互斥锁都是将多任务改成单任务去执行，保证了数据的准确性，但是执行效率降低。

import threading

# 全局变量
g_num = 0
# 创建互斥锁，Lock本质上是一个函数，通过调用函数创建一个互斥锁
lock = threading.Lock()

def task1():
    # 为了保证全局变量在使用中不能有其他线程进行操作，所以在使用全局变量前加锁
    # 所有使用全局变量的任务都要上锁，不然别处还是会修改全局变量
    lock.acquire()
    for i in range(1000000):
        # g_gum是不可变类型，想要修改他，就要改变他的内存地址
        # 如果此处不声明global，每次取值都是0
        global g_num
        # 每次循环给全局变量加1
        g_num += 1
    print("task1:", g_num)
    # 释放锁
    lock.release()

def task2():
    # 为了保证全局变量在使用中不能有其他线程进行操作，所以在使用全局变量前加锁
    # 所有使用全局变量的任务都要上锁，不然别处还是会修改全局变量
    lock.acquire()
    for i in range(1000000):
        # g_gum是不可变类型，想要修改他，就要改变他的内存地址
        # 如果此处不声明global，每次取值都是0
        global g_num
        # 每次循环给全局变量加1
        g_num += 1
    print("task2:", g_num)
    # 释放锁
    lock.release()

if __name__ == '__main__':
    # 创建两个子线程
    first_thread = threading.Thread(target=task1)
    second_thread = threading.Thread(target=task2)
    # 主线程启动第一个子线程，从start开始，主线程和第一个子线程并发往下执行
    first_thread.start()

    # 没有join时主线程直接到这里启动第二个子线程，从这个start开始，主线程和第一个、第二个子线程一起往下执行
    second_thread.start()

    # 没有join时主线程来到了这里，直接打印了全局变量，此时全局变量已经被两个子线程改变了，但子线程没有join的话任务还没有执行完，g_num比较小
    print(g_num)