# 上下文管理器，在类里实现__enter__和__exit__方法，创建的对象就是上下文管理器

class File(object):
    def __init__(self, file_path, file_mode) -> None:
        self.file_path = file_path
        self.file_mode = file_mode

    def __enter__(self):
        # 上文方法，负责返回操作对象资源，比如文件或数据库连接对象
        self.file = open(self.file_path, self.file_mode)
        return self.file
    # 当with语句执行完成后自动执行__exit__方法，需要传入四个参数
    def __exit__(self, exc_type, exc_val, exc_tb):
        # 下文方法，负责释放资源，比如关闭文件和数据库连接
        print("over")
        self.file.close()

# with语句结合上下文管理器对象使用
with File("test.txt", "r") as file:
    content = file.read()
    print(content)
    # file.write("wahaha")
