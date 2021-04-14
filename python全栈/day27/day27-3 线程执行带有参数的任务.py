# 以元组方式传参，顺序和函数参数一致
# 以字典方式传参，key名和函数参数一致

# 1.导入threading模块
import threading

def show_info(name, age):
    print("name: %s, age: %d" % (name, age))

if __name__ == '__main__':

    # 2.创建子线程
    # 以元组方式传参
    # sub_thread = threading.Thread(target=show_info, args=("lisa", 20))

    # 以字典方式传参
    sub_thread = threading.Thread(target=show_info, kwargs={"name": "luna", "age": 18})
    # 3.运行子线程
    sub_thread.start()