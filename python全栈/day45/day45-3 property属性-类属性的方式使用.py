class Student(object):
    def __init__(self) -> None:
        # 私有属性
        self.__age = 0

    def get_age(self):
        print("获取属性")
        return self.__age

    def set_age(self, new_age):
        print("设置属性")
        self.__age = new_age
    # property关键字，是一个类，传参依次是获取、设置、删除
    age = property(get_age, set_age)

student = Student()
age = student.age
print(age)
student.age = 30
age = student.age
print(age)