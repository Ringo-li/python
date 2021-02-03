class Washer():
    def __init__(self):
        self.width = 600
        self.height = 800

    def __del__(self):
        print("对象已经被删除")

haier = Washer()