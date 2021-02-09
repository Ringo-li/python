class Dog(object):
    tooth = 30

wangcai = Dog()
xiaohei = Dog()

# 1.类对象修改类属性 类名.属性 = 值
Dog.tooth = 32

print(Dog.tooth)        #32
print(wangcai.tooth)    #32
print(xiaohei.tooth)    #32
# 2.实例对象修改类属性
wangcai.tooth = 36

print(Dog.tooth)        #32
print(wangcai.tooth)    #36
print(xiaohei.tooth)    #32