#1.准备数据

age = 18
name = "Tom"
weight = 75.5
stu_id = 1

#2.标准化格式输出
print('我的年龄是%d岁' % age)
print('my name is %s'  %name)


#小数点位数
print('my weight is %.2f' % weight)
print('my studante id is %d' % stu_id)
#位数补全
print('my studante id is %03d' % stu_id)
#多参数，和计算
print('I am %s, I will be %d next year' % (name, age + 1))
#%s可以格式化其他类型数据
print('I am %s, i am %s years old, and my weight is %s' % (name, age, weight))