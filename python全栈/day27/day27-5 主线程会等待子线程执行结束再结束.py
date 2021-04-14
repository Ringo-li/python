import threading
import time

def task():
    while True:
        print("singing...")
        time.sleep(0.3)

if __name__ == '__main__':
    # 主线程延时一秒后退出,发现不起作用,说明主线程会等待子线程执行结束再结束,exit也没用
    # 解决办法,设置子线程为守护主线程
    # 写法一
    # sub_thread = threading.Thread(target=task)
    # sub_thread.daemon = True

    # 写法二
    sub_thread = threading.Thread(target=task, daemon=True)

    sub_thread.start()
    time.sleep(1)
    print("over...")
    # exit()