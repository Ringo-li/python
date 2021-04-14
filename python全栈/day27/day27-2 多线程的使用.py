# 1.导入线程模块
import threading
import time

def sing():
    # 获取当前线程
    current_thread = threading.current_thread()
    print(current_thread)
    for i in range(3):
        print("sing...")
        time.sleep(0.2)

def dance():
    # 获取当前线程
    current_thread = threading.current_thread()
    print(current_thread)
    for i in range(3):
        print("dance...")
        time.sleep(0.2)


if __name__ == '__main__':

    # 获取当前线程
    current_thread = threading.current_thread()
    print(current_thread)

    # 2.创建子线程
    sing_thread = threading.Thread(target=sing)
    dance_thread = threading.Thread(target=dance)
    # 3.启动子线程对应任务
    sing_thread.start()
    dance_thread.start()