from contextlib import contextmanager

# 加上装饰器，下面的函数创建的对象就是一个上下文管理器
@contextmanager
def my_open(file_name, file_mode):
    try:
        file = open(file_name, file_mode)
        # yield之前的方法可以看作上文方法，负责返回操作对象资源
        yield file
    except Exception as e:
        print(e)
    finally:
        print("over")
        # yield关键字之后代码可以认为是下文方法，负责释放资源。
        file.close()

# 普通函数不能结合with语言使用，with语句只和上下文管理器结合使用
with my_open("test.txt", "r") as file:
    # content = file.read()
    # print(content)
    file.write("WAHAHA")