import multiprocessing
import time

# 主进程会等待子进程执行完毕后再退出

# 如果子进程是个死循环呢？
# 解决办法：主进程退出子进程销毁
# 1.让子进程设置为守护主进程，主进程退出，子进程销毁，子进程依赖与主进程。
# 2.在主进程退出前

def task():
    for i in range(10):
        print("任务执行中。。。")
        time.sleep(0.2)

# 判断是否是直接执行的模块，程序入口模块
#  标准python写法，直接执行的模块，需要加上判断是否是主模块的代码
if __name__ == '__main__':
    # 创建子进程
    sub_process = multiprocessing.Process(target=task)
    # 方法一，设置为守护主进程
    # sub_process.daemon = True

    sub_process.start()

    # 主进程延时0.5秒
    time.sleep(0.5)

    # 方法二，退出主进程前，先让子进程销毁
    sub_process.terminate()
    print("over")

