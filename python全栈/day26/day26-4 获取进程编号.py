# 1.导入多进程包
import multiprocessing
import time
import os


# 获取主进程id
main_process_id = os.getpid()
print('main_process_id:', main_process_id)

def dance():
    # 获取当前进程ID
    dance_process_id = os.getpid()
    print('dance_process_id:', dance_process_id)
    dance_parent_process_id = os.getppid()
    print('dance_parent_process_id:', dance_parent_process_id)

    for i in range(3):
        print('dancing...')
        time.sleep(0.2)
        # 扩展：根据进程编号强制杀死指定进程
        os.kill(dance_process_id, 9)



def sing():
    sing_process_id = os.getpid()
    print('sing_process_id:', sing_process_id)
    sing_parent_process_id = os.getppid()
    print('sing_parent_process_id:', sing_parent_process_id)
    for i in range(3):
        print('singing...')
        time.sleep(0.2)




# 2.创建子进程对象
sing_process = multiprocessing.Process(target=sing)
dance_process = multiprocessing.Process(target=dance)

# 3.运行子进程
if __name__ == '__main__':
    sing_process.start()
    dance_process.start()