# 需求：警务人员和警犬一起工作，携带不同类型的警犬完成不同的工作

# 定义父类，提供公共方法 需求上归类：人和警犬
class Dog(object):
    def work(self):
        pass

class Person(object):
    def work_with_dog(self, dog):
        dog.work()

# 定义子类，重写父类方法 定义两个不同种类的警犬
class ArmyDog(Dog):
    def work(self):
        print('追击敌人')

class DrugDog(Dog):
    def work(self):
        print('追查毒品')

# 传递子类对象给调用者，可以看到不同子类执行效果不同 

armydog = ArmyDog()
drugdog = DrugDog()

xiaoli = Person()
xiaoli.work_with_dog(armydog)
xiaoli.work_with_dog(drugdog)



