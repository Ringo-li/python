# 创建类
class Washer():
    def wash(self):
        print('I can wash')
        print(self)

# 实例化:
haier = Washer()
print(haier)

haier.wash()
# 打印对象和打印self得到相同的内存地址，所有self指的就是调用该函数的对象
