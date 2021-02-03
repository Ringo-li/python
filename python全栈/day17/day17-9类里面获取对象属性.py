class Washer():
    def wash(self):
        print('I can wash')
        print(self)

    # 类里面获取对象的属性，语法：self.属性名
    def print_info(self):
        print('我的高度是{}'.format(self.height))
        print('我的宽度是{}'.format(self.width))

haier = Washer()

haier.height = 800
haier.width = 600

haier.print_info()