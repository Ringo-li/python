class Washer():
    def __init__(self, width, height):
        # 添加实例属性
        self.width = width
        self.height = height

    def print_info(self):
        print('我的高度是{}'.format(self.height))
        print('我的宽度是{}'.format(self.width))

haier = Washer(500, 800)
haier.print_info()

xiaotiane = Washer(600, 800)
xiaotiane.print_info()