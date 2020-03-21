class Singleton(object):
	__instance = None
	
	def __new__(cls,age,name):
		if not cls.__instance:
			cls.__instance = object.__new__(cls)
		return cls.__instance

a = Singleton(18,'lily')
b = Singleton(8,'licy')
#c = Singleton()

print(id(a))
print(id(b))
print(Singleton('hdux',67))

a.age = 34
print(a.age)
print(b.age)

print(a)
print(b)

