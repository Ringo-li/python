# 1.导入模块
import multiprocessing

# 2.创建任务子进程
def show_info(name, age):
    print(name, age)

# 以元组方式传参,传参顺序要和函数保持一致
# sub_process = multiprocessing.Process(target=show_info, args=('lisi', 20))

# 以字典方式传参，传参key要和函数保持一致
sub_process = multiprocessing.Process(target=show_info, kwargs={"age":15, "name":'zhangsan'})

# 调用
if __name__ == '__main__':
    sub_process.start()
