# 死锁：一直等待对方释放锁的情景叫死锁

import threading

# 创建互斥锁
lock = threading.Lock()

g_list = [i for i in range(3)]

# 需求：多线程同时根据下标在列表中取值，要保证同一时刻只能有一个线程去取值
def task(index):
    # 上锁
    lock.acquire()

    # 判断下标是否越界
    if index >= len(g_list):
        print("下标越界：", index)
        # 取值不成功，也要释放互斥锁，不然影响后面的线程取值，造成死锁
        lock.release()
        return
    # 根据下标取值
    value = g_list[index]
    print(value)
    # 释放锁
    lock.release()


if __name__ == '__main__':
    # 创建大量线程
    for i in range(10):
        sub_thread = threading.Thread(target=task, args=(i,))
        sub_thread.start()




