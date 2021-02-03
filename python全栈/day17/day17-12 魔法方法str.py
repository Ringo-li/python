class Washer():
    def __init__(self):
        self.width = 600
        self.height = 800
        print(self)

    def __str__(self):
        return "不用再打内存地址，打印这些内容"

haier = Washer()


    