class Washer():
    def wash(self):
        print('I can wash')
        print(self)

haier = Washer()
# 类外面添加对象属性
haier.height = 800
haier.width = 600

# 类外面获取对象的属性，语法：对象名.属性名
print('haier的宽度是{}'.format(haier.width))
print('haier的高度是{}'.format(haier.height))


