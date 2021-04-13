import multiprocessing
import time

# 定义全局变量列表
g_list = []

# 添加数据任务
def add_data():
    for i in range(3):
        # 列表是可变类型，在原有内存基础上修改数据，内存地址不变，不需要加global关键字
        # 加上global的作用：声明要修改全局变量的内存地址
        g_list.append(i)
        print("添加:", i)
        time.sleep(0.2)
    print("添加完成：",g_list)

# 读取数据任务
def read_data():
    print("读取：", g_list)

# 创建添加数据子进程
add_process = multiprocessing.Process(target=add_data)

# 创建读取数据子进程
read_process = multiprocessing.Process(target=read_data)

# 直接执行的文件模块中必须加main
# 运行子进程
# windows创建子进程会复制一份主进程资源，在复制到子进程时，子进程又会递归往下复制
# 通过判断是否是主模块来解决windows递归创建子进程
if __name__ == '__main__':
    add_process.start()
    # 当前进程（主进程）等待添加数据进程完成以后代码再继续往下执行
    add_process.join()
    print("main读取", g_list)
    read_process.start()

# 结论：进程之间不共享全局变量