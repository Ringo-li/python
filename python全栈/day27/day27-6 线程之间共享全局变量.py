# 结论:线程之间共享全局变量
import threading
import time

g_list = []

# 添加数据任务
def add_data():
    for i in range(3):
        g_list.append(i)
        print("add:", g_list)
        time.sleep(0.3)
    print("add finish: ", g_list)

# 读取数据任务
def read_data():
    print("read data: ", g_list)

if __name__ == '__main__':
    # 创建子线程
    add_thread = threading.Thread(target=add_data)
    read_thread = threading.Thread(target=read_data)

    # 运行子线程
    add_thread.start()
    # 让当前线程(主线程)等待添加数据线程执行完毕后继续往下执行
    add_thread.join()
    read_thread.start()