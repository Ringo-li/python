# 第一步：导包
import multiprocessing
import  time

# 跳舞任务
def dance():
    for i in range(3):
        print('dancing...')
        time.sleep(0.2)

# 唱歌任务
def sing():
    for i in range(3):
        print('singing...')
        time.sleep(0.2)

# 第二部：创建进程对象（自己手动创建的进程叫做子进程,在__init__文件中已经导入Process类，所以不用包.文件.类）
# 1.target：进程执行的目标任务
# 2.name：进程名，默认Process-1
dance_process = multiprocessing.Process(target=dance)
sing_process = multiprocessing.Process(target=sing)
# 第三步：启动进程对应的任务
# 在windows中执行一定要加 if __name__ == '__main__':
if __name__ == '__main__':
    dance_process.start()
    sing_process.start()

    # 主进程执行唱歌任务
    # sing()