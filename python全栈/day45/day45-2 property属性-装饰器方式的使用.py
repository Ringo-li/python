class Student(object):
    def __init__(self) -> None:
        #  私有属性
        self.__age = 0

    @property # 当调用age属性时会调用下面的方法（方法转属性）
    def age(self):
        print("获取属性")
        return self.__age
    
    @age.setter # 当调用属性修改时会调用以下方法
    def age(self, new_age):
        print("设置属性")
        if new_age >= 0 and new_age <= 130:
            self.__age = new_age
        else:
            print("你确定？")

        
# 调用装饰器方法的property属性方法名要保持一致

student = Student()
age = student.age
print(age)

student.age = 34
age = student.age
print(age)
