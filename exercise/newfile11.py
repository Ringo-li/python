# !/usr/bin/env python


# the first test

class Bike:
	def __init__(self,newWheelNum,newColor):
		self.wheel = newWheelNum
		self.color = newColor
	def move(self):
		mike = input('your num:')
		if mike == self.wheel:
			return ('i can move')
		else:
			return ('are you ok?')


#usename = input('car name:')
#usenum = int(input('your num:'))
#usecolor = input('your color:')
#	


#def main():	
#	try:
#		return(Bike(usenum,usecolor))
#		print(usename.move)
#	except ValueError :
#		print('one more again')

#if __name__ == '__main__':
#	main()
	
bikeA = Bike(2,'green')
#print(bikeA.wheel)


bikeB = Bike(4,'yellow')

#print(bikeB.move())
#print(bikeB.move(3))


# the second test

#class Person(object):
#	def __new__(cls,*args,**kwargs):
#		print('in __new__')
#		instance = object.__new__(cls,*args,**kwargs)
#		return instance
#		
#	def __init__(self,name,age):
#		print('in __init__')
#		self._name = name
#		self._age = age

#p = Person('xlzhang',33)
class Person(object):
    def __new__(cls, *args, **kwargs):
        print("in __new__")
        instance = object.__new__(cls, *args, **kwargs)
        return instance

    def __init__(self, name, age):
        print("in __init__")
        self._name = name
        self._age = age

#p = Person("Wang",33)

class Singleton(object):
	_instance = None
	def __new__(cls,*args,**kwargs):
		if cls._instance is None:
			cls._instance = object.__new__(cls,*args,**kwargs)
		return cls._instance
		
s1 = Singleton()
s2 = Singleton()

print(s1)
print(s2)


class Fruit(object):
	def __init__(self):
		pass
		
	def print_color(self):
		pass

class Apple(Fruit):
	def __init__(self):
		pass
		
	def print_color(self):
		print('Apple is red')
		
class Orange(Fruit):
	def __init__(self):
		pass
		
	def print_color(self):
		print('Orange is yellow')
		
class Fruit_Factory(object):
	fruits = {'Apple':Apple,'Orange':Orange}
	
	def __new__(cls,args):
		if args in cls.fruits.keys():
			return cls.fruits[args]()
		else:
			return Fruit()
			
fruit1 = Fruit_Factory('Apple')
fruit2 = Fruit_Factory('Orange')


fruit1.print_color()
fruit2.print_color()