class Singleton(object):
	__instance = None
	
	def __new__(cls):
		if cls.__instance:
			pass
		else:
			cls.__instance = object.__new__(cls)
		return cls.__instance
		
a = Singleton()
b = Singleton()

#print(id(a),id(b))

#example2

class Single():
	instance = None
	
	def __new__(cls):
		if not cls.instance:
			cls.instance = super().__new__(cls)
		return cls.instance
		
c = Single()
d = Single()
print(id(c),id(d))
		